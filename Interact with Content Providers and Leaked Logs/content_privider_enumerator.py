#!/usr/bin/env python3

import subprocess
import re
import json
import sys
from datetime import datetime

class ContentProviderEnumerator:
    def __init__(self):
        self.device_id = None
        self.providers = []
        self.results = {}
        
    def check_device_connection(self):
        """Check if Android device is connected"""
        try:
            result = subprocess.run(['adb', 'devices'], 
                                  capture_output=True, text=True)
            if 'device' in result.stdout:
                print("[+] Android device connected")
                return True
            else:
                print("[-] No Android device found")
                return False
        except Exception as e:
            print(f"[-] Error checking device: {e}")
            return False
    
    def enumerate_providers(self):
        """Enumerate all content providers on the device"""
        print("[*] Enumerating content providers...")
        
        try:
            result = subprocess.run(['adb', 'shell', 'dumpsys', 'package', 'providers'],
                                  capture_output=True, text=True)
            
            # Parse provider information
            provider_pattern = r'Provider{[^}]+} (.+?):'
            authority_pattern = r'authority=([^,\s]+)'
            
            providers = re.findall(provider_pattern, result.stdout)
            authorities = re.findall(authority_pattern, result.stdout)
            
            self.providers = list(zip(providers, authorities))
            print(f"[+] Found {len(self.providers)} content providers")
            
            return self.providers
            
        except Exception as e:
            print(f"[-] Error enumerating providers: {e}")
            return []
    
    def test_provider_access(self, authority):
        """Test access to a specific content provider"""
        test_uris = [
            f"content://{authority}/",
            f"content://{authority}/users",
            f"content://{authority}/data",
            f"content://{authority}/settings",
            f"content://{authority}/accounts"
        ]
        
        accessible_uris = []
        
        for uri in test_uris:
            try:
                result = subprocess.run(['adb', 'shell', 'content', 'query', 
                                       '--uri', uri], 
                                      capture_output=True, text=True, timeout=10)
                
                if result.returncode == 0 and 'Row:' in result.stdout:
                    accessible_uris.append(uri)
                    print(f"[+] Accessible URI: {uri}")
                    
            except subprocess.TimeoutExpired:
                print(f"[-] Timeout accessing: {uri}")
            except Exception as e:
                print(f"[-] Error accessing {uri}: {e}")
        
        return accessible_uris
    
    def extract_data(self, uri):
        """Extract data from accessible content provider URI"""
        try:
            result = subprocess.run(['adb', 'shell', 'content', 'query', 
                                   '--uri', uri], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                return result.stdout
            else:
                return None
                
        except Exception as e:
            print(f"[-] Error extracting data from {uri}: {e}")
            return None
    
    def analyze_sensitive_data(self, data):
        """Analyze extracted data for sensitive information"""
        sensitive_patterns = {
            'password': r'password[=:]\s*([^\s,]+)',
            'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
            'token': r'token[=:]\s*([a-zA-Z0-9]+)',
            'api_key': r'api[_-]?key[=:]\s*([a-zA-Z0-9]+)'
        }
        
        findings = {}
        
        for pattern_name, pattern in sensitive_patterns.items():
            matches = re.findall(pattern, data, re.IGNORECASE)
            if matches:
                findings[pattern_name] = matches
                print(f"[!] Found {pattern_name}: {matches}")
        
        return findings
    
    def run_full_enumeration(self):
        """Run complete content provider enumeration and analysis"""
        print("="*60)
        print("Content Provider Security Assessment")
        print("="*60)
        
        if not self.check_device_connection():
            return
        
        # Enumerate providers
        providers = self.enumerate_providers()
        
        if not providers:
            print("[-] No content providers found")
            return
        
        # Test each provider
        for provider_name, authority in providers:
            print(f"\n[*] Testing provider: {provider_name}")
            print(f"[*] Authority: {authority}")
            
            accessible_uris = self.test_provider_access(authority)
            
            if accessible_uris:
                self.results[authority] = {
                    'provider_name': provider_name,
                    'accessible_uris': accessible_uris,
                    'extracted_data': {},
                    'sensitive_findings': {}
                }
                
                # Extract and analyze data
                for uri in accessible_uris:
                    data = self.extract_data(uri)
                    if data:
                        self.results[authority]['extracted_data'][uri] = data
                        sensitive_data = self.analyze_sensitive_data(data)
                        if sensitive_data:
                            self.results[authority]['sensitive_findings'][uri] = sensitive_data
        
        # Generate report
        self.generate_report()
    
    def generate_report(self):
        """Generate assessment report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"content_provider_assessment_{timestamp}.json"
        
        with open(report_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n[+] Assessment complete. Report saved to: {report_file}")
        
        # Print summary
        print("\n" + "="*60)
        print("ASSESSMENT SUMMARY")
        print("="*60)
        
        total_providers = len(self.results)
        vulnerable_providers = sum(1 for r in self.results.values() 
                                 if r['sensitive_findings'])
        
        print(f"Total providers tested: {total_providers}")
        print(f"Vulnerable providers: {vulnerable_providers}")
        
        if vulnerable_providers > 0:
            print("\n[!] SECURITY ISSUES FOUND:")
            for authority, data in self.results.items():
                if data['sensitive_findings']:
                    print(f"  - {authority}: {len(data['sensitive_findings'])} issues")

if __name__ == "__main__":
    enumerator = ContentProviderEnumerator()
    enumerator.run_full_enumeration()

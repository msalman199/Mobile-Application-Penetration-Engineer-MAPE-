#!/usr/bin/env python3
"""
API Key Detection Script for Android APK Analysis
This script searches for hardcoded API keys and sensitive information in decompiled APK files.
"""

import os
import re
import sys
import json
from pathlib import Path

class APIKeyDetector:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)
        self.findings = []
        
        # Define patterns for different types of API keys and secrets
        self.patterns = {
            'generic_api_key': r'(?i)(api[_-]?key|apikey)\s*[:=]\s*["\']([a-zA-Z0-9_-]{20,})["\']',
            'access_token': r'(?i)(access[_-]?token|accesstoken)\s*[:=]\s*["\']([a-zA-Z0-9_.-]{20,})["\']',
            'secret_key': r'(?i)(secret[_-]?key|secretkey)\s*[:=]\s*["\']([a-zA-Z0-9_-]{20,})["\']',
            'bearer_token': r'(?i)bearer\s+([a-zA-Z0-9_.-]{20,})',
            'aws_access_key': r'AKIA[0-9A-Z]{16}',
            'aws_secret_key': r'(?i)aws[_-]?secret[_-]?access[_-]?key["\']?\s*[:=]\s*["\']([a-zA-Z0-9/+=]{40})["\']',
            'google_api_key': r'AIza[0-9A-Za-z_-]{35}',
            'firebase_key': r'(?i)firebase[_-]?key["\']?\s*[:=]\s*["\']([a-zA-Z0-9_-]{20,})["\']',
            'base64_encoded': r'[A-Za-z0-9+/]{40,}={0,2}',
            'long_hex_string': r'[a-fA-F0-9]{32,}',
            'jwt_token': r'eyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*'
        }
    
    def scan_file(self, file_path):
        """Scan a single file for API keys and secrets"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            for pattern_name, pattern in self.patterns.items():
                matches = re.finditer(pattern, content)
                for match in matches:
                    finding = {
                        'file': str(file_path.relative_to(self.apk_path)),
                        'pattern': pattern_name,
                        'match': match.group(0),
                        'line_number': content[:match.start()].count('\n') + 1
                    }
                    self.findings.append(finding)
                    
        except Exception as e:
            print(f"Error scanning {file_path}: {e}")
    
    def scan_directory(self):
        """Recursively scan all files in the APK directory"""
        file_extensions = ['.xml', '.smali', '.txt', '.properties', '.json', '.js', '.java']
        
        for file_path in self.apk_path.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in file_extensions:
                self.scan_file(file_path)
    
    def generate_report(self):
        """Generate a detailed report of findings"""
        if not self.findings:
            print("No potential API keys or secrets found.")
            return
        
        print(f"\n=== API Key Detection Report ===")
        print(f"Scanned APK: {self.apk_path}")
        print(f"Total findings: {len(self.findings)}\n")
        
        # Group findings by pattern type
        by_pattern = {}
        for finding in self.findings:
            pattern = finding['pattern']
            if pattern not in by_pattern:
                by_pattern[pattern] = []
            by_pattern[pattern].append(finding)
        
        for pattern_name, findings in by_pattern.items():
            print(f"--- {pattern_name.upper().replace('_', ' ')} ({len(findings)} found) ---")
            for finding in findings[:5]:  # Show first 5 matches per pattern
                print(f"  File: {finding['file']}")
                print(f"  Line: {finding['line_number']}")
                print(f"  Match: {finding['match'][:100]}...")
                print()
            
            if len(findings) > 5:
                print(f"  ... and {len(findings) - 5} more matches\n")
    
    def save_report(self, output_file):
        """Save findings to a JSON file"""
        with open(output_file, 'w') as f:
            json.dump(self.findings, f, indent=2)
        print(f"Detailed report saved to: {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 api_key_detector.py <path_to_extracted_apk>")
        sys.exit(1)
    
    apk_path = sys.argv[1]
    if not os.path.exists(apk_path):
        print(f"Error: Path {apk_path} does not exist")
        sys.exit(1)
    
    detector = APIKeyDetector(apk_path)
    print("Scanning for API keys and secrets...")
    detector.scan_directory()
    detector.generate_report()
    
    # Save detailed report
    output_file = f"../results/api_key_report_{Path(apk_path).name}.json"
    detector.save_report(output_file)

if __name__ == "__main__":
    main()

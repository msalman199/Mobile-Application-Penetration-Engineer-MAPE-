#!/usr/bin/env python3
"""
Enhanced API Key Detection Script with Entropy Analysis
"""

import os
import re
import sys
import json
import math
from pathlib import Path
from collections import Counter

class EnhancedAPIKeyDetector:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)
        self.findings = []
        self.high_entropy_strings = []
        
        # Enhanced patterns with more specific matching
        self.patterns = {
            'google_api_key': r'AIza[0-9A-Za-z_-]{35}',
            'firebase_key': r'(?i)(firebase[_-]?key|firebase[_-]?token)["\']?\s*[:=]\s*["\']([a-zA-Z0-9_-]{20,})["\']',
            'aws_access_key': r'AKIA[0-9A-Z]{16}',
            'github_token': r'gh[pousr]_[A-Za-z0-9_]{36}',
            'slack_token': r'xox[baprs]-[0-9a-zA-Z-]{10,48}',
            'stripe_key': r'sk_live_[0-9a-zA-Z]{24}',
            'generic_secret': r'(?i)(secret|password|pwd|pass)["\']?\s*[:=]\s*["\']([a-zA-Z0-9!@#$%^&*()_+-=]{8,})["\']',
            'base64_pattern': r'[A-Za-z0-9+/]{40,}={0,2}',
            'hex_pattern': r'[a-fA-F0-9]{32,64}',
            'jwt_token': r'eyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*'
        }
    
    def calculate_entropy(self, string):
        """Calculate Shannon entropy of a string"""
        if len(string) == 0:
            return 0
        
        entropy = 0
        for count in Counter(string).values():
            probability = count / len(string)
            entropy -= probability * math.log2(probability)
        
        return entropy
    
    def is_high_entropy(self, string, threshold=4.5):
        """Check if string has high entropy (likely random/encoded)"""
        return self.calculate_entropy(string) > threshold and len(string) > 15
    
    def extract_context(self, content, match_start, match_end, context_size=50):
        """Extract context around a match"""
        start = max(0, match_start - context_size)
        end = min(len(content), match_end + context_size)
        return content[start:end]
    
    def scan_file_enhanced(self, file_path):
        """Enhanced file scanning with entropy analysis"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Pattern-based detection
            for pattern_name, pattern in self.patterns.items():
                matches = re.finditer(pattern, content)
                for match in matches:
                    context = self.extract_context(content, match.start(), match.end())
                    
                    finding = {
                        'file': str(file_path.relative_to(self.apk_path)),
                        'pattern': pattern_name,
                        'match': match.group(0),
                        'line_number': content[:match.start()].count('\n') + 1,
                        'context': context,
                        'entropy': self.calculate_entropy(match.group(0)),
                        'confidence': self.assess_confidence(pattern_name, match.group(0), context)
                    }
                    self.findings.append(finding)
            
            # High entropy string detection
            string_pattern = r'["\']([a-zA-Z0-9+/=_-]{20,})["\']'
            for match in re.finditer(string_pattern, content):
                string_value = match.group(1)
                if self.is_high_entropy(string_value):
                    context = self.extract_context(content, match.start(), match.end())
                    
                    entropy_finding = {
                        'file': str(file_path.relative_to(self.apk_path)),
                        'pattern': 'high_entropy_string',
                        'match': string_value,
                        'line_number': content[:match.start()].count('\n') + 1,
                        'context': context,
                        'entropy': self.calculate_entropy(string_value),
                        'confidence': 'medium'
                    }
                    self.high_entropy_strings.append(entropy_finding)
                    
        except Exception as e:
            print(f"Error scanning {file_path}: {e}")
    
    def assess_confidence(self, pattern_name, match, context):
        """Assess confidence level of the finding"""
        high_confidence_patterns = ['google_api_key', 'aws_access_key', 'github_token']
        
        if pattern_name in high_confidence_patterns:
            return 'high'
        
        # Check context for suspicious keywords
        suspicious_keywords = ['test', 'example', 'demo', 'placeholder', 'dummy']
        context_lower = context.lower()
        
        if any(keyword in context_lower for keyword in suspicious_keywords):
            return 'low'
        
        return 'medium'
    
    def scan_directory(self):
        """Scan all relevant files in the directory"""
        file_extensions = ['.xml', '.smali', '.txt', '.properties', '.json', '.js', '.java', '.kt']
        
        for file_path in self.apk_path.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in file_extensions:
                self.scan_file_enhanced(file_path)
    
    def generate_enhanced_report(self):
        """Generate comprehensive report"""
        print(f"\n=== Enhanced API Key Detection Report ===")
        print(f"Scanned APK: {self.apk_path}")
        print(f"Pattern-based findings: {len(self.findings)}")
        print(f"High entropy strings: {len(self.high_entropy_strings)}")
        
        # High confidence findings
        high_conf = [f for f in self.findings if f['confidence'] == 'high']
        if high_conf:
            print(f"\n--- HIGH CONFIDENCE FINDINGS ({len(high_conf)}) ---")
            for finding in high_conf:
                print(f"  Pattern: {finding['pattern']}")
                print(f"  File: {finding['file']}:{finding['line_number']}")
                print(f"  Match: {finding['match']}")
                print(f"  Entropy: {finding['entropy']:.2f}")
                print(f"  Context: ...{finding['context']}...")
                print()
        
        # Medium confidence findings
        med_conf = [f for f in self.findings if f['confidence'] == 'medium']
        if med_conf:
            print(f"\n--- MEDIUM CONFIDENCE FINDINGS ({len(med_conf)}) ---")
            for finding in med_conf[:3]:  # Show first 3
                print(f"  Pattern: {finding['pattern']}")
                print(f"  File: {finding['file']}:{finding['line_number']}")
                print(f"  Match: {finding['match'][:50]}...")
                print()
        
        # High entropy strings
        if self.high_entropy_strings:
            print(f"\n--- HIGH ENTROPY STRINGS (Top 5) ---")
            sorted_entropy = sorted(self.high_entropy_strings, 
                                  key=lambda x: x['entropy'], reverse=True)
            for finding in sorted_entropy[:5]:
                print(f"  File: {finding['file']}:{finding['line_number']}")
                print(f"  String: {finding['match'][:50]}...")
                print(f"  Entropy: {finding['entropy']:.2f}")
                print()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 enhanced_api_detector.py <path_to_extracted_apk>")
        sys.exit(1)
    
    apk_path = sys.argv[1]
    detector = EnhancedAPIKeyDetector(apk_path)
    
    print("Running enhanced API key detection...")
    detector.scan_directory()
    detector.generate_enhanced_report()
    
    # Save results
    all_findings = {
        'pattern_findings': detector.findings,
        'entropy_findings': detector.high_entropy_strings
    }
    
    output_file = f"../results/enhanced_report_{Path(apk_path).name}.json"
    with open(output_file, 'w') as f:
        json.dump(all_findings, f, indent=2)
    
    print(f"\nDetailed report saved to: {output_file}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import subprocess
import re
import json
import time
from datetime import datetime
from collections import defaultdict

class LogAnalyzer:
    def __init__(self):
        self.sensitive_patterns = {
            'passwords': [
                r'password[=:\s]+([^\s,\)]+)',
                r'pwd[=:\s]+([^\s,\)]+)',
                r'pass[=:\s]+([^\s,\)]+)'
            ],
            'emails': [
                r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            ],
            'phone_numbers': [
                r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
                r'\+\d{1,3}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}'
            ],
            'credit_cards': [
                r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
            ],
            'tokens': [
                r'token[=:\s]+([a-zA-Z0-9_-]+)',
                r'auth[=:\s]+([a-zA-Z0-9_-]+)',
                r'bearer\s+([a-zA-Z0-9_-]+)'
            ],
            'api_keys': [
                r'api[_-]?key[=:\s]+([a-zA-Z0-9_-]+)',
                r'secret[=:\s]+([a-zA-Z0-9_-]+)'
            ],
            'database_info': [
                r'INSERT\s+INTO\s+\w+.*VALUES.*',
                r'UPDATE\s+\w+\s+SET.*',
                r'SELECT.*FROM\s+\w+.*'
            ]
        }
        
        self.findings = defaultdict(list)
    
    def capture_logs(self, duration=30):
        """Capture logs for specified duration"""
        print(f"[*] Capturing logs for {duration} seconds...")
        
        try:
            # Clear existing logs
            subprocess.run(['adb', 'logcat', '-c'], check=True)
            
            # Capture logs
            result = subprocess.run(['adb', 'logcat', '-d'], 
                                  capture_output=True, text=True, 
                                  timeout=duration)
            
            return result.stdout
            
        except subprocess.TimeoutExpired:
            print("[*] Log capture completed")
            return ""
        except Exception as e:
            print(f"[-] Error capturing logs: {e}")
            return ""
    
    def analyze_logs(self, log_data):
        """Analyze logs for sensitive information"""
        print("[*] Analyzing logs for sensitive data...")
        
        lines = log_data.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            for category, patterns in self.sensitive_patterns.items():
                for pattern in patterns:
                    matches = re.findall(pattern, line, re.IGNORECASE)
                    if matches:
                        self.findings[category].append({
                            'line_number': line_num,
                            'line_content': line.strip(),
                            'matches': matches,
                            'timestamp': self.extract_timestamp(line)
                        })
    
    def extract_timestamp(self, log_line):
        """Extract timestamp from log line"""
        timestamp_pattern = r'(\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d{3})'
        match = re.search(timestamp_pattern, log_line)
        return match.group(1) if match else "Unknown"
    
    def monitor_realtime(self, duration=60):
        """Monitor logs in real-time"""
        print(f"[*] Starting real-time log monitoring for {duration} seconds...")
        
        try:
            process = subprocess.Popen(['adb', 'logcat'], 
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE,
                                     text=True)
            
            start_time = time.time()
            
            while time.time() - start_time < duration:
                line = process.stdout.readline()
                if line:
                    self.analyze_single_line(line.strip())
                    
            process.terminate()
            
        except Exception as e:
            print(f"[-] Error in real-time monitoring: {e}")
    
    def analyze_single_line(self, line):
        """Analyze a single log line"""
        for category, patterns in self.sensitive_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    print(f"[!] REAL-TIME ALERT - {category}: {matches}")
                    self.findings[category].append({
                        'line_content': line,
                        'matches': matches,
                        'timestamp': self.extract_timestamp(line),
                        'real_time': True
                    })
    
    def generate_report(self):
        """Generate analysis report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"log_analysis_report_{timestamp}.json"
        
        # Convert defaultdict to regular dict for JSON serialization
        report_data = {
            'analysis_timestamp': timestamp,
            'total_findings': sum(len(findings) for findings in self.findings.values()),
            'findings_by_category': dict(self.findings)
        }
        
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n[+] Analysis report saved to: {report_file}")
        
        # Print summary
        self.print_summary()
    
    def print_summary(self):
        """Print analysis summary"""
        print("\n" + "="*60)
        print("LOG ANALYSIS SUMMARY")
        print("="*60)
        
        if not self.findings:
            print("[+] No sensitive data found in logs")
            return
        
        for category, findings in self.findings.items():
            if findings:
                print(f"\n[!] {category.upper()}: {len(findings)} instances found")
                for finding in findings[:3]:  # Show first 3 instances
                    print(f"    - {finding['matches']}")
                if len(findings) > 3:
                    print(f"    ... and {len(findings) - 3} more")
    
    def run_analysis(self, mode='capture', duration=30):
        """Run log analysis"""
        print("="*60)
        print("Android Log Security Analysis")
        print("="*60)
        
        if mode == 'capture':
            log_data = self.capture_logs(duration)
            if log_data:
                self.analyze_logs(log_data)
        elif mode == 'realtime':
            self.monitor_realtime(duration)
        
        self.generate_report()

if __name__ == "__main__":
    analyzer = LogAnalyzer()
    
    # Run capture mode analysis
    print("Running log capture analysis...")
    analyzer.run_analysis(mode='capture', duration=30)
    
    # Optional: Run real-time monitoring
    # analyzer.run_analysis(mode='realtime', duration=60)

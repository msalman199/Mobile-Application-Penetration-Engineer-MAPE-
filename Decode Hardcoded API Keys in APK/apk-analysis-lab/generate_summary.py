#!/usr/bin/env python3
"""
Summary Report Generator for API Key Detection Results
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def generate_summary_report(json_file):
    """Generate a human-readable summary report"""
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    pattern_findings = data.get('pattern_findings', [])
    entropy_findings = data.get('entropy_findings', [])
    
    print("=" * 60)
    print("API KEY DETECTION SUMMARY REPORT")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Report file: {json_file}")
    print()
    
    # Executive Summary
    print("EXECUTIVE SUMMARY")
    print("-" * 20)
    total_findings = len(pattern_findings) + len(entropy_findings)
    high_risk = len([f for f in pattern_findings if f.get('confidence') == 'high'])
    medium_risk = len([f for f in pattern_findings if f.get('confidence') == 'medium'])
    
    print(f"Total potential secrets found: {total_findings}")
    print(f"High risk findings: {high_risk}")
    print(f"Medium risk findings: {medium_risk}")
    print(f"High entropy strings: {len(entropy_findings)}")
    print()
    
    # Risk Assessment
    if high_risk > 0:
        risk_level = "HIGH"
    elif medium_risk > 5:
        risk_level = "MEDIUM"
    elif total_findings > 0:
        risk_level = "LOW"
    else:
        risk_level = "MINIMAL"
    
    print(f"OVERALL RISK LEVEL: {risk_level}")
    print()
    
    # Detailed Findings
    if pattern_findings:
        print("DETAILED FINDINGS")
        print("-" * 20)
        
        # Group by pattern type
        by_pattern = {}
        for finding in pattern_findings:
            pattern = finding['pattern']
            if pattern not in by_pattern:
                by_pattern[pattern] = []
            by_pattern[pattern].append(finding)
        
        for pattern, findings in by_pattern.items():
            print(f"\n{pattern.upper().replace('_', ' ')} ({len(findings)} found)")
            print("  " + "-" * 40)
            
            for i, finding in enumerate(findings[:3], 1):  # Show top 3
                print(f"  {i}. File: {finding['file']}")
                print(f"     Line: {finding['line_number']}")
                print(f"     Confidence: {finding.get('confidence', 'unknown')}")
                if len(finding['match']) > 50:
                    print(f"     Value: {finding['match'][:50]}...")
                else:
                    print(f"     Value: {finding['match']}")
                print()
            
            if len(findings) > 3:
                print(f"     ... and {len(findings) - 3} more")
    
    # Recommendations
    print("\nRECOMMENDATIONS")
    print("-" * 20)
    
    if high_risk > 0:
        print("1. IMMEDIATE ACTION REQUIRED:")
        print("   - Review all high-confidence findings immediately")
        print("   - Rotate any confirmed API keys or secrets")
        print("   - Implement proper secret management")
    
    if medium_risk > 0:
        print("2. REVIEW MEDIUM RISK FINDINGS:")
        print("   - Manually verify medium-confidence findings")
        print("   - Remove any confirmed hardcoded secrets")
    
    if len(entropy_findings) > 0:
        print("3. INVESTIGATE HIGH ENTROPY STRINGS:")
        print("   - Review strings with high randomness")
        print("   - These may be encoded secrets or tokens")
    
    print("4. GENERAL SECURITY IMPROVEMENTS:")
    print("   - Use Android Keystore for sensitive data")
    print("   - Implement runtime secret retrieval")
    print("   - Use environment variables or secure configuration")
    print("   - Regular security code reviews")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generate_summary.py <json_report_file>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    if not Path(json_file).exists():
        print(f"Error: File {json_file} not found")
        sys.exit(1)
    
    generate_summary_report(json_file)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Plist Analyzer - Identifies sensitive data in plist files
Students: Complete the TODO sections to implement full functionality
"""

import plistlib
import re
import json
from pathlib import Path

def parse_plist_file(file_path):
    """
    Parse a plist file and return its contents.
    
    Args:
        file_path: Path to the plist file
    
    Returns:
        Dictionary containing plist data or None on error
    """
    # TODO: Open and parse the plist file using plistlib
    # TODO: Handle exceptions and return None on error
    # TODO: Return the parsed data
    pass

def identify_sensitive_keys(data, path="root"):
    """
    Recursively search for sensitive information in plist data.
    
    Args:
        data: Plist data (dict, list, or primitive)
        path: Current path in the data structure
    
    Returns:
        List of findings with type, path, key, value, and risk_level
    """
    sensitive_patterns = {
        'api_key': r'(?i)(api[_-]?key|apikey)',
        'password': r'(?i)(password|passwd|pwd)',
        'token': r'(?i)(token|auth|bearer)',
        'secret': r'(?i)(secret|private)',
        'credential': r'(?i)(credential|cred)',
        'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    }
    
    findings = []
    
    # TODO: Implement recursive search through dictionary
    # TODO: Check keys against sensitive_patterns
    # TODO: Check string values against patterns
    # TODO: Assign risk levels (HIGH for password/secret/api_key, MEDIUM for others)
    # TODO: Handle nested dictionaries and lists
    # TODO: Append findings with proper structure
    
    return findings

def generate_report(plist_data, findings, output_file):
    """
    Generate JSON report of analysis results.
    
    Args:
        plist_data: Original plist data
        findings: List of sensitive data findings
        output_file: Path to output JSON file
    
    Returns:
        Dictionary containing the complete report
    """
    # TODO: Create report structure with timestamp
    # TODO: Calculate risk summary (count HIGH, MEDIUM, LOW)
    # TODO: Include findings and raw data
    # TODO: Write to JSON file with proper formatting
    # TODO: Return the report dictionary
    pass

def main():
    """Main execution function"""
    plist_file = 'sample_app/Library/Preferences/com.example.app.plist'
    
    print("=== Plist Analysis Tool ===")
    
    # TODO: Parse the plist file
    # TODO: Identify sensitive information
    # TODO: Display findings organized by risk level
    # TODO: Generate and save report
    # TODO: Print summary statistics
    # TODO: Display security recommendations if HIGH risk found
    
    pass

if __name__ == "__main__":
    main()

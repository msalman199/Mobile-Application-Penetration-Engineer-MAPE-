#!/usr/bin/env python3

import subprocess
import sys
import time
from datetime import datetime

def run_content_provider_assessment():
    """Run content provider security assessment"""
    print("Starting Content Provider Assessment...")
    try:
        result = subprocess.run([sys.executable, 'content_provider_enumerator.py'], 
                              check=True)
        print("[+] Content provider assessment completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Content provider assessment failed: {e}")
        return False

def run_log_analysis():
    """Run log analysis"""
    print("Starting Log Analysis...")
    try:
        result = subprocess.run([sys.executable, 'log_analyzer.py'], 
                              check=True)
        print("[+] Log analysis completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Log analysis failed: {e}")
        return False

def main():
    print("="*70)
    print("COMPREHENSIVE ANDROID SECURITY ASSESSMENT")
    print("="*70)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check ADB connection
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        if 'device' not in result.stdout:
            print("[-] No Android device connected. Please connect a device and try again.")
            sys.exit(1)
    except FileNotFoundError:
        print("[-] ADB not found. Please ensure Android SDK is installed.")
        sys.exit(1)
    
    success_count = 0
    
    # Run assessments
    if run_content_provider_assessment():
        success_count += 1
    
    time.sleep(2)  # Brief pause between assessments
    
    if run_log_analysis():
        success_count += 1
    
    # Summary
    print("\n" + "="*70)
    print("ASSESSMENT COMPLETE")
    print("="*70)
    print(f"Completed assessments: {success_count}/2")
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if success_count == 2:
        print("[+] All assessments completed successfully")
        print("[*] Check the generated JSON reports for detailed findings")
    else:
        print("[-] Some assessments failed. Check the output above for details")

if __name__ == "__main__":
    main()

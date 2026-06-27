# 🛡️ Android Content Provider & Log Analysis 

<div align="center">

![Android](https://img.shields.io/badge/Android-SDK-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![ADB](https://img.shields.io/badge/ADB-Android%20Debug%20Bridge-0078D4?style=for-the-badge&logo=android&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Security](https://img.shields.io/badge/Security-Penetration%20Testing-FF0000?style=for-the-badge&logo=hackthebox&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-Reports-000000?style=for-the-badge&logo=json&logoColor=white)
![CMAPE](https://img.shields.io/badge/CMAPE-Certified-gold?style=for-the-badge&logo=acclaim&logoColor=white)

> **🏫 Platform:** Al Nafi Cloud Lab &nbsp;|&nbsp; **🎓 Cert:** Al Razzaq CMAPE &nbsp;|&nbsp; **⚡ Level:** Intermediate

</div>

---

## 📋 Table of Contents

| # | Section |
|---|---------|
| 1 | [🎯 Objectives](#-objectives) |
| 2 | [✅ Prerequisites](#-prerequisites) |
| 3 | [☁️ Lab Environment Setup](#️-lab-environment-setup) |
| 4 | [🔬 Task 1 — Access & Manipulate Content Providers](#-task-1--access--manipulate-content-providers) |
| 5 | [📋 Task 2 — Extract Data from Leaked Logs](#-task-2--extract-data-from-leaked-logs-using-adb) |
| 6 | [🐍 Task 3 — Python Automation Scripts](#-task-3--automate-with-python) |
| 7 | [🔧 Troubleshooting](#-troubleshooting) |
| 8 | [🛡️ Security Best Practices](#️-security-best-practices) |
| 9 | [🏁 Conclusion & Key Takeaways](#-conclusion--key-takeaways) |

---

## 🎯 Objectives

> By the end of this lab, students will be able to:

- 🔍 Understand Android **content provider architecture** and security implications
- ⚡ Access and manipulate content providers using **ADB commands**
- 🗂️ Extract sensitive data from **leaked log files** on Android devices
- 🐛 Identify common **content provider vulnerabilities** and misconfigurations
- 🤖 Automate enumeration and data extraction using **Python scripts**
- 📊 Analyze log files for **sensitive information disclosure**
- 🧪 Apply content provider security testing in **mobile app penetration testing**

---

## ✅ Prerequisites

> Before starting this lab, students should have:

| Requirement | Description |
|-------------|-------------|
| 🤖 **Android Architecture** | Basic understanding of Android application architecture |
| 💻 **Linux CLI** | Familiarity with Linux command line operations |
| ⚡ **ADB Knowledge** | Basic knowledge of Android Debug Bridge commands |
| 🗄️ **SQL Concepts** | Understanding of SQL database concepts |
| 🐍 **Python Basics** | Basic Python programming knowledge |
| 🔐 **Mobile Security** | Knowledge of mobile application security fundamentals |

---

## ☁️ Lab Environment Setup

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cloud%20Lab-blue?style=flat-square&logo=cloud&logoColor=white)
![No Setup](https://img.shields.io/badge/Setup-Zero%20Config%20Required-success?style=flat-square&logo=checkmarx&logoColor=white)

> 💡 **Al Nafi provides pre-configured Linux-based cloud machines.** Simply click **Start Lab** — no VM or extra software needed.

### 🧰 Pre-Installed Tools

| Tool | Purpose |
|------|---------|
| 🤖 Android SDK & ADB | Device communication & debugging |
| 🐍 Python 3.x + Libraries | Automation scripting |
| 📱 Android Emulator | Vulnerable app testing environment |
| 📝 Text Editors & Analysis Tools | Log analysis & code editing |
| 📦 Vulnerable APKs | Target applications for testing |

---

## 🔬 Task 1 — Access & Manipulate Content Providers

![ADB](https://img.shields.io/badge/Tool-ADB-0078D4?style=flat-square&logo=android&logoColor=white)
![Android](https://img.shields.io/badge/Platform-Android-3DDC84?style=flat-square&logo=android&logoColor=white)

### 📚 1.1 — Understanding Content Providers

> Content providers are Android components that manage access to structured data. They act as an interface between applications and their underlying data sources.

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| 🔗 **Content URI** | Unique identifier for content provider data |
| 🔄 **Content Resolver** | Client interface for accessing content providers |
| 🔒 **Permissions** | Access control mechanism for content providers |

---

### ⚙️ 1.2 — Setting Up the Android Environment

![ADB](https://img.shields.io/badge/ADB-Shell-0078D4?style=flat-square)
![Emulator](https://img.shields.io/badge/Android-Emulator-3DDC84?style=flat-square)

> 🚀 Start the Android emulator and prepare the testing environment.

```bash
# ▶️ Start the Android emulator
cd /opt/android-sdk/emulator
./emulator -avd TestDevice -no-snapshot-load &

# ⏳ Wait for the device to boot (about 2-3 minutes)
sleep 120

# ✅ Verify device connection
adb devices
```

> ⏱️ **Note:** The emulator takes approximately 2–3 minutes to fully boot. The `sleep 120` command waits automatically.

---

### 📦 1.3 — Installing Vulnerable Applications

![APK](https://img.shields.io/badge/APK-Install-3DDC84?style=flat-square&logo=android)
![Vuln App](https://img.shields.io/badge/App-Vulnerable-red?style=flat-square)

> 📲 Install the pre-built vulnerable applications for testing.

```bash
# 📂 Navigate to the applications directory
cd /home/student/lab-materials/vulnerable-apps

# 📥 Install the vulnerable content provider app
adb install VulnerableContentProvider.apk

# 📥 Install the data leakage app
adb install DataLeakageApp.apk

# ✅ Verify installations
adb shell pm list packages | grep -E "(vulnerable|leakage)"
```

---

### 🔍 1.4 — Discovering Content Providers

![dumpsys](https://img.shields.io/badge/ADB-dumpsys-0078D4?style=flat-square)
![Recon](https://img.shields.io/badge/Phase-Reconnaissance-orange?style=flat-square)

> 🗺️ Enumerate all available content providers on the device to map the attack surface.

```bash
# 📋 List all content providers
adb shell dumpsys package providers

# 🔎 Filter for our vulnerable app
adb shell dumpsys package providers | grep -A 10 -B 5 "vulnerable"

# ℹ️ Get detailed information about a specific provider
adb shell dumpsys package com.example.vulnerableapp
```

---

### 📊 1.5 — Querying Content Providers

![SQL](https://img.shields.io/badge/SQL-Query-003B57?style=flat-square&logo=sqlite)
![ADB Content](https://img.shields.io/badge/ADB-content%20query-0078D4?style=flat-square)

> 🗄️ Interact with discovered content providers and extract data.

```bash
# 🔍 Query the vulnerable content provider
adb shell content query --uri content://com.example.vulnerableapp.provider/users

# 📌 Query with specific columns
adb shell content query \
  --uri content://com.example.vulnerableapp.provider/users \
  --projection id,username,password

# 🔎 Query with WHERE clause
adb shell content query \
  --uri content://com.example.vulnerableapp.provider/users \
  --where "id=1"
```

---

### ➕ 1.6 — Inserting Data into Content Providers

![Write Access](https://img.shields.io/badge/Test-Write%20Access-red?style=flat-square)
![SQL INSERT](https://img.shields.io/badge/SQL-INSERT-003B57?style=flat-square)

> ⚠️ Test if unauthorized data can be inserted — a critical vulnerability indicator.

```bash
# 💉 Insert a new user record (unauthorized)
adb shell content insert \
  --uri content://com.example.vulnerableapp.provider/users \
  --bind username:s:hacker \
  --bind password:s:password123 \
  --bind email:s:hacker@example.com

# ✅ Verify the insertion was successful
adb shell content query --uri content://com.example.vulnerableapp.provider/users
```

> 🚨 **Security Alert:** If insertion succeeds without authentication errors, the content provider has **critical write-access misconfiguration**.

---

### ✏️ 1.7 — Updating and Deleting Data

![SQL UPDATE](https://img.shields.io/badge/SQL-UPDATE%20%2F%20DELETE-003B57?style=flat-square)
![Data Manipulation](https://img.shields.io/badge/Test-Data%20Manipulation-red?style=flat-square)

> 🛠️ Test modification capabilities — update and delete records without authorization.

```bash
# ✏️ Update an existing record
adb shell content update \
  --uri content://com.example.vulnerableapp.provider/users \
  --where "username='admin'" \
  --bind password:s:compromised

# 🗑️ Delete a record
adb shell content delete \
  --uri content://com.example.vulnerableapp.provider/users \
  --where "id=2"

# ✅ Verify changes took effect
adb shell content query --uri content://com.example.vulnerableapp.provider/users
```

---

## 📋 Task 2 — Extract Data from Leaked Logs Using ADB

![Logcat](https://img.shields.io/badge/Tool-ADB%20Logcat-0078D4?style=flat-square&logo=android)
![grep](https://img.shields.io/badge/Tool-grep%20%2F%20regex-E95420?style=flat-square&logo=linux)

### 📖 2.1 — Understanding Android Logging

> Android uses several logging mechanisms that can leak sensitive information:

| Log Type | Description |
|----------|-------------|
| 📢 **System logs** | General system messages |
| 📱 **Application logs** | App-specific debug information |
| 💥 **Crash logs** | Error and exception details |

---

### 📄 2.2 — Accessing System Logs

![Logcat](https://img.shields.io/badge/ADB-logcat-0078D4?style=flat-square)
![Priority](https://img.shields.io/badge/Filter-Priority%20Levels-orange?style=flat-square)

> 🔎 Examine system logs to hunt for sensitive data leakage.

```bash
# 👁️ View current system logs (live stream)
adb logcat

# ⚠️ Filter logs by priority level (Warning and above)
adb logcat *:W

# 🏷️ Filter logs by specific tag
adb logcat -s "VulnerableApp"

# 💾 Save all logs to file for offline analysis
adb logcat -d > /tmp/system_logs.txt
```

---

### ▶️ 2.3 — Generating Application Activity

![App Launch](https://img.shields.io/badge/ADB-am%20start-3DDC84?style=flat-square)
![Input](https://img.shields.io/badge/ADB-input%20keyevent-3DDC84?style=flat-square)

> 🎭 Trigger the vulnerable app to generate log entries containing sensitive data.

```bash
# 🚀 Launch the vulnerable app
adb shell am start -n com.example.vulnerableapp/.MainActivity

# 👤 Simulate user login — type username
adb shell input text "admin"

# ⌨️ Press Tab key (keyevent 61) to move to password field
adb shell input keyevent 61

# 🔑 Type the password
adb shell input text "password123"

# ↩️ Press Enter to submit login (keyevent 66)
adb shell input keyevent 66

# 📡 Trigger database sync via broadcast
adb shell am broadcast -a com.example.vulnerableapp.SYNC_DATA
```

---

### 🔬 2.4 — Analyzing Logs for Sensitive Data

![Bash](https://img.shields.io/badge/Script-Bash-4EAA25?style=flat-square&logo=gnubash)
![Pattern Match](https://img.shields.io/badge/Tool-Pattern%20Matching-E95420?style=flat-square)

> 📝 Create a shell script to scan logs for sensitive patterns automatically.

```bash
# 📝 Create the log analysis shell script
cat > /tmp/analyze_logs.sh << 'EOF'
#!/bin/bash

LOG_FILE="/tmp/system_logs.txt"
SENSITIVE_PATTERNS="/tmp/sensitive_patterns.txt"

# 📋 Define sensitive data patterns to search for
cat > $SENSITIVE_PATTERNS << 'PATTERNS'
password
credit.card
ssn
email
phone
token
api.key
secret
private.key
PATTERNS

echo "🔍 Analyzing logs for sensitive data..."
echo "=================================="

while read -r pattern; do
    echo "Searching for: $pattern"
    grep -i "$pattern" "$LOG_FILE" | head -5
    echo "---"
done < "$SENSITIVE_PATTERNS"
EOF

# ✅ Make executable and run
chmod +x /tmp/analyze_logs.sh
/tmp/analyze_logs.sh
```

---

### 🗄️ 2.5 — Extracting Database Logs

![SQL](https://img.shields.io/badge/SQL-Log%20Extraction-003B57?style=flat-square&logo=sqlite)
![grep](https://img.shields.io/badge/Tool-grep%20regex-4EAA25?style=flat-square)

> 📦 Hunt for database-related sensitive information in log output.

```bash
# 🗄️ Filter for SQL-related log entries
adb logcat -d | grep -i -E "(sql|database|query|insert|update|delete)" > /tmp/db_logs.txt

# 🔍 Search database logs for sensitive values
cat /tmp/db_logs.txt | grep -i -E "(password|user|admin|token)"

# 📡 Capture content provider operation logs
adb logcat -d | grep -i "content.*provider" > /tmp/provider_logs.txt
```

---

### 👁️ 2.6 — Monitoring Real-Time Log Leakage

![Real-time](https://img.shields.io/badge/Mode-Real--Time%20Monitor-FF4500?style=flat-square)
![Background](https://img.shields.io/badge/Process-Background%20Jobs-4EAA25?style=flat-square)

> ⚡ Set up parallel background monitors to catch secrets as they leak live.

```bash
# 🔑 Monitor logs in real-time for passwords
adb logcat | grep -i --line-buffered "password" &

# 💳 Monitor for credit card number patterns
adb logcat | grep -E --line-buffered \
  "[0-9]{4}[[:space:]-]?[0-9]{4}[[:space:]-]?[0-9]{4}[[:space:]-]?[0-9]{4}" &

# 📧 Monitor for email address patterns
adb logcat | grep -E --line-buffered \
  "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" &
```

> 💡 **Tip:** The `&` operator runs each monitor as a background job so all three run simultaneously in parallel.

---

## 🐍 Task 3 — Automate with Python

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Automation](https://img.shields.io/badge/Mode-Automation-blueviolet?style=for-the-badge)
![subprocess](https://img.shields.io/badge/Lib-subprocess-3776AB?style=flat-square)
![regex](https://img.shields.io/badge/Lib-re%20(regex)-3776AB?style=flat-square)
![json](https://img.shields.io/badge/Lib-json-3776AB?style=flat-square)

### ⚙️ 3.1 — Setting Up Python Environment

![pip3](https://img.shields.io/badge/Tool-pip3-3776AB?style=flat-square&logo=python)
![Setup](https://img.shields.io/badge/Phase-Environment%20Setup-success?style=flat-square)

> 🐍 Verify Python is available and prepare the working directory.

```bash
# 🔍 Check Python version
python3 --version

# 📦 Install required packages
pip3 install subprocess32 re json datetime

# 📁 Create and navigate to working directory
mkdir -p /home/student/content-provider-automation
cd /home/student/content-provider-automation
```

---

### 🤖 3.2 — Content Provider Enumeration Script

![Python Script](https://img.shields.io/badge/Script-content__provider__enumerator.py-3776AB?style=flat-square&logo=python)
![OOP](https://img.shields.io/badge/Pattern-OOP%20Class-blueviolet?style=flat-square)
![JSON Output](https://img.shields.io/badge/Output-JSON%20Report-000000?style=flat-square)

> 🔎 Save the following as `content_provider_enumerator.py`

```python
#!/usr/bin/env python3
# ============================================================
# 🔍 Content Provider Security Enumerator
# File:    content_provider_enumerator.py
# Purpose: Enumerate & test Android content providers via ADB
# Output:  content_provider_assessment_YYYYMMDD_HHMMSS.json
# ============================================================

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
        """✅ Check if Android device is connected via ADB"""
        try:
            result = subprocess.run(
                ['adb', 'devices'],
                capture_output=True, text=True
            )
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
        """🗺️ Enumerate all content providers on the device"""
        print("[*] Enumerating content providers...")
        try:
            result = subprocess.run(
                ['adb', 'shell', 'dumpsys', 'package', 'providers'],
                capture_output=True, text=True
            )
            # 🔎 Parse provider information using regex
            provider_pattern = r'Provider{[^}]+} (.+?):'
            authority_pattern = r'authority=([^,\s]+)'

            providers  = re.findall(provider_pattern, result.stdout)
            authorities = re.findall(authority_pattern, result.stdout)

            self.providers = list(zip(providers, authorities))
            print(f"[+] Found {len(self.providers)} content providers")
            return self.providers

        except Exception as e:
            print(f"[-] Error enumerating providers: {e}")
            return []

    def test_provider_access(self, authority):
        """🔓 Test accessibility of common URI paths for a provider"""
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
                result = subprocess.run(
                    ['adb', 'shell', 'content', 'query', '--uri', uri],
                    capture_output=True, text=True, timeout=10
                )
                if result.returncode == 0 and 'Row:' in result.stdout:
                    accessible_uris.append(uri)
                    print(f"[+] Accessible URI: {uri}")

            except subprocess.TimeoutExpired:
                print(f"[-] Timeout accessing: {uri}")
            except Exception as e:
                print(f"[-] Error accessing {uri}: {e}")

        return accessible_uris

    def extract_data(self, uri):
        """📦 Extract raw data from an accessible content provider URI"""
        try:
            result = subprocess.run(
                ['adb', 'shell', 'content', 'query', '--uri', uri],
                capture_output=True, text=True
            )
            return result.stdout if result.returncode == 0 else None
        except Exception as e:
            print(f"[-] Error extracting data from {uri}: {e}")
            return None

    def analyze_sensitive_data(self, data):
        """🔬 Scan extracted data for sensitive information using regex"""
        sensitive_patterns = {
            'password':    r'password[=:]\s*([^\s,]+)',
            'email':       r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'phone':       r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
            'token':       r'token[=:]\s*([a-zA-Z0-9]+)',
            'api_key':     r'api[_-]?key[=:]\s*([a-zA-Z0-9]+)'
        }
        findings = {}
        for pattern_name, pattern in sensitive_patterns.items():
            matches = re.findall(pattern, data, re.IGNORECASE)
            if matches:
                findings[pattern_name] = matches
                print(f"[!] Found {pattern_name}: {matches}")
        return findings

    def run_full_enumeration(self):
        """🚀 Run complete content provider enumeration and analysis"""
        print("=" * 60)
        print("Content Provider Security Assessment")
        print("=" * 60)

        if not self.check_device_connection():
            return

        providers = self.enumerate_providers()
        if not providers:
            print("[-] No content providers found")
            return

        for provider_name, authority in providers:
            print(f"\n[*] Testing provider: {provider_name}")
            print(f"[*] Authority: {authority}")

            accessible_uris = self.test_provider_access(authority)

            if accessible_uris:
                self.results[authority] = {
                    'provider_name':    provider_name,
                    'accessible_uris':  accessible_uris,
                    'extracted_data':   {},
                    'sensitive_findings': {}
                }
                for uri in accessible_uris:
                    data = self.extract_data(uri)
                    if data:
                        self.results[authority]['extracted_data'][uri] = data
                        sensitive = self.analyze_sensitive_data(data)
                        if sensitive:
                            self.results[authority]['sensitive_findings'][uri] = sensitive

        self.generate_report()

    def generate_report(self):
        """📊 Save findings to a timestamped JSON assessment report"""
        timestamp   = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"content_provider_assessment_{timestamp}.json"

        with open(report_file, 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"\n[+] Assessment complete. Report: {report_file}")
        print("\n" + "=" * 60)
        print("ASSESSMENT SUMMARY")
        print("=" * 60)

        total      = len(self.results)
        vulnerable = sum(1 for r in self.results.values() if r['sensitive_findings'])
        print(f"Total providers tested:  {total}")
        print(f"Vulnerable providers:    {vulnerable}")

        if vulnerable > 0:
            print("\n[!] SECURITY ISSUES FOUND:")
            for authority, data in self.results.items():
                if data['sensitive_findings']:
                    print(f"  - {authority}: {len(data['sensitive_findings'])} issues")


# ▶️ Entry point
if __name__ == "__main__":
    enumerator = ContentProviderEnumerator()
    enumerator.run_full_enumeration()
```

```bash
# 💾 Make executable and run
chmod +x content_provider_enumerator.py
python3 content_provider_enumerator.py
```

---

### 📊 3.3 — Log Analysis Automation Script

![Python Script](https://img.shields.io/badge/Script-log__analyzer.py-3776AB?style=flat-square&logo=python)
![regex](https://img.shields.io/badge/Lib-re%20(regex)-blueviolet?style=flat-square)
![Realtime](https://img.shields.io/badge/Mode-Capture%20%2F%20Real--Time-FF4500?style=flat-square)

> 📋 Save the following as `log_analyzer.py`

```python
#!/usr/bin/env python3
# ============================================================
# 📊 Android Log Security Analyzer
# File:    log_analyzer.py
# Purpose: Detect sensitive data leakage in Android logcat
# Output:  log_analysis_report_YYYYMMDD_HHMMSS.json
# ============================================================

import subprocess
import re
import json
import time
from datetime import datetime
from collections import defaultdict


class LogAnalyzer:
    def __init__(self):
        # 🔎 Sensitive data regex patterns organized by category
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
        """📥 Capture device logcat output for a set duration"""
        print(f"[*] Capturing logs for {duration} seconds...")
        try:
            subprocess.run(['adb', 'logcat', '-c'], check=True)  # clear buffer
            result = subprocess.run(
                ['adb', 'logcat', '-d'],
                capture_output=True, text=True,
                timeout=duration
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            print("[*] Log capture completed")
            return ""
        except Exception as e:
            print(f"[-] Error capturing logs: {e}")
            return ""

    def analyze_logs(self, log_data):
        """🔬 Analyze captured log text for sensitive information"""
        print("[*] Analyzing logs for sensitive data...")
        lines = log_data.split('\n')
        for line_num, line in enumerate(lines, 1):
            for category, patterns in self.sensitive_patterns.items():
                for pattern in patterns:
                    matches = re.findall(pattern, line, re.IGNORECASE)
                    if matches:
                        self.findings[category].append({
                            'line_number':  line_num,
                            'line_content': line.strip(),
                            'matches':      matches,
                            'timestamp':    self.extract_timestamp(line)
                        })

    def extract_timestamp(self, log_line):
        """🕐 Parse the timestamp from a logcat line"""
        pattern = r'(\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d{3})'
        match = re.search(pattern, log_line)
        return match.group(1) if match else "Unknown"

    def monitor_realtime(self, duration=60):
        """👁️ Stream logcat and analyze each line in real-time"""
        print(f"[*] Starting real-time monitoring for {duration} seconds...")
        try:
            process = subprocess.Popen(
                ['adb', 'logcat'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            start_time = time.time()
            while time.time() - start_time < duration:
                line = process.stdout.readline()
                if line:
                    self.analyze_single_line(line.strip())
            process.terminate()
        except Exception as e:
            print(f"[-] Error in real-time monitoring: {e}")

    def analyze_single_line(self, line):
        """⚡ Check a single log line and alert immediately on matches"""
        for category, patterns in self.sensitive_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                if matches:
                    print(f"[!] REAL-TIME ALERT — {category}: {matches}")
                    self.findings[category].append({
                        'line_content': line,
                        'matches':      matches,
                        'timestamp':    self.extract_timestamp(line),
                        'real_time':    True
                    })

    def generate_report(self):
        """📊 Write all findings to a timestamped JSON report"""
        timestamp   = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"log_analysis_report_{timestamp}.json"

        report_data = {
            'analysis_timestamp':   timestamp,
            'total_findings':       sum(len(v) for v in self.findings.values()),
            'findings_by_category': dict(self.findings)
        }
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)

        print(f"\n[+] Report saved to: {report_file}")
        self.print_summary()

    def print_summary(self):
        """📋 Print a human-readable findings summary to stdout"""
        print("\n" + "=" * 60)
        print("LOG ANALYSIS SUMMARY")
        print("=" * 60)

        if not self.findings:
            print("[+] No sensitive data found in logs")
            return

        for category, findings in self.findings.items():
            if findings:
                print(f"\n[!] {category.upper()}: {len(findings)} instances found")
                for finding in findings[:3]:
                    print(f"    - {finding['matches']}")
                if len(findings) > 3:
                    print(f"    ... and {len(findings) - 3} more")

    def run_analysis(self, mode='capture', duration=30):
        """🚀 Run log analysis in capture or real-time mode"""
        print("=" * 60)
        print("Android Log Security Analysis")
        print("=" * 60)

        if mode == 'capture':
            log_data = self.capture_logs(duration)
            if log_data:
                self.analyze_logs(log_data)
        elif mode == 'realtime':
            self.monitor_realtime(duration)

        self.generate_report()


# ▶️ Entry point
if __name__ == "__main__":
    analyzer = LogAnalyzer()

    # 📥 Default: capture mode
    print("Running log capture analysis...")
    analyzer.run_analysis(mode='capture', duration=30)

    # 👁️ Uncomment below for real-time streaming mode instead:
    # analyzer.run_analysis(mode='realtime', duration=60)
```

```bash
# 💾 Make executable and run
chmod +x log_analyzer.py
python3 log_analyzer.py
```

---

### ▶️ 3.4 — Running the Automation Scripts

![Execute](https://img.shields.io/badge/Action-Execute%20Scripts-success?style=flat-square)
![JSON](https://img.shields.io/badge/Output-JSON%20Reports-000000?style=flat-square)

```bash
# 🔍 Run content provider enumeration
python3 content_provider_enumerator.py

# 📊 Run log analysis
python3 log_analyzer.py

# 📁 List all generated JSON reports
ls -la *.json
```

---

### 🧩 3.5 — Combined Assessment Script (Master Orchestrator)

![Python Script](https://img.shields.io/badge/Script-combined__assessment.py-3776AB?style=flat-square&logo=python)
![Orchestration](https://img.shields.io/badge/Pattern-Orchestration-blueviolet?style=flat-square)
![Master](https://img.shields.io/badge/Type-Master%20Script-gold?style=flat-square)

> 🎯 Save the following as `combined_assessment.py`

```python
#!/usr/bin/env python3
# ============================================================
# 🧩 Combined Android Security Assessment — Master Script
# File:    combined_assessment.py
# Purpose: Orchestrate full security audit with one command
# ============================================================

import subprocess
import sys
import time
from datetime import datetime


def run_content_provider_assessment():
    """🔍 Phase 1 — Run content provider security assessment"""
    print("\n[*] ── Phase 1: Content Provider Assessment ──")
    try:
        subprocess.run(
            [sys.executable, 'content_provider_enumerator.py'],
            check=True
        )
        print("[+] Content provider assessment completed ✅")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Content provider assessment failed: {e}")
        return False


def run_log_analysis():
    """📊 Phase 2 — Run log leakage analysis"""
    print("\n[*] ── Phase 2: Log Analysis ──")
    try:
        subprocess.run(
            [sys.executable, 'log_analyzer.py'],
            check=True
        )
        print("[+] Log analysis completed ✅")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Log analysis failed: {e}")
        return False


def main():
    print("=" * 70)
    print("  🛡️  COMPREHENSIVE ANDROID SECURITY ASSESSMENT")
    print("=" * 70)
    print(f"  ⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # ✅ Step 1: Verify ADB connectivity
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        if 'device' not in result.stdout:
            print("[-] No Android device connected. Please connect a device.")
            sys.exit(1)
        print("[+] ADB device connection verified ✅")
    except FileNotFoundError:
        print("[-] ADB not found. Ensure Android SDK is installed and in PATH.")
        sys.exit(1)

    success_count = 0

    # 🔍 Phase 1: Content Provider Assessment
    if run_content_provider_assessment():
        success_count += 1

    time.sleep(2)  # brief pause between phases

    # 📊 Phase 2: Log Analysis
    if run_log_analysis():
        success_count += 1

    # 📋 Final unified summary
    print("\n" + "=" * 70)
    print("  📋  ASSESSMENT COMPLETE")
    print("=" * 70)
    print(f"  ✅ Completed: {success_count}/2 assessments")
    print(f"  ⏰ Finished:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if success_count == 2:
        print("  🎉 All assessments completed successfully!")
        print("  📁 Review the generated JSON reports for detailed findings.")
    else:
        print("  ⚠️  Some assessments failed. Check the output above.")

    print("=" * 70)


# ▶️ Entry point
if __name__ == "__main__":
    main()
```

```bash
# 💾 Make executable and run the full audit
chmod +x combined_assessment.py
python3 combined_assessment.py
```

---

### 📁 3.6 — Reviewing Assessment Reports

![Reports](https://img.shields.io/badge/Output-JSON%20Reports-000000?style=flat-square)
![Analysis](https://img.shields.io/badge/Phase-Post%20Analysis-blueviolet?style=flat-square)

```bash
# 📁 List all generated report files
ls -la *report*.json
ls -la *assessment*.json

# 🔍 Check content provider sensitive findings
echo "=== Content Provider Findings ==="
cat content_provider_assessment_*.json | grep -A 5 "sensitive_findings"

# 📊 Check log analysis category findings
echo "=== Log Analysis Findings ==="
cat log_analysis_report_*.json | grep -A 10 "findings_by_category"
```

---

## 🔧 Troubleshooting

### ❌ Device Connection Issues

![ADB Fix](https://img.shields.io/badge/Fix-ADB%20Restart-red?style=flat-square)

```bash
# 🔄 Restart the ADB server
adb kill-server
adb start-server
adb devices

# 🔍 Check whether the emulator process is running
ps aux | grep emulator

# 🔁 Kill and restart the emulator if needed
pkill -f emulator
cd /opt/android-sdk/emulator
./emulator -avd TestDevice -no-snapshot-load &
```

---

### 🔒 Permission Denied Errors

![Permissions](https://img.shields.io/badge/Fix-chmod%20%2F%20sudo-E95420?style=flat-square&logo=linux)

```bash
# 🔓 Fix USB device permissions
sudo chmod 666 /dev/bus/usb/*/*

# 🔄 Or restart ADB with root privileges
sudo adb kill-server
sudo adb start-server
```

---

### 🐍 Script Execution Issues

![Python Fix](https://img.shields.io/badge/Fix-Python%20%2F%20pip3-3776AB?style=flat-square&logo=python)

```bash
# ✅ Ensure all Python scripts are executable
chmod +x *.py

# 🔍 Verify Python installation path
which python3

# 📦 Install any missing dependencies
pip3 install --user subprocess32 re json datetime
```

---

## 🛡️ Security Best Practices

### 👨‍💻 For Developers

| Practice | Details |
|----------|---------|
| 🔒 **Permissions** | Apply proper permissions to every content provider |
| ✅ **Input Validation** | Validate all data received by content providers |
| 🛡️ **Parameterized Queries** | Use parameterized queries to prevent SQL injection |
| 🚫 **No Sensitive Logging** | Never log passwords, tokens, PII, or credentials |
| 🔐 **Access Controls** | Implement strict access controls on all data endpoints |

### 🕵️ For Security Testers

| Practice | Details |
|----------|---------|
| 📄 **Authorization** | Always obtain written authorization before testing |
| 📋 **Documentation** | Document all findings thoroughly with evidence |
| ✅ **Manual Verification** | Manually verify every automated finding |
| 💼 **Business Impact** | Assess and communicate the business impact of each vulnerability |
| 📢 **Responsible Disclosure** | Follow responsible disclosure timelines and practices |

---

## 🏁 Conclusion & Key Takeaways

> ✅ In this lab you have successfully learned how to:

- ⚡ Interact with Android content providers using **ADB commands** — query, insert, update, and delete
- 🗂️ Extract and analyze sensitive data from **Android log files** with filtering techniques
- 🤖 Automate security assessments using **Python scripts** for enumeration and log analysis
- 🐛 Identify common **security vulnerabilities** in Android apps related to data exposure
- 📊 Generate comprehensive **JSON reports** documenting all security findings

### 💡 Key Takeaways

| # | Takeaway |
|---|----------|
| 1 | 🔓 Content providers expose sensitive data when not secured with proper permissions |
| 2 | 📋 Android logs frequently leak credentials, tokens, and PII that must never be logged |
| 3 | 🤖 Python automation greatly improves speed and coverage of security assessments |
| 4 | 📊 Proper documentation and reporting are crucial for actionable security testing |
| 5 | 🔄 The tools built here are reusable and adaptable across any Android environment |

---

<div align="center">

### 🎓 Certification

This lab directly supports the:

![CMAPE](https://img.shields.io/badge/Al%20Razzaq-CMAPE%20Certification-gold?style=for-the-badge&logo=acclaim&logoColor=white)

**Al Razzaq Certified Mobile Application Penetration Engineer**

---

![Android](https://img.shields.io/badge/Android-SDK-3DDC84?style=flat-square&logo=android&logoColor=white)
![ADB](https://img.shields.io/badge/ADB-Tool-0078D4?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite)
![Security](https://img.shields.io/badge/Security-PenTest-FF0000?style=flat-square)
![JSON](https://img.shields.io/badge/Output-JSON-000000?style=flat-square)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=flat-square&logo=gnubash)

*Happy Hacking — Stay Ethical! 🛡️*

</div>

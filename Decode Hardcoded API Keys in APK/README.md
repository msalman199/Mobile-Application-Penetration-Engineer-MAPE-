# 🔐 Decode Hardcoded API Keys in APK

<div align="center">

# 📱 Android APK Secret Discovery Lab

### Decode Hardcoded API Keys • Tokens • Secrets • Credentials

---

![Android](https://img.shields.io/badge/Android-APK-3DDC84?style=for-the-badge\&logo=android)
![APKTool](https://img.shields.io/badge/APKTool-Decompiler-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge\&logo=python)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-FCC624?style=for-the-badge\&logo=linux)
![Regex](https://img.shields.io/badge/Regex-Pattern%20Matching-purple?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Reports-lightgrey?style=for-the-badge)
![Security](https://img.shields.io/badge/Mobile-Security-red?style=for-the-badge)
![Static Analysis](https://img.shields.io/badge/Static-Analysis-orange?style=for-the-badge)
![OWASP](https://img.shields.io/badge/OWASP-Mobile-green?style=for-the-badge)

---

## 🔎 Mobile Application Security Assessment Lab

**Learn how to discover hardcoded API keys, tokens, secrets, and sensitive credentials inside Android APK applications using APKTool and Python automation.**

</div>

---

# 📚 Table of Contents

* 📖 Overview
* 🎯 Objectives
* 🛠 Technologies Used
* 📋 Prerequisites
* 💻 Lab Environment
* 📂 Workspace Structure
* 🚀 Task 1 – Extract APK Resources Using APKTool
* 🔍 Task 2 – Locate Hardcoded API Keys
* 🤖 Task 3 – Automate API Key Detection
* 📊 Expected Results
* 🛠 Troubleshooting
* 🎓 Conclusion

---

# 📖 Overview

Hardcoded credentials remain one of the most common security weaknesses in Android applications.

Developers sometimes embed:

* 🔑 API Keys
* 🔐 Secret Keys
* 🎫 Access Tokens
* 🌐 Firebase Keys
* ☁ AWS Credentials
* 📧 Email Credentials
* 🔒 Passwords
* 🎟 Bearer Tokens

inside the application source code.

Once an APK is distributed, these secrets can often be recovered through reverse engineering.

In this lab you will learn how professional mobile security analysts locate sensitive information using static analysis techniques and Python automation.

---

# 🎯 Learning Objectives

By the end of this lab, you will be able to:

* ✅ Extract Android APK files using APKTool
* ✅ Navigate decompiled APK directory structures
* ✅ Analyze AndroidManifest.xml
* ✅ Search Smali bytecode
* ✅ Inspect XML resources
* ✅ Locate hardcoded API keys
* ✅ Detect access tokens
* ✅ Identify secret credentials
* ✅ Build automated Python detection tools
* ✅ Apply regex for pattern matching
* ✅ Generate professional analysis reports

---

# 🛠 Technologies Used

| Technology             | Purpose                   |
| ---------------------- | ------------------------- |
| 📱 Android APK         | Target Application        |
| 🔨 APKTool             | APK Decompilation         |
| 🐍 Python 3            | Automation                |
| 🐧 Ubuntu Linux        | Operating System          |
| 🔍 Regular Expressions | Pattern Matching          |
| 📄 JSON                | Report Generation         |
| 💻 Linux Terminal      | Static Analysis           |
| 📂 Smali               | Android Bytecode          |
| 📜 XML                 | Resources & Configuration |

---

# 📋 Prerequisites

Before beginning this lab you should understand:

* ✅ Android application architecture
* ✅ Linux command-line operations
* ✅ Basic Python programming
* ✅ Regular Expressions (Regex)
* ✅ API authentication concepts
* ✅ File system navigation

---

# 💻 Lab Environment

This lab is performed on the **Al Nafi Cloud Machine**.

### Environment Configuration

| Component        | Version      |
| ---------------- | ------------ |
| Operating System | Ubuntu Linux |
| APKTool          | Installed    |
| Python           | Python 3     |
| Text Editors     | Installed    |
| File Browser     | Installed    |
| Sample APK       | Included     |

Everything required for the exercise is already installed.

---

# 📂 Workspace Structure

```text
apk-analysis-lab/
│
├── extracted-apks/
│      └── sample-app/
│
├── scripts/
│      ├── api_key_detector.py
│      ├── enhanced_api_detector.py
│      └── generate_summary.py
│
└── results/
       ├── api_key_report.json
       ├── enhanced_report.json
       └── lab_summary.txt
```

---

# 🚀 Task 1 — Extract APK Resources Using APKTool

---

# 📌 Subtask 1.1 — Prepare the Lab Environment

## 🎯 Objective

Create an organized workspace and verify that all required tools are available.

---

## 📁 Create the Workspace

```bash
mkdir -p ~/apk-analysis-lab

cd ~/apk-analysis-lab
```

---

## 🔍 Verify APKTool Installation

```bash
apktool --version
```

Expected Output

```text
2.x.x
```

---

## 📂 Create Working Directories

```bash
mkdir -p extracted-apks

mkdir -p scripts

mkdir -p results
```

---

## ✅ Expected Directory Layout

```text
apk-analysis-lab/
├── extracted-apks/
├── scripts/
└── results/
```

---

## 💡 Why This Step?

A structured workspace keeps:

* Decompiled APKs
* Python scripts
* Analysis reports

organized throughout the assessment.

---

# 📌 Subtask 1.2 — Download the Sample APK

## 🎯 Objective

Download a vulnerable Android application for analysis.

---

## 📥 Download the APK

```bash
wget -O sample-app.apk \
"https://github.com/OWASP/owasp-mstg/raw/master/Crackmes/Android/Level_01/UnCrackable-Level1.apk"
```

---

## 📄 Verify Download

```bash
ls -la sample-app.apk
```

Example

```text
-rw-r--r-- user user 3.4M sample-app.apk
```

---

## 🔍 Verify File Type

```bash
file sample-app.apk
```

Example

```text
sample-app.apk: Zip archive data
```

---

## 💡 Why Verify?

APK files are ZIP archives containing:

* AndroidManifest.xml
* classes.dex
* resources.arsc
* assets
* native libraries

---

# 📌 Subtask 1.3 — Extract the APK

## 🎯 Objective

Use APKTool to extract all APK resources.

---

## 🔨 Decompile the APK

```bash
apktool d sample-app.apk -o extracted-apks/sample-app
```

---

## 📂 Navigate into the Decompiled APK

```bash
cd extracted-apks/sample-app
```

---

## 📁 Display Directory Contents

```bash
ls -la
```

Example

```text
AndroidManifest.xml
apktool.yml
assets
res
smali
original
unknown
```

---

## 💡 APKTool Output

APKTool extracts:

* Manifest
* Resources
* Assets
* Smali Code
* Native Libraries
* Configuration Files

---

# 📌 Subtask 1.4 — Explore the APK Structure

## 🎯 Objective

Understand where sensitive information is commonly stored.

---

## 🌳 Display Directory Tree

```bash
tree -L 3
```

Example

```text
sample-app/
├── AndroidManifest.xml
├── assets/
├── res/
├── smali/
├── original/
└── unknown/
```

---

## 📄 View Android Manifest

```bash
echo "=== APK Manifest ==="

head -20 AndroidManifest.xml
```

---

## 📂 Examine Resources

```bash
echo "=== Resources Directory ==="

ls -la res/
```

---

## 📦 Examine Assets

```bash
echo "=== Assets Directory ==="

ls -la assets/ 2>/dev/null || echo "No assets directory found"
```

---

## 💻 Examine Smali Code

```bash
echo "=== Smali Code Directory ==="

ls -la smali/
```

---

# 📖 Understanding the Decompiled APK

| Directory           | Description                |
| ------------------- | -------------------------- |
| AndroidManifest.xml | Application configuration  |
| res                 | XML resources              |
| assets              | Application assets         |
| smali               | Decompiled Dalvik bytecode |
| original            | Original metadata          |
| unknown             | Unknown resources          |

---

# 🔎 Common Locations for Hardcoded Secrets

During reverse engineering, sensitive data is frequently found inside:

### 📄 XML Resources

```
res/values/
```

---

### 💻 Smali Bytecode

```
smali/
```

---

### 📦 Assets

```
assets/
```

---

### ⚙ Configuration Files

```
.properties
.config
.json
.cfg
.ini
```

---

### 🌐 JavaScript Files

```
.js
```

---

### 📜 Android Manifest

```
AndroidManifest.xml
```

---

# 🛡 Security Assessment Checklist

Before moving to the next task, confirm:

* ✅ APK downloaded
* ✅ APKTool installed
* ✅ APK successfully decompiled
* ✅ Manifest reviewed
* ✅ Resource folders explored
* ✅ Smali directory located
* ✅ Assets inspected

---

# 🎉 Task 1 Complete

Congratulations!

You have successfully:

* 📦 Downloaded a sample APK
* 🔨 Decompiled the application using APKTool
* 📂 Explored the internal APK structure
* 📄 Examined Android resources
* 💻 Located Smali bytecode
* 🔍 Identified common locations where secrets may exist

---

# ➡️ Next: Part 2

In **Part 2**, you will learn how to:

* 🔍 Search for hardcoded API keys
* 🔑 Locate access tokens
* 🔐 Find secret credentials
* 📄 Analyze XML resources
* 💻 Inspect Smali bytecode
* ⚙ Review configuration files
* 🚨 Identify sensitive information manually before automating detection
---

# 🔍 Task 2 — Locate Hardcoded API Keys in the Decompiled APK

---

# 📌 Subtask 2.1 — Search for Common API Key Patterns

## 🎯 Objective

Perform a systematic search through the decompiled APK to identify hardcoded API keys, authentication tokens, and other sensitive credentials.

Rather than reviewing every file manually, we'll use Linux command-line tools to quickly identify suspicious strings.

---

## 📂 Navigate to the Decompiled APK

```bash
cd ~/apk-analysis-lab/extracted-apks/sample-app
```

---

## 🔑 Search for API Keys

```bash
echo "=== Searching for API Keys ==="

grep -r -i "api[_-]key" . \
--include="*.xml" \
--include="*.smali" \
--include="*.txt"
```

---

### 📖 What This Search Looks For

Common variable names such as:

* api_key
* api-key
* apikey
* API_KEY

---

## 🎟 Search for Access Tokens

```bash
echo "=== Searching for Access Tokens ==="

grep -r -i "access[_-]token" . \
--include="*.xml" \
--include="*.smali" \
--include="*.txt"
```

---

## 🔐 Search for Secret Keys

```bash
echo "=== Searching for Secret Keys ==="

grep -r -i "secret[_-]key" . \
--include="*.xml" \
--include="*.smali" \
--include="*.txt"
```

---

## 🪪 Search for Bearer Tokens

```bash
echo "=== Searching for Bearer Tokens ==="

grep -r -i "bearer" . \
--include="*.xml" \
--include="*.smali" \
--include="*.txt"
```

---

## 🚨 Typical Findings

During mobile application assessments, analysts often discover:

* Google API Keys
* Firebase Tokens
* AWS Credentials
* OAuth Tokens
* Bearer Tokens
* JWT Tokens
* Database Credentials
* Third-party Service Keys

---

# 📌 Subtask 2.2 — Analyze XML String Resources

## 🎯 Objective

Android developers frequently store configuration values inside XML resource files.

---

## 📄 Locate String Resource Files

```bash
find . -name "strings.xml" -type f
```

Example

```text
./res/values/strings.xml
./res/values-en/strings.xml
```

---

## 🔍 Search for Sensitive Strings

```bash
echo "=== Analyzing String Resources ==="

for strings_file in $(find . -name "strings.xml" -type f); do
    echo "File: $strings_file"

    cat "$strings_file" | grep -E "(key|token|secret|password|api)" -i

    echo "---"
done
```

---

## 📄 Example Finding

```xml
<string name="google_api_key">
AIzaSyDemoXXXXXXXXXXXXXXXXXXXXXXXXXXXX
</string>
```

---

## 🚩 Red Flags

Pay close attention to values containing:

* api
* token
* key
* password
* bearer
* client_secret
* access_token

---

# 📌 Subtask 2.3 — Inspect Smali Bytecode

## 🎯 Objective

Many developers hardcode sensitive values directly into compiled bytecode.

APKTool converts this bytecode into **Smali**, making it searchable.

---

## 🔎 Locate Smali Files with String Constants

```bash
echo "=== Searching Smali Files ==="

find . -name "*.smali" \
-exec grep -l "const-string" {} \; | head -10
```

---

## 🔍 Search for Base64 Encoded Strings

```bash
echo "=== Searching for Base64 Strings ==="

grep -r \
"const-string.*[A-Za-z0-9+/=]\{20,\}" \
. --include="*.smali" | head -5
```

---

## 🔍 Search for Long Alphanumeric Strings

```bash
echo "=== Searching for Long Strings ==="

grep -r \
"const-string.*[A-Za-z0-9]\{32,\}" \
. --include="*.smali" | head -5
```

---

## 📄 Example Smali Code

```smali
const-string v0, "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

---

## 💡 Why Smali Matters

Even if Java source code is unavailable, hardcoded values frequently remain visible inside:

* const-string instructions
* Static fields
* Method parameters
* Resource references

---

# 📌 Subtask 2.4 — Inspect Configuration Files

## 🎯 Objective

Configuration files often contain secrets that developers accidentally package into production applications.

---

## 🔎 Search for Configuration Files

```bash
echo "=== Looking for Configuration Files ==="

find . \
-name "*.properties" \
-o -name "*.config" \
-o -name "*.cfg" \
-o -name "*.ini"
```

---

## 📄 Search for JSON Configuration Files

```bash
find . -name "*.json" -type f
```

---

## 📖 Display Configuration Files

```bash
for config_file in $(find . \
-name "*.properties" \
-o -name "*.config" \
-o -name "*.json" 2>/dev/null); do

    if [ -f "$config_file" ]; then

        echo "=== Configuration File: $config_file ==="

        cat "$config_file"

        echo "---"

    fi

done
```

---

## 🚨 Common Secrets Found

Configuration files frequently contain:

* Database passwords
* Firebase configuration
* API endpoints
* AWS credentials
* Client secrets
* OAuth settings

---

# 🔍 Manual Secret Hunting Checklist

Before automation, verify the following manually.

| Item                | Checked |
| ------------------- | ------- |
| API Keys            | ✅       |
| Secret Keys         | ✅       |
| Passwords           | ✅       |
| Bearer Tokens       | ✅       |
| JWT Tokens          | ✅       |
| OAuth Credentials   | ✅       |
| Firebase Keys       | ✅       |
| AWS Keys            | ✅       |
| Base64 Strings      | ✅       |
| Long Random Strings | ✅       |

---

# 🔐 Common API Key Formats

## Google API Key

```text
AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## AWS Access Key

```text
AKIAIOSFODNN7EXAMPLE
```

---

## GitHub Token

```text
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Slack Token

```text
xoxb-1234567890-abcdefghijklmnopqrstuv
```

---

## Stripe Secret Key

```text
sk_live_xxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Firebase Token

```text
AAAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## JWT Token

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

# 🚨 Security Risks

Hardcoded secrets can lead to:

* 🔴 API abuse
* 🔴 Unauthorized cloud access
* 🔴 Database compromise
* 🔴 Account takeover
* 🔴 Financial loss
* 🔴 Data leakage

---

# 💡 Best Practices

Instead of hardcoding secrets:

* ✅ Use Android Keystore
* ✅ Retrieve secrets securely from a backend
* ✅ Rotate credentials regularly
* ✅ Encrypt sensitive configuration
* ✅ Remove debug credentials before release

---

# 🎉 Task 2 Completed

Excellent work!

You have successfully learned how to:

* 🔍 Search XML resources
* 💻 Analyze Smali bytecode
* 📄 Inspect configuration files
* 🔐 Detect API keys manually
* 🎟 Identify access tokens
* 🔑 Locate secret credentials
* 🚨 Recognize common hardcoded secret patterns

---

# 🤖 Next: Part 3

In **Part 3**, you'll build automated detection tools using Python, including:

* 🐍 `api_key_detector.py`
* 🚀 `enhanced_api_detector.py`
* 📊 `generate_summary.py`

These scripts will automate API key detection, perform entropy analysis, generate JSON reports, and create professional security assessment summaries.


---

# ✅ Verification and Testing

After completing the lab, verify that all components were created successfully and that your analysis environment is functioning correctly.

---

# 📌 Step 4.1 — Verify the Decompiled APK

Return to the lab workspace.

```bash
cd ~/apk-analysis-lab
```

Verify the extracted APK structure.

```bash
echo "=== Checking Decompiled APK ==="

ls -la extracted-apks/sample-app/
```

Expected directories include:

```text
AndroidManifest.xml
apktool.yml
assets/
res/
smali/
original/
unknown/
```

---

# 📌 Step 4.2 — Verify Python Scripts

Ensure all automation scripts were created successfully.

```bash
echo "=== Checking Scripts ==="

ls -la scripts/
```

Expected Output

```text
api_key_detector.py
enhanced_api_detector.py
generate_summary.py
```

---

# 📌 Step 4.3 — Verify Generated Reports

Display all generated reports.

```bash
echo "=== Checking Results ==="

ls -la results/
```

Expected Output

```text
api_key_report_sample-app.json
enhanced_report_sample-app.json
lab_summary.txt
```

---

# 📌 Step 4.4 — Test Python Environment

Verify Python can execute correctly.

```bash
cd scripts

python3 -c "
import sys
print('Python environment is working correctly.')
"
```

Expected Output

```text
Python environment is working correctly.
```

---

# 📌 Step 4.5 — Generate a Lab Summary

Create a simple summary of the completed lab.

```bash
echo "=== Lab Completion Summary ===" > ../results/lab_summary.txt

echo "Date: $(date)" >> ../results/lab_summary.txt

echo "APK Analyzed: sample-app.apk" >> ../results/lab_summary.txt

echo "Scripts Created: 3" >> ../results/lab_summary.txt

echo "JSON Reports Generated: $(ls ../results/*.json 2>/dev/null | wc -l)" >> ../results/lab_summary.txt

cat ../results/lab_summary.txt
```

Example Output

```text
=== Lab Completion Summary ===
Date: Mon Jun 27 15:20:12 UTC
APK Analyzed: sample-app.apk
Scripts Created: 3
JSON Reports Generated: 2
```

---

# 📊 Expected Results

After completing this lab, you should have successfully:

---

## 📦 Decompiled the APK

Using APKTool, you extracted:

* ✅ AndroidManifest.xml
* ✅ Smali bytecode
* ✅ Resources
* ✅ Assets
* ✅ Configuration files

---

## 🔍 Performed Manual Secret Discovery

You searched for:

* API Keys
* Secret Keys
* Access Tokens
* JWT Tokens
* Bearer Tokens
* OAuth Credentials
* Firebase Keys
* AWS Credentials

---

## 🤖 Automated Secret Detection

Your Python scripts automatically identified:

* Hardcoded API Keys
* Authentication Tokens
* Long Random Strings
* Base64 Encoded Secrets
* JWT Tokens
* High-Entropy Strings
* Cloud Credentials

---

## 📄 Generated Reports

The automation produced:

* 📑 JSON detection reports
* 📋 Summary reports
* 📊 Security assessment output

---

# 🚨 Example Security Findings

Typical findings during APK analysis include:

| Finding                      | Severity  |
| ---------------------------- | --------- |
| Google API Key               | 🔴 High   |
| Firebase API Key             | 🔴 High   |
| AWS Access Key               | 🔴 High   |
| GitHub Personal Access Token | 🔴 High   |
| Slack Token                  | 🔴 High   |
| JWT Token                    | 🟠 Medium |
| Base64 Encoded Secret        | 🟠 Medium |
| Hardcoded Password           | 🔴 High   |

---

# 📂 Example Results Directory

```text
results/
├── api_key_report_sample-app.json
├── enhanced_report_sample-app.json
├── lab_summary.txt
```

---

# 🛡 Security Assessment Checklist

Use this checklist whenever reviewing Android applications.

| Assessment                   | Status |
| ---------------------------- | ------ |
| APK Decompiled               | ✅      |
| Manifest Reviewed            | ✅      |
| Resources Reviewed           | ✅      |
| Smali Analyzed               | ✅      |
| XML Resources Inspected      | ✅      |
| Configuration Files Reviewed | ✅      |
| API Keys Searched            | ✅      |
| Tokens Identified            | ✅      |
| Python Automation Executed   | ✅      |
| Reports Generated            | ✅      |

---

# ⚠️ Troubleshooting Guide

---

## ❌ APKTool Not Found

### Error

```text
apktool: command not found
```

### Solution

```bash
sudo apt update

sudo apt install apktool -y
```

---

## ❌ Permission Denied

### Error

```text
Permission denied
```

### Solution

```bash
chmod +x scripts/*.py

chmod -R 755 ~/apk-analysis-lab
```

---

## ❌ Python Module Errors

### Error

```text
ModuleNotFoundError
```

### Solution

Most required libraries are included with Python.

If additional packages are required:

```bash
pip3 install pathlib
```

---

## ❌ No Findings Detected

Some APKs intentionally hide secrets using:

* Encryption
* Obfuscation
* Runtime retrieval
* Native libraries

For testing purposes, create a sample XML file.

```bash
cat > extracted-apks/sample-app/test_secrets.xml << 'EOF'
<?xml version="1.0" encoding="utf-8"?>
<resources>

<string name="google_api_key">
AIzaSyDemoKey1234567890abcdefghijklmnop
</string>

<string name="aws_access_key">
AKIAIOSFODNN7EXAMPLE
</string>

<string name="stripe_secret">
sk_live_abcdef1234567890abcdef12
</string>

</resources>
EOF
```

Re-run the scanner.

```bash
cd scripts

python3 enhanced_api_detector.py ../extracted-apks/sample-app
```

---

## ❌ Report Not Generated

Verify the results directory exists.

```bash
mkdir -p ~/apk-analysis-lab/results
```

Check permissions.

```bash
chmod 755 ~/apk-analysis-lab/results
```

---

# 💡 Security Best Practices

When developing Android applications:

* Never hardcode API keys.
* Never store passwords inside APKs.
* Use Android Keystore for sensitive information.
* Retrieve secrets securely from backend services.
* Rotate credentials regularly.
* Remove debug credentials before release.
* Encrypt sensitive local data.
* Use short-lived authentication tokens.
* Perform regular security reviews before deployment.

---

# 📈 Skills Gained

By completing this lab, you have developed hands-on experience with:

* 📱 Android APK reverse engineering
* 🔨 APKTool decompilation
* 🔍 Static code analysis
* 💻 Smali inspection
* 📄 XML resource analysis
* 🐍 Python automation
* 🔐 Secret detection
* 📊 JSON reporting
* 🛡 Mobile application security assessment

---

# 🚀 Next Steps

Expand your Android security knowledge by exploring:

## 📱 Dynamic Mobile Analysis

Recommended tools:

* Frida
* Objection
* Android Studio Debugger
* ADB

---

## 🔍 Advanced Static Analysis

Learn:

* Smali reverse engineering
* APK patching
* Obfuscation analysis
* Native library analysis
* Certificate pinning
* SSL pinning bypass

---

## 🛡 Mobile Penetration Testing

Practice:

* Authentication testing
* Secure storage testing
* IPC testing
* Network interception
* Runtime instrumentation
* Reverse engineering production applications (with authorization)

---

# 📚 Recommended Learning Path

```text
Android Fundamentals
        │
        ▼
APK Structure
        │
        ▼
APKTool
        │
        ▼
Static Analysis
        │
        ▼
Smali Analysis
        │
        ▼
Regex Pattern Matching
        │
        ▼
Python Automation
        │
        ▼
Secret Detection
        │
        ▼
Dynamic Analysis
        │
        ▼
Professional Mobile Penetration Testing
```

---

# 📌 Key Takeaways

✔ APKTool provides complete access to Android resources and Smali bytecode.

✔ XML resources and Smali files are common locations for hardcoded secrets.

✔ Regular expressions enable rapid discovery of credentials and API keys.

✔ Automated scanning significantly improves analysis speed and consistency.

✔ High-entropy string analysis helps uncover hidden or encoded secrets.

✔ Static analysis should always be complemented with manual review and, when appropriate, dynamic analysis.

---

# 🏁 Conclusion

Congratulations!

You have successfully completed the **Decode Hardcoded API Keys in APK** laboratory.

Throughout this exercise, you learned how to:

* 📦 Decompile Android APK files using APKTool.
* 🔍 Navigate the internal APK directory structure.
* 📄 Analyze XML resources and configuration files.
* 💻 Inspect Smali bytecode for embedded secrets.
* 🔑 Locate hardcoded API keys, access tokens, and sensitive credentials.
* 🐍 Build Python tools to automate secret detection using pattern matching and entropy analysis.
* 📊 Generate professional reports documenting your findings.

These skills are essential for mobile application security assessments, secure code reviews, Android penetration testing, malware analysis, and reverse engineering engagements.

---

# ⚖️ Ethical & Legal Notice

> **This lab is intended for educational purposes and authorized security testing only.**
>
> Only analyze Android applications that you own or for which you have explicit permission to assess. Unauthorized reverse engineering or extraction of sensitive information may violate software licenses, organizational policies, or applicable laws.
>
> Always follow responsible disclosure practices and perform security testing ethically.

---

<div align="center">

# ⭐ Congratulations!

### 🎉 You Have Successfully Completed the Lab

**Decode Hardcoded API Keys in APK**

🔐 **Practice Responsibly • Secure Applications • Keep Learning**

</div>


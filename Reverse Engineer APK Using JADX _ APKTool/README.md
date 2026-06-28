# 📱 Reverse Engineer APK Using JADX + APKTool

<div align="center">

# 📱 Reverse Engineering Android APKs

## Using APKTool • JADX • Python Automation

---

![Android](https://img.shields.io/badge/Android-APK-3DDC84?style=for-the-badge\&logo=android)
![APKTool](https://img.shields.io/badge/APKTool-Resources-blue?style=for-the-badge)
![JADX](https://img.shields.io/badge/JADX-Decompiler-orange?style=for-the-badge)
![Java](https://img.shields.io/badge/Java-JDK11-red?style=for-the-badge\&logo=openjdk)
![Python](https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge\&logo=python)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?style=for-the-badge\&logo=ubuntu)
![Linux](https://img.shields.io/badge/Linux-Terminal-FCC624?style=for-the-badge\&logo=linux)
![JSON](https://img.shields.io/badge/JSON-Reports-lightgrey?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-Reporting-E34F26?style=for-the-badge\&logo=html5)
![Security](https://img.shields.io/badge/Security-Mobile-red?style=for-the-badge)
![Reverse Engineering](https://img.shields.io/badge/Reverse-Engineering-purple?style=for-the-badge)

---

### 🔐 Mobile Application Security Laboratory

**Learn Android APK Reverse Engineering using Industry Standard Tools**

</div>

---

# 📖 Table of Contents

* Overview
* Learning Objectives
* Technologies Used
* Prerequisites
* Lab Environment
* Repository Structure
* Task 1 – Decompile APK with APKTool
* Task 2 – Analyze Source Code using JADX
* Task 3 – Automate APK Analysis using Python
* Expected Results
* Troubleshooting
* Conclusion

---

# 📚 Overview

Android applications are distributed as **APK (Android Package)** files.

Reverse engineering APKs helps security professionals:

* 🔍 Discover security vulnerabilities
* 🔑 Identify hardcoded credentials
* 📱 Analyze application behavior
* 🛡️ Perform security assessments
* ⚙️ Audit Android applications
* 🚨 Detect insecure coding practices

This lab introduces the complete Android reverse engineering workflow using **APKTool**, **JADX**, and **Python automation**.

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

* ✅ Decompile Android APK files using APKTool
* ✅ Extract Android resources and manifests
* ✅ Analyze Java source code using JADX
* ✅ Identify Android security vulnerabilities
* ✅ Search for hardcoded secrets
* ✅ Detect insecure coding practices
* ✅ Automate APK analysis with Python
* ✅ Generate professional JSON reports
* ✅ Produce HTML security reports

---

# 🛠 Technologies Used

| Technology        | Purpose             |
| ----------------- | ------------------- |
| 📱 Android APK    | Target Application  |
| 🔨 APKTool        | Resource Extraction |
| ☕ Java JDK 11     | Runtime             |
| 🐍 Python 3.10    | Automation          |
| 🔍 JADX           | Java Decompiler     |
| 🐧 Ubuntu 22.04   | Operating System    |
| 💻 Linux Terminal | Command Line        |
| 📄 JSON           | Reporting           |
| 🌐 HTML           | Security Reports    |

---

# 📋 Prerequisites

Before beginning this lab, ensure you have:

* ✅ Basic Android architecture knowledge
* ✅ Familiarity with Java
* ✅ Linux command line experience
* ✅ Basic Python programming
* ✅ Understanding of mobile application security

---

# 🖥️ Lab Environment

This lab is performed using the **Al Nafi Cloud Machine**.

### Environment Specifications

| Component        | Version          |
| ---------------- | ---------------- |
| Operating System | Ubuntu 22.04 LTS |
| Java             | JDK 11           |
| Python           | 3.10             |
| APKTool          | Installed        |
| JADX             | Installed        |

---

# 📂 Repository Structure

```text
apk-analysis/
│
├── apk-files/
│     └── diva-beta.apk
│
├── decompiled-output/
│     └── diva-decompiled/
│
├── jadx-output/
│     └── jadx-diva-output/
│
├── reports/
│     ├── analysis_report.json
│     └── analysis_report.html
│
├── apk_analyzer.py
├── string_analyzer.py
└── vulnerability_scanner.py
```

---

# 🚀 Task 1 — Decompile APK with APKTool

---

# 📌 Step 1.1 — Create the Working Environment

## 🎯 Objective

Create an organized workspace for APK reverse engineering.

---

### 📁 Create Analysis Directories

```bash
mkdir -p ~/apk-analysis/{apk-files,decompiled-output,jadx-output,reports}

cd ~/apk-analysis
```

---

### 🔍 Verify APKTool Installation

```bash
apktool --version
```

---

### ✅ Expected Output

```
2.x.x
```

---

### 💡 Why This Step?

Organizing files makes the reverse engineering workflow cleaner and easier to automate later.

---

# 📌 Step 1.2 — Download the Target APK

## 🎯 Objective

Download the **DIVA (Damn Insecure and Vulnerable App)** application for analysis.

---

### 📥 Download APK

```bash
cd ~/apk-analysis/apk-files

wget https://github.com/payatu/diva-android/raw/master/diva-beta.apk
```

---

### 📂 Verify Download

```bash
ls -lh diva-beta.apk
```

Example

```
-rw-r--r-- 1 user user 5.4M diva-beta.apk
```

---

### 🔎 Verify APK Format

```bash
file diva-beta.apk
```

Example

```
diva-beta.apk: Zip archive data
```

---

### 💡 Why This Step?

Every Android APK is essentially a ZIP archive containing:

* AndroidManifest.xml
* classes.dex
* resources
* assets
* native libraries

---

# 📌 Step 1.3 — Extract APK Information

## 🎯 Objective

Gather metadata before decompiling the application.

---

### 📦 View Package Information

```bash
aapt dump badging diva-beta.apk | grep -E "package|application-label|sdkVersion"
```

Example

```
package: name='jakhar.aseem.diva'
application-label:'DIVA'
sdkVersion:'14'
```

---

### 📂 View APK Contents

```bash
unzip -l diva-beta.apk | head -20
```

Example

```
AndroidManifest.xml
classes.dex
resources.arsc
META-INF/
res/
assets/
```

---

### 🔍 Information Collected

* 📦 Package Name
* 📱 Application Name
* 📌 SDK Version
* 📂 Internal File Structure

---

# 📌 Step 1.4 — Decompile APK using APKTool

## 🎯 Objective

Extract resources, manifest, and Smali code.

---

### 🔨 Decompile APK

```bash
cd ~/apk-analysis/decompiled-output

apktool d ../apk-files/diva-beta.apk -o diva-decompiled
```

---

### 📂 Navigate to Decompiled Files

```bash
cd diva-decompiled
```

---

### 🌳 View Directory Structure

```bash
tree -L 2
```

Example

```text
diva-decompiled
├── AndroidManifest.xml
├── apktool.yml
├── assets
├── lib
├── original
├── res
├── smali
└── unknown
```

---

### 📖 Understanding the Output

| Directory           | Description           |
| ------------------- | --------------------- |
| AndroidManifest.xml | Application Manifest  |
| smali               | Decompiled Bytecode   |
| res                 | Resources             |
| assets              | Application Assets    |
| lib                 | Native Libraries      |
| original            | Original APK Metadata |
| apktool.yml         | APKTool Configuration |

---

### 💡 Why APKTool?

APKTool extracts components unavailable through Java decompilers, including:

* Resources
* XML files
* Manifest
* Smali code
* Assets

---

# 📌 Step 1.5 — Analyze AndroidManifest.xml

## 🎯 Objective

Inspect the application's security configuration.

---

### 📄 Display Manifest

```bash
cat AndroidManifest.xml
```

---

### 🔑 Extract Permissions

```bash
grep "uses-permission" AndroidManifest.xml
```

Example

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

---

### 🔓 Identify Exported Components

```bash
grep -E "exported.*true" AndroidManifest.xml
```

---

### 🐞 Check Debug Configuration

```bash
grep "debuggable" AndroidManifest.xml
```

---

# 🔍 Security Analysis Checklist

During manifest review, verify the following:

### 🔴 Dangerous Permissions

* READ_EXTERNAL_STORAGE
* WRITE_EXTERNAL_STORAGE
* CAMERA
* RECORD_AUDIO
* ACCESS_FINE_LOCATION
* READ_CONTACTS

---

### 🔴 Exported Activities

Look for components exposed without authentication.

Example

```xml
android:exported="true"
```

---

### 🔴 Debuggable Applications

Production apps should never include:

```xml
android:debuggable="true"
```

---

### 🔴 Backup Enabled

Applications allowing backups may expose sensitive data.

Example

```xml
android:allowBackup="true"
```

---

### 🔴 Network Security Configuration

Look for:

```xml
android:networkSecurityConfig
```

which controls:

* Cleartext HTTP
* Certificate pinning
* Custom trust anchors

---

# 🎉 Task 1 Completed

At this point you have successfully:

* ✅ Downloaded the APK
* ✅ Extracted metadata
* ✅ Decompiled the APK using APKTool
* ✅ Explored project structure
* ✅ Reviewed AndroidManifest.xml
* ✅ Identified important security settings

---

# ➡️ Next

In **Part 2**, we will cover:

* 🔍 Reverse Engineering with JADX
* 📄 Java Source Analysis
* 🔑 Finding Hardcoded Credentials
* 💣 SQL Injection Discovery
* 🔒 Weak Cryptography Detection
* 🌐 Network Security Review
* 🚀 Beginning Python Automation

---

# 🔍 Task 2 — Analyze Decompiled Code Using JADX

---

# 📌 Step 2.1 — Decompile APK to Java Source

## 🎯 Objective

Convert the application's DEX bytecode into readable Java source code using **JADX**.

Unlike APKTool, which extracts resources and Smali code, JADX reconstructs Java source files that are significantly easier to read and audit.

---

## 📂 Navigate to the JADX Workspace

```bash
cd ~/apk-analysis/jadx-output
```

---

## 🚀 Decompile the APK

```bash
jadx -d jadx-diva-output ~/apk-analysis/apk-files/diva-beta.apk
```

---

## 📁 Verify Output

```bash
ls -la jadx-diva-output/
```

Example:

```text
resources/
sources/
```

---

## 🌳 Explore the Decompiled Source Tree

```bash
tree jadx-diva-output/sources -L 3
```

Example

```text
sources/
└── jakhar
    └── aseem
        └── diva
            ├── MainActivity.java
            ├── LoginActivity.java
            ├── SQLInjectionActivity.java
            ├── FileStorageActivity.java
            └── ...
```

---

## 💡 Why Use JADX?

JADX reconstructs readable Java code, allowing security analysts to:

* 🔍 Understand application logic
* 🔑 Locate secrets
* 💣 Find vulnerable functions
* 🌐 Inspect networking code
* 🔐 Review authentication logic

---

# 📌 Step 2.2 — Explore the Decompiled Source Code

## 🎯 Objective

Locate the application's Java source files.

---

## 📂 Navigate into Sources

```bash
cd jadx-diva-output/sources
```

---

## 📄 Display Java Files

```bash
find . -name "*.java" | head -10
```

Example

```text
./jakhar/aseem/diva/MainActivity.java
./jakhar/aseem/diva/LoginActivity.java
./jakhar/aseem/diva/InsecureDataStorageActivity.java
```

---

## 📱 List Activity Classes

```bash
find . -name "*Activity*.java"
```

Example

```text
MainActivity.java
LoginActivity.java
SQLInjectionActivity.java
NotesActivity.java
FileStorageActivity.java
```

---

## 💡 Why Focus on Activities?

Activities frequently contain:

* Login logic
* User authentication
* Database access
* Network requests
* Local storage
* File operations

These are common locations for security flaws.

---

# 📌 Step 2.3 — Search for Common Security Issues

## 🎯 Objective

Use Linux utilities to locate insecure coding patterns.

---

# 🔑 Search for Hardcoded Credentials

```bash
grep -rn -i "password\s*=\|secret\s*=\|key\s*=" . --include="*.java"
```

Possible findings:

* API Keys
* Passwords
* Encryption Keys
* Authentication Tokens

---

# 💣 Search for SQL Injection

```bash
grep -rn "SELECT\|INSERT\|UPDATE\|DELETE" . --include="*.java" | grep "+"
```

Unsafe example

```java
String query = "SELECT * FROM users WHERE username='" + username + "'";
```

⚠️ Dynamic SQL concatenation often indicates SQL Injection.

---

# 📂 Search for File Operations

```bash
grep -rn "openFileOutput\|getSharedPreferences" . --include="*.java"
```

Look for:

* SharedPreferences
* Internal Storage
* External Storage

---

# 🌐 Search for Network Operations

```bash
grep -rn "http://\|HttpURLConnection" . --include="*.java"
```

Possible issues include:

* HTTP instead of HTTPS
* Plaintext traffic
* Weak certificate validation

---

# 🔐 Search for Weak Cryptography

```bash
grep -rn "DES\|MD5\|SHA1" . --include="*.java"
```

Weak algorithms include:

* DES
* MD5
* SHA1

Recommended replacements:

* AES-256
* SHA-256
* SHA-384
* SHA-512

---

# 📊 Summary of Manual Searches

| Search            | Purpose                |
| ----------------- | ---------------------- |
| password          | Hardcoded Secrets      |
| SELECT            | SQL Injection          |
| SharedPreferences | Insecure Storage       |
| HTTP              | Insecure Communication |
| MD5               | Weak Cryptography      |

---

# 📌 Step 2.4 — Analyze Critical Source Files

## 🎯 Objective

Review sensitive Java classes for insecure implementations.

---

## 📖 Display MainActivity

```bash
find . -name "MainActivity.java" -exec cat {} \;
```

Carefully review:

* User input
* Authentication
* Navigation
* Sensitive methods

---

## 🔓 Search for Insecure File Permissions

```bash
grep -rn "MODE_WORLD_READABLE\|MODE_WORLD_WRITABLE" . --include="*.java"
```

These permissions expose application data to other apps and should never be used.

---

## 🌍 Search for WebView Configuration

```bash
grep -rn "setJavaScriptEnabled\|addJavascriptInterface" . --include="*.java"
```

Potential risks:

* JavaScript Injection
* Remote Code Execution
* Cross-App Scripting

---

# 🛡️ Manual Security Review Checklist

During your code review, verify the following:

### 🔴 Hardcoded Passwords

```java
String password = "admin123";
```

---

### 🔴 Hardcoded API Keys

```java
String apiKey = "AIza...";
```

---

### 🔴 SQL Injection

```java
String query = "SELECT * FROM users WHERE id=" + id;
```

---

### 🔴 Weak Hashing

```java
MessageDigest.getInstance("MD5");
```

---

### 🔴 DES Encryption

```java
Cipher.getInstance("DES");
```

---

### 🔴 Insecure WebView

```java
webView.getSettings().setJavaScriptEnabled(true);
```

---

### 🔴 World Readable Files

```java
MODE_WORLD_READABLE
```

---

### 🔴 HTTP Communication

```java
http://example.com
```

---

# 🎯 Common Vulnerabilities Found in DIVA

The DIVA application intentionally contains numerous security flaws for educational purposes.

Typical findings include:

| Vulnerability              | Severity  |
| -------------------------- | --------- |
| Hardcoded Credentials      | 🔴 High   |
| SQL Injection              | 🔴 High   |
| Insecure SharedPreferences | 🟠 Medium |
| Weak Cryptography          | 🟠 Medium |
| Exported Components        | 🟠 Medium |
| HTTP Communication         | 🟡 Low    |
| Weak Input Validation      | 🔴 High   |

---

# 🚀 Task 3 — Automate APK Analysis with Python

---

# 📌 Step 3.1 — Build the APK Analyzer

## 🎯 Objective

Instead of manually repeating the same analysis every time, automate the workflow using Python.

The automation script will perform the following tasks:

* ✅ Calculate APK SHA-256 hash
* ✅ Extract APK metadata
* ✅ Execute APKTool
* ✅ Analyze AndroidManifest.xml
* ✅ Execute JADX
* ✅ Scan Java source files
* ✅ Detect common vulnerabilities
* ✅ Produce JSON reports
* ✅ Generate HTML reports

---

## 📄 Create the Main Analyzer Script

Create the following file:

```text
~/apk-analysis/apk_analyzer.py
```

> **📌 Note:** The **complete source code** for `apk_analyzer.py` will be provided in **Part 3** of this README.

---

## Make the Script Executable

```bash
chmod +x ~/apk-analysis/apk_analyzer.py
```

---

# 📌 Step 3.2 — Build the String Analyzer

## 🎯 Objective

Automatically extract interesting strings from the decompiled Java source.

The analyzer will identify:

* 🌐 URLs
* 🌍 IP Addresses
* 📧 Email Addresses
* 🔑 API Keys
* 🔒 Secrets
* 🪙 Tokens

---

Create:

```text
~/apk-analysis/string_analyzer.py
```

> **📌 Note:** The complete implementation is included in **Part 3**.

---

# 📌 Step 3.3 — Build the Vulnerability Scanner

## 🎯 Objective

Create a dedicated scanner that detects Android security issues automatically.

The scanner will inspect:

* Hardcoded credentials
* SQL Injection
* Weak cryptography
* HTTP endpoints
* SharedPreferences misuse
* Insecure WebViews
* Dangerous file permissions

Create:

```text
~/apk-analysis/vulnerability_scanner.py
```

> **📌 Note:** The full source code is provided in **Part 3**.

---

# 📌 Step 3.4 — Execute the Automated Analysis

Run the complete toolkit.

---

## Run the Main Analyzer

```bash
cd ~/apk-analysis

python3 apk_analyzer.py apk-files/diva-beta.apk
```

---

## Run the String Analyzer

```bash
python3 string_analyzer.py jadx-output/jadx-diva-output/sources
```

---

## Run the Vulnerability Scanner

```bash
python3 vulnerability_scanner.py jadx-output/jadx-diva-output/sources
```

---

# 📌 Step 3.5 — Review Generated Reports

## View JSON Report

```bash
cd ~/apk-analysis/reports

cat analysis_report_*.json | jq '.'
```

---

## Open HTML Report

```bash
firefox analysis_report_*.html &
```

---

# 🎉 Part 2 Complete

You have now learned how to:

* ✅ Decompile APKs into Java source using JADX
* ✅ Navigate the reconstructed source code
* ✅ Identify common Android vulnerabilities
* ✅ Search for insecure coding practices
* ✅ Prepare an automated APK analysis workflow
* ✅ Execute Python-based security tools

---

# ➡️ Next: Part 3

In **Part 3**, we'll include the **complete source code** for:

* 🐍 `apk_analyzer.py`
* 🐍 `string_analyzer.py`
* 🐍 `vulnerability_scanner.py`

These scripts will be fully implemented and ready to copy directly into your repository.
---

# 📊 Expected Outcomes

After successfully completing this laboratory, you should have accomplished the following:

---

## 📦 Decompiled APK Structure

You should have extracted the complete APK contents using **APKTool**, including:

* ✅ AndroidManifest.xml
* ✅ Application resources
* ✅ Assets
* ✅ Native libraries
* ✅ Smali bytecode
* ✅ APK configuration files

---

## ☕ Decompiled Java Source

Using **JADX**, you should have generated readable Java source code suitable for manual security review.

This enables:

* 🔍 Source code inspection
* 🔐 Authentication review
* 🌐 Network analysis
* 📂 Storage analysis
* 💣 Vulnerability discovery

---

## 🚨 Security Findings

During the assessment, you should have identified multiple security weaknesses.

### 🔴 Hardcoded Credentials

Example:

```java
String password = "admin123";
```

---

### 🔴 SQL Injection

Example:

```java
String query = "SELECT * FROM users WHERE username='" + username + "'";
```

---

### 🟠 Weak Cryptography

Examples include:

* MD5
* SHA1
* DES

---

### 🟠 Insecure File Operations

Examples:

* SharedPreferences
* World Readable Files
* External Storage

---

### 🔴 Dangerous Android Permissions

Examples:

* READ_EXTERNAL_STORAGE
* WRITE_EXTERNAL_STORAGE
* CAMERA
* ACCESS_FINE_LOCATION
* RECORD_AUDIO

---

### 🟠 Exported Components

Activities or services accessible without proper authorization.

---

### 🌐 Insecure Network Communication

Examples include:

* HTTP traffic
* Missing certificate validation
* Weak TLS configuration

---

# 🧪 Example Findings from the DIVA Application

The DIVA application intentionally contains vulnerable code for educational purposes.

Typical findings include:

| Vulnerability              | Severity  |
| -------------------------- | --------- |
| Hardcoded Vendor Key       | 🔴 High   |
| SQL Injection              | 🔴 High   |
| Insecure SharedPreferences | 🟠 Medium |
| Weak Cryptography          | 🟠 Medium |
| Weak Input Validation      | 🔴 High   |
| Exported Activities        | 🟠 Medium |
| Backup Enabled             | 🟡 Low    |
| Insecure File Permissions  | 🔴 High   |

---

# 📂 Generated Reports

Your automation scripts should generate reports similar to:

```text
reports/
├── analysis_report.json
├── analysis_report.html
└── strings_report.txt
```

---

## JSON Report

Contains:

* APK Information
* SHA-256 Hash
* Permissions
* Exported Components
* Vulnerabilities
* File Locations
* Analysis Timestamp

---

## HTML Report

Professional report including:

* Executive Summary
* APK Information
* Risk Overview
* Security Findings
* Vulnerability Details
* Recommendations

---

# 🧾 Sample JSON Report

```json
{
  "apk_name": "diva-beta.apk",
  "package": "jakhar.aseem.diva",
  "analysis_date": "2026-06-27T13:15:20",
  "permissions": [
    "INTERNET",
    "WRITE_EXTERNAL_STORAGE",
    "READ_EXTERNAL_STORAGE"
  ],
  "vulnerabilities": [
    {
      "type": "Hardcoded Credential",
      "severity": "High"
    },
    {
      "type": "SQL Injection",
      "severity": "High"
    }
  ]
}
```

---

# 📄 Sample HTML Report

A typical report should include:

* 📱 APK Overview
* 📦 Package Information
* 🔐 Manifest Analysis
* 🚨 Security Findings
* 📂 Vulnerable Files
* 📈 Risk Summary
* ✅ Recommendations

---

# 📈 Risk Classification

| Severity         | Description                     |
| ---------------- | ------------------------------- |
| 🔴 Critical      | Immediate exploitation possible |
| 🔴 High          | Significant security impact     |
| 🟠 Medium        | Requires remediation            |
| 🟡 Low           | Best practice recommendation    |
| 🔵 Informational | No immediate risk               |

---

# 🛡️ Security Assessment Checklist

Use the following checklist during every Android application assessment.

| Check                       | Status |
| --------------------------- | ------ |
| APK Decompiled              | ✅      |
| Manifest Reviewed           | ✅      |
| Permissions Audited         | ✅      |
| Exported Components Checked | ✅      |
| Hardcoded Secrets Reviewed  | ✅      |
| SQL Injection Tested        | ✅      |
| Network Traffic Reviewed    | ✅      |
| File Storage Audited        | ✅      |
| Weak Crypto Identified      | ✅      |
| Reports Generated           | ✅      |

---

# 🛠 Troubleshooting Guide

---

## ❌ APKTool Exception

### Error

```text
brut.androlib.AndrolibException
```

### Solution

```bash
apktool d app.apk -r
```

Or update APKTool to the latest version.

---

## ❌ JADX Produces Obfuscated Code

### Solution

Use:

```bash
jadx --deobf app.apk
```

This attempts to improve readability for obfuscated applications.

---

## ❌ Python Encoding Errors

### Solution

Open files using UTF-8 with ignored decoding errors.

```python
open(file_path, encoding="utf-8", errors="ignore")
```

---

## ❌ Vulnerability Scanner Finds Nothing

Possible reasons:

* Application is obfuscated.
* Strings are encrypted.
* Vulnerabilities are dynamically generated.

Recommended actions:

* Perform manual code review.
* Search for method signatures.
* Analyze runtime behavior.

---

## ❌ Reports Directory Missing

Create it manually.

```bash
mkdir -p ~/apk-analysis/reports
```

Grant write permissions.

```bash
chmod 755 ~/apk-analysis/reports
```

---

## ❌ APK Cannot Be Decompiled

Verify the APK is valid.

```bash
file app.apk
```

Expected output:

```text
Zip archive data
```

---

# 💡 Best Practices

When performing Android reverse engineering:

* ✅ Analyze only applications you own or have permission to test.
* ✅ Verify hashes before analysis.
* ✅ Use multiple tools for better coverage.
* ✅ Combine manual and automated review.
* ✅ Validate findings dynamically whenever possible.
* ✅ Document every discovered issue.
* ✅ Follow responsible disclosure practices.

---

# 🔒 Security Recommendations

To improve Android application security:

* Avoid hardcoded credentials.
* Never enable debugging in production builds.
* Disable unnecessary exported components.
* Use HTTPS exclusively.
* Replace MD5, SHA1, and DES with modern cryptography.
* Encrypt sensitive local storage.
* Validate all user input.
* Use parameterized SQL queries.
* Restrict backup functionality when handling sensitive data.
* Enable certificate pinning where appropriate.

---

# 🎓 Skills Gained

By completing this lab, you have developed practical experience with:

* 📱 Android APK reverse engineering
* 🔨 APKTool resource extraction
* ☕ Java source code analysis
* 🔍 Static application security testing
* 🐍 Python automation
* 🛡️ Mobile vulnerability assessment
* 📄 Professional report generation
* 🚨 Android security auditing

---

# 🚀 Next Steps

Continue building your Android application security skills by exploring:

## 📱 Dynamic Analysis

Recommended tools:

* Frida
* Objection
* Android Studio Debugger
* ADB

---

## 🔐 Advanced Reverse Engineering

Topics to explore:

* Smali programming
* APK patching
* Signature bypass
* Anti-tampering mechanisms
* Root detection bypass
* SSL pinning bypass

---

## 🛡️ Mobile Penetration Testing

Practice:

* Authentication testing
* Storage testing
* IPC testing
* Network interception
* Runtime instrumentation

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
JADX
        │
        ▼
Static Analysis
        │
        ▼
Python Automation
        │
        ▼
Dynamic Analysis
        │
        ▼
Frida & Objection
        │
        ▼
Professional Mobile Penetration Testing
```

---

# 📌 Key Takeaways

✔ APKTool extracts resources, manifests, and Smali code.

✔ JADX converts DEX bytecode into readable Java source.

✔ AndroidManifest.xml is a valuable source of security configuration details.

✔ Static analysis helps identify hardcoded secrets, insecure storage, SQL injection, and weak cryptography.

✔ Automated analysis increases efficiency, but manual verification remains essential.

✔ Combining multiple tools provides more comprehensive application assessments.

---

# 🏁 Conclusion

Congratulations!

You have successfully completed the **Reverse Engineer APK Using JADX + APKTool** laboratory.

Throughout this lab, you learned how to:

* 📦 Decompile Android APK files
* 📄 Extract application resources
* 🔍 Analyze Java source code
* 🛡️ Identify common Android security vulnerabilities
* 🐍 Automate static analysis with Python
* 📊 Generate professional security assessment reports

These skills form a strong foundation for Android reverse engineering, mobile application penetration testing, malware analysis, and secure software assessment.

Continue practicing with intentionally vulnerable applications before progressing to assessments of production applications where you have explicit authorization.

---

# ⚖️ Ethical & Legal Notice

> **This laboratory is intended solely for educational and authorized security testing purposes.**
>
> Only analyze Android applications that you own or for which you have explicit written permission to assess.
>
> Unauthorized reverse engineering, vulnerability discovery, or security testing may violate software license agreements, organizational policies, or applicable laws. Always act responsibly and follow responsible disclosure practices.

---

<div align="center">

## ⭐ Thank You for Completing This Lab!

**Happy Learning • Practice Responsibly • Stay Curious • Secure the Mobile Ecosystem**

</div>

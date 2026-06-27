# 📱 Explore iOS Filesystem and Keychain Secrets

<div align="center">

# 🔐 Mobile Application Penetration Testing 

### iOS Filesystem • Keychain Analysis • Python Automation • Security Assessment

![Platform](https://img.shields.io/badge/Platform-iOS-black?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Mobile%20Security-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge)
![Storage](https://img.shields.io/badge/Focus-Keychain-success?style=for-the-badge)
![Environment](https://img.shields.io/badge/Linux-Ubuntu%2022.04-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Lab-Hands--On-brightgreen?style=for-the-badge)

</div>

---

# 📖 Overview

This hands-on lab introduces students to the internal structure of the **iOS filesystem** and demonstrates how security professionals analyze **Keychain secrets** within a simulated iOS environment.

Students will build a virtual iOS filesystem on Linux, create Python-based tools to discover and extract Keychain entries, inspect application storage, and identify security weaknesses in stored credentials. The lab also introduces automated reporting techniques commonly used during professional mobile application security assessments.

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

- 📱 Understand the iOS filesystem hierarchy
- 🔐 Understand iOS Keychain architecture
- 🗂 Create a simulated iOS filesystem
- 🔍 Locate Keychain databases
- 🐍 Build Python tools for Keychain extraction
- 📊 Analyze stored credentials
- 🔒 Evaluate password strength
- 🛡 Identify insecure application storage
- 📄 Generate professional security reports
- ⚙ Automate filesystem security analysis

---

# 🧠 Skills You Will Gain

- Mobile Application Penetration Testing
- iOS Security Assessment
- Filesystem Analysis
- Keychain Analysis
- Python Automation
- Password Auditing
- Secure Storage Assessment
- Security Reporting
- Linux Administration
- Security Tool Development

---

# 🛠 Technologies Used

## Mobile Platform

- iOS

## Operating System

- Ubuntu 22.04

## Programming Languages

- Python 3.10+
- Bash

## Security Technologies

- iOS Keychain
- Property Lists (plist)
- JSON
- SQLite
- Linux Filesystem

## Python Libraries

- pathlib
- json
- datetime
- pycryptodome

---

# 📚 Prerequisites

Before starting this lab, students should have:

- Basic Linux command-line experience
- Fundamental Python programming skills
- Basic understanding of mobile application security
- Familiarity with Linux file permissions
- Understanding of directory structures

---

# 🖥 Lab Environment

The lab uses a pre-configured Ubuntu Linux machine with:

- Python 3.10+
- SQLite
- Tree
- Pip
- PyCryptodome
- Linux utilities
- Preconfigured development environment

---

# 🏗 Lab Architecture

```
                  Ubuntu Linux
                       │
                       ▼
         Simulated iOS Filesystem
                       │
       ┌───────────────┼───────────────┐
       │               │               │
       ▼               ▼               ▼
 Applications      Library        System
                       │
                       ▼
                  Keychains
                       │
                       ▼
             Python Extraction Tool
                       │
                       ▼
              Security Analyzer
                       │
                       ▼
          JSON & HTML Assessment Reports
```

---

# 📂 Project Structure

```text
ios-security-lab/
│
├── ios-filesystem/
│   ├── Applications/
│   ├── Library/
│   │   ├── Keychains/
│   │   ├── Preferences/
│   │   └── Caches/
│   ├── System/
│   └── var/
│
├── keychain_dumper.py
├── security_analyzer.py
├── batch_analyzer.py
│
├── results/
└── batch_results/
```

---

# 🚀 Task 1 — Create a Simulated iOS Filesystem

---

# 🎯 Objective

Create a realistic iOS filesystem that can be used to perform mobile security assessments without requiring a physical iPhone.

---

## Step 1 — Create the Working Directory

Create the project workspace.

```bash
mkdir -p ~/ios-security-lab

cd ~/ios-security-lab
```

---

## Step 2 — Create the iOS Filesystem Structure

Generate a simplified iOS directory hierarchy.

```bash
mkdir -p ios-filesystem/{Applications,Library,System,var}

mkdir -p ios-filesystem/Applications/TestApp.app

mkdir -p ios-filesystem/Library/{Keychains,Preferences,Caches}

mkdir -p ios-filesystem/var/{mobile,log}
```

---

## Step 3 — Verify the Directory Structure

```bash
tree ios-filesystem/
```

---

### ✅ Expected Output

```
ios-filesystem/

├── Applications
│   └── TestApp.app
│
├── Library
│   ├── Keychains
│   ├── Preferences
│   └── Caches
│
├── System
│
└── var
    ├── log
    └── mobile
```

---

# 📁 Understanding the Directory Layout

| Directory | Purpose |
|------------|----------|
| Applications | Installed iOS applications |
| Library | Stores application data |
| Keychains | Secure credential storage |
| Preferences | Application configuration |
| Caches | Temporary files |
| System | Operating system components |
| var | User and runtime data |

---

# 🚀 Step 4 — Create a Sample iOS Application

Create the application's metadata file.

```bash
cat > ios-filesystem/Applications/TestApp.app/Info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"

"http://www.apple.com/DTDs/PropertyList-1.0.dtd">

<plist version="1.0">

<dict>

<key>CFBundleIdentifier</key>

<string>com.example.testapp</string>

<key>CFBundleName</key>

<string>TestApp</string>

<key>CFBundleVersion</key>

<string>1.0</string>

</dict>

</plist>
EOF
```

---

# 📄 Info.plist Overview

The **Info.plist** file contains application metadata used by iOS.

Important fields include:

| Key | Description |
|------|-------------|
| CFBundleIdentifier | Unique application identifier |
| CFBundleName | Application name |
| CFBundleVersion | Application version |

---

# 🚀 Step 5 — Create Sample Keychain Data

The lab uses simulated Keychain databases containing sample credentials for security analysis.

Create the primary Keychain database.

```bash
cat > ios-filesystem/Library/Keychains/keychain-2.db << 'EOF'
service: com.example.testapp
account: user@example.com
password: Test123
access_group: com.example.testapp
creation_date: 2024-01-15

service: com.banking.secure
account: john.doe@bank.com
password: SecureBank@2024!
access_group: com.banking.secure
creation_date: 2024-02-01

service: com.social.app
account: socialuser
password: password
access_group: com.social.app
creation_date: 2024-01-20
EOF
```

---

Create an additional Keychain database.

```bash
cat > ios-filesystem/Library/Keychains/keychain-3.db << 'EOF'
service: com.enterprise.vpn
account: employee@company.com
password: VPN_P@ssw0rd_2024
access_group: com.enterprise.vpn
creation_date: 2024-02-10

service: com.email.client
account: user@email.com
password: 123456
access_group: com.email.client
creation_date: 2024-01-05
EOF
```

---

# 📊 Simulated Keychain Entries

The sample databases include credentials for:

- Mobile applications
- Banking applications
- Social media applications
- VPN services
- Email clients

These entries provide realistic data for learning how to identify weak passwords and insecure storage practices.

---

# 🚀 Step 6 — Install Required Tools

Update package repositories.

```bash
sudo apt update
```

Install required packages.

```bash
sudo apt install -y python3 python3-pip sqlite3 tree
```

Install Python dependency.

```bash
pip3 install --user pycryptodome
```

---

# 📦 Installed Components

| Tool | Purpose |
|------|---------|
| Python 3 | Automation |
| SQLite | Database inspection |
| Tree | Directory visualization |
| Pip | Package management |
| PyCryptodome | Cryptographic operations |

---

# 🎉 Part 1 Complete

You have successfully:

- ✅ Created a simulated iOS filesystem
- ✅ Built the required directory hierarchy
- ✅ Created a sample iOS application
- ✅ Generated sample Keychain databases
- ✅ Installed all required tools
- ✅ Prepared the environment for Keychain extraction and security analysis

---

➡️ **Next:** **Part 2** covers:

- 🔐 Building the Keychain Extraction Tool
- 🐍 Developing a Python Keychain Dumper
- 📊 Parsing Keychain Entries
- 🔒 Implementing Password Strength Analysis
- 📄 Generating JSON and HTML Security Reports

- # 🚀 Task 2 — Build the Keychain Extraction Tool

---

# 🎯 Objective

The purpose of this task is to build a custom **Python Keychain Dumper** capable of locating, parsing, and extracting credentials stored inside simulated iOS Keychain databases.

By the end of this section, you will understand how security professionals automate the discovery of sensitive credentials during mobile application penetration tests.

---

# 🔐 Understanding the iOS Keychain

The **iOS Keychain** is Apple's secure storage mechanism for protecting sensitive application data.

Applications commonly store:

- Usernames
- Passwords
- Authentication Tokens
- API Keys
- Certificates
- VPN Credentials
- Wi-Fi Passwords
- Encryption Keys

Unlike normal files, Keychain items are encrypted and protected by iOS security mechanisms.

---

# 📊 Keychain Extraction Workflow

```text
Locate Keychain Files
          │
          ▼
Read Database Files
          │
          ▼
Parse Entries
          │
          ▼
Extract Credentials
          │
          ▼
Generate JSON Report
```

---

# 🛠 Step 1 — Create the Keychain Dumper

Create the following file.

```text
keychain_dumper.py
```

---

# 🧩 Tool Responsibilities

The Python utility will:

- Discover Keychain databases
- Parse stored credentials
- Extract account information
- Organize extracted entries
- Export structured reports

---

# 📦 Class Structure

```text
KeychainDumper
│
├── __init__()
├── find_keychain_files()
├── extract_from_file()
├── dump_keychain_data()
└── generate_report()
```

---

# 🔍 Locate Keychain Files

The first stage is locating Keychain databases inside the simulated filesystem.

Supported file types include:

- `.db`
- `.keychain`
- `.plist`

The search should recursively inspect the target directory for supported file types.

---

# 📖 Extract Keychain Entries

Each discovered file should be parsed for entries such as:

```text
service:
account:
password:
access_group:
creation_date:
```

---

# 📄 Expected Parsed Entry

```json
{
    "service":"com.example.testapp",
    "account":"user@example.com",
    "password":"Test123"
}
```

---

# ▶ Make the Script Executable

```bash
chmod +x keychain_dumper.py
```

---

# ▶ Execute the Keychain Dumper

```bash
python3 keychain_dumper.py ios-filesystem/Library/Keychains/
```

---

# 📄 Display the Generated Report

```bash
cat keychain_report.json | python3 -m json.tool
```

---

# ✅ Expected Report Structure

```json
{
    "extraction_summary":{
        "total_entries":5,
        "keychain_path":"ios-filesystem/Library/Keychains/"
    },

    "keychain_entries":[]
}
```

---

# 📊 Extracted Information

The report should contain:

- Service Name
- Username
- Password
- Access Group
- Creation Date

---

# 🚀 Task 3 — Implement Security Analysis

---

# 🎯 Objective

Building a Keychain dumper is only the first step.

Professional penetration testers must also evaluate the extracted credentials to identify weak passwords, insecure storage practices, and other security risks.

---

# 🔎 Security Analysis Workflow

```text
Extract Credentials
          │
          ▼
Password Analysis
          │
          ▼
Secret Discovery
          │
          ▼
Risk Classification
          │
          ▼
Generate Recommendations
          │
          ▼
Create Reports
```

---

# 🛠 Step 1 — Create the Security Analyzer

Create

```text
security_analyzer.py
```

---

# 📦 Analyzer Responsibilities

The analyzer will:

- Scan Keychain databases
- Evaluate password strength
- Search plist files for secrets
- Calculate risk levels
- Produce executive summaries
- Generate recommendations
- Export JSON reports
- Generate HTML dashboards

---

# 🧩 Class Design

```text
SecurityAnalyzer
│
├── __init__()
├── analyze_password_strength()
├── scan_keychain_files()
├── scan_plist_files()
├── generate_executive_summary()
├── generate_recommendations()
├── generate_html_report()
└── run_analysis()
```

---

# 🔐 Password Strength Analysis

Each password should be evaluated using common security criteria.

Checks include:

- Minimum length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Dictionary words
- Common weak passwords

---

# 📊 Risk Classification

| Risk | Description |
|-------|-------------|
| 🔴 High | Weak password or exposed secret |
| 🟠 Medium | Moderate security weakness |
| 🟢 Low | Strong implementation |

---

# 🔍 Analyze Keychain Files

The analyzer inspects every discovered Keychain file and performs:

- Credential extraction
- Password evaluation
- Risk scoring
- Security issue identification

---

# 🔎 Scan Property List Files

The analyzer also searches every **Info.plist** and configuration file for embedded secrets.

Typical indicators include:

- Passwords
- Tokens
- API Keys
- Secrets
- Encryption Keys

---

# 📈 Executive Summary

The generated summary includes:

- Files scanned
- Credentials discovered
- Weak passwords
- Security issues
- Overall risk rating

---

# 💡 Security Recommendations

Recommendations should include guidance such as:

- Use strong passwords
- Avoid storing plaintext credentials
- Protect Keychain access
- Remove hardcoded secrets
- Use secure storage APIs
- Rotate exposed credentials
- Apply least privilege principles

---

# 🌐 HTML Security Report

In addition to JSON, the analyzer generates an HTML dashboard.

The report includes:

- Executive Summary
- Findings
- Password Analysis
- Risk Charts
- Recommendations

---

# ▶ Execute the Analyzer

```bash
mkdir -p results
```

Run the security analysis.

```bash
python3 security_analyzer.py ios-filesystem/ -o results/
```

---

# 📂 Review Generated Reports

```bash
ls -la results/
```

Display the JSON report.

```bash
cat results/comprehensive_report.json | python3 -m json.tool
```

---

# 🌍 View HTML Report

If running in a graphical environment:

```bash
firefox results/security_report.html
```

Or inspect the HTML source.

```bash
cat results/security_report.html
```

---

# 📊 Expected Security Findings

The analyzer may identify issues such as:

- Weak passwords
- Reused credentials
- Hardcoded secrets
- Sensitive data in plist files
- Improper storage practices
- Weak authentication mechanisms

---

# 🎯 Skills Developed

During this section you learned how to:

- ✅ Build a Python Keychain Dumper
- ✅ Locate Keychain databases
- ✅ Parse credential records
- ✅ Analyze password strength
- ✅ Search for embedded secrets
- ✅ Classify security risks
- ✅ Produce executive summaries
- ✅ Generate JSON reports
- ✅ Generate HTML security dashboards

---

# 🎉 Part 2 Complete

You have successfully:

- 🔐 Built a custom Keychain extraction utility
- 🐍 Automated credential extraction with Python
- 🔍 Implemented password strength analysis
- 📊 Classified discovered security risks
- 📄 Generated professional JSON reports
- 🌐 Produced HTML security assessment dashboards
- 🛡️ Applied automated techniques used in real-world mobile application security assessments

---

➡️ **Next:** **Part 3** covers:

- 📦 Automated Batch Analysis
- 📊 Comparing Multiple iOS Applications
- 📄 Batch Reporting
- ✅ Verification
- 🛠 Troubleshooting
- 📈 Expected Outcomes
- 🎓 Key Takeaways
- 🔒 Security Best Practices
- 🤝 Contributing
- ⭐ Support

# 🚀 Task 4 — Automated Batch Analysis

---

# 🎯 Objective

Large mobile application assessments often involve dozens or even hundreds of applications. Manually reviewing each one is inefficient and error-prone.

In this task, you will build a **Batch Analyzer** capable of automatically discovering multiple iOS applications, performing security analysis, comparing findings, and generating consolidated reports.

---

# 📊 Batch Analysis Workflow

```text
Locate Applications
        │
        ▼
Analyze Each Application
        │
        ▼
Extract Keychain Data
        │
        ▼
Perform Security Analysis
        │
        ▼
Generate Individual Reports
        │
        ▼
Create Comparative Report
```

---

# 🛠 Step 1 — Create the Batch Analyzer

Create the following file.

```text
batch_analyzer.py
```

---

# 📦 Batch Analyzer Responsibilities

The tool should:

- Discover iOS applications
- Parse Info.plist files
- Analyze Keychain entries
- Search for sensitive information
- Compare security findings
- Rank application risk
- Generate summary reports

---

# 🧩 Class Structure

```text
BatchAnalyzer
│
├── __init__()
├── find_applications()
├── analyze_single_app()
├── process_all_apps()
├── generate_comparison_report()
└── export_results()
```

---

# 📂 Discover Applications

The analyzer recursively searches for application bundles.

Supported application format:

```
*.app
```

Example:

```
Applications/

├── TestApp.app

├── SecureApp.app

└── WeakApp.app
```

---

# 🔎 Analyze Each Application

For every discovered application, the analyzer should inspect:

- Info.plist
- Bundle Identifier
- Application Metadata
- Keychain Usage
- Sensitive Files
- Configuration Files

---

# 📊 Comparative Analysis

The analyzer compares all applications and identifies:

- Weakest application
- Strongest application
- Common vulnerabilities
- Shared security weaknesses
- Credential reuse
- Configuration problems

---

# 📈 Risk Ranking

Applications are ranked according to discovered issues.

| Risk | Description |
|------|-------------|
| 🔴 High | Critical weaknesses |
| 🟠 Medium | Moderate findings |
| 🟢 Low | Secure implementation |

---

# 🚀 Step 2 — Create Additional Applications

Create a second application.

```bash
mkdir -p ios-filesystem/Applications/SecureApp.app
```

Create its Info.plist.

```bash
cat > ios-filesystem/Applications/SecureApp.app/Info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>

<plist version="1.0">

<dict>

<key>CFBundleIdentifier</key>

<string>com.secure.app</string>

<key>CFBundleName</key>

<string>SecureApp</string>

</dict>

</plist>
EOF
```

---

Create another application.

```bash
mkdir -p ios-filesystem/Applications/WeakApp.app
```

```bash
cat > ios-filesystem/Applications/WeakApp.app/Info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>

<plist version="1.0">

<dict>

<key>CFBundleIdentifier</key>

<string>com.weak.app</string>

<key>CFBundleName</key>

<string>WeakApp</string>

</dict>

</plist>
EOF
```

---

# ▶ Execute Batch Analysis

Run the analyzer.

```bash
python3 batch_analyzer.py ios-filesystem/Applications/ -o batch_results/
```

---

# 📄 View Results

```bash
cat batch_results/batch_summary.json | python3 -m json.tool
```

---

# 📊 Example Output

```text
Applications Scanned : 3

High Risk : 1

Medium Risk : 1

Low Risk : 1

Common Findings : Weak Passwords

Reports Generated : Success
```

---

# 📁 Batch Results Directory

```text
batch_results/

├── batch_summary.json

├── comparison_report.json

├── dashboard.html

└── application_reports/
```

---

# ✅ Lab Verification

Verify the environment after completing the lab.

---

# 🎯 Verification Checklist

Ensure the following items are completed successfully.

- ✅ Simulated iOS filesystem created
- ✅ Keychain databases discovered
- ✅ Python extraction tool functioning
- ✅ Security analyzer completed
- ✅ JSON reports generated
- ✅ HTML reports generated
- ✅ Batch analysis completed

---

# 📂 Verify Directory Structure

```bash
tree ios-security-lab
```

---

# Expected Structure

```text
ios-security-lab/

├── ios-filesystem/

├── keychain_dumper.py

├── security_analyzer.py

├── batch_analyzer.py

├── results/

└── batch_results/
```

---

# Verify Reports

```bash
ls -la results/

ls -la batch_results/
```

---

# Verify JSON Files

```bash
python3 -m json.tool results/comprehensive_report.json

python3 -m json.tool batch_results/batch_summary.json
```

---

# 🛠 Troubleshooting Guide

---

## ❌ Permission Errors

Symptoms

```
Permission denied
```

Solution

```bash
chmod +x *.py

chmod -R u+rw ios-filesystem/
```

---

## ❌ Missing Python Modules

Symptoms

```
ModuleNotFoundError
```

Solution

```bash
pip3 install --user --upgrade pycryptodome
```

Verify installation.

```bash
python3 -c "import Crypto; print('Success')"
```

---

## ❌ Empty Keychain Results

Possible causes:

- Missing Keychain database
- Incorrect file format
- Parsing logic incomplete

Verify files.

```bash
ls -la ios-filesystem/Library/Keychains/
```

---

## ❌ Invalid JSON

Validate reports.

```bash
python3 -m json.tool keychain_report.json
```

Pretty-print output.

```bash
cat keychain_report.json | python3 -m json.tool
```

---

# 🔒 Security Best Practices

When analyzing iOS applications:

- Store credentials only in the Keychain
- Never hardcode secrets
- Enforce strong password policies
- Encrypt sensitive application data
- Use Secure Enclave whenever possible
- Avoid plaintext storage
- Remove unused credentials
- Rotate exposed passwords
- Perform regular security assessments
- Automate repetitive security testing

---

# 📈 Skills Developed

After completing this lab, you will have practical experience with:

- iOS Filesystem Analysis
- Keychain Analysis
- Python Security Tool Development
- Password Auditing
- Secure Storage Assessment
- Mobile Application Security
- Batch Processing
- Security Automation
- Risk Assessment
- Professional Security Reporting

---

# 🎓 Learning Outcomes

Upon successful completion of this lab, you will be able to:

- Understand the iOS filesystem structure
- Navigate Keychain storage locations
- Build Python-based extraction tools
- Parse and analyze Keychain data
- Identify weak passwords and exposed secrets
- Generate JSON and HTML reports
- Automate mobile security assessments
- Compare multiple applications using batch processing
- Produce executive-level security reports

---

# 📚 Key Takeaways

- The iOS Keychain is designed to securely store sensitive credentials, but improper implementation can still expose valuable data.
- Weak passwords remain one of the most common mobile security issues.
- Automated analysis significantly improves the speed and consistency of security assessments.
- Batch processing enables scalable analysis across multiple applications.
- Well-structured reports help communicate technical findings and remediation guidance effectively.

---

# 🚀 Next Labs

Continue expanding your mobile application security skills with:

- 📱 iOS Application Reverse Engineering
- 🔍 Dynamic Application Analysis
- 🧩 Frida Runtime Instrumentation
- 🔐 SSL Pinning Bypass
- 📡 Mobile Traffic Interception
- 🛡 Secure Enclave Analysis
- 🔓 iOS Runtime Manipulation
- ⚙️ Objection Framework
- 📦 IPA Static Analysis
- 🤖 Mobile Security Automation

---

# ⚠ Disclaimer

This repository is intended **solely for educational purposes, cybersecurity training, and authorized security assessments**.

Only perform the techniques demonstrated in this lab on systems, applications, and devices for which you have explicit authorization. Unauthorized testing or access is illegal and unethical.

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- 📚 Adding new labs
- 🐛 Fixing bugs
- 📝 Improving documentation
- 🛠 Enhancing Python automation
- 🔍 Adding new security checks
- 📊 Improving report generation
- 🚀 Optimizing batch analysis

---

# ⭐ Support

If you found this repository useful:

- ⭐ Star the repository
- 🍴 Fork the repository
- 📢 Share it with the cybersecurity community
- 🤝 Contribute to future improvements

---

<div align="center">

# 📱 Master iOS Filesystem & Keychain Security Through Hands-on Practice

### 🚀 Happy Hacking & Keep Learning!

</div>

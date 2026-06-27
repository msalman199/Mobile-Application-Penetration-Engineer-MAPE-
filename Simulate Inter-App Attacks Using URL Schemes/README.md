# 📱 Analyze iOS Application Bundle and Property Lists

<div align="center">

# 🚀 Mobile Application Penetration Testing 

### iOS Bundle Analysis • Property List Inspection • Python Automation • Mobile Security Assessment

![Platform](https://img.shields.io/badge/Platform-iOS-black?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Mobile%20Security-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-App%20Bundle-success?style=for-the-badge)
![Environment](https://img.shields.io/badge/Linux-Ubuntu%2022.04-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Lab-Hands--On-brightgreen?style=for-the-badge)

</div>

---

# 📖 Overview

This hands-on lab introduces students to the internal structure of an **iOS Application Bundle** and demonstrates how penetration testers analyze **Property List (plist)** files during mobile application security assessments.

Students will build a simulated iOS application bundle, inspect application metadata, identify insecure configurations, automate bundle analysis using Python, and prepare professional security assessment reports.

The exercises simulate the techniques used by mobile security professionals to evaluate iOS applications without requiring a physical iPhone.

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

- 📱 Understand the iOS Application Bundle structure
- 📄 Analyze Info.plist files
- 🔍 Inspect Property List (plist) files
- 🏷 Extract application metadata
- 🔐 Identify insecure application configurations
- 🐍 Automate bundle analysis using Python
- 📊 Generate security assessment reports
- 🛡 Detect common mobile application weaknesses
- ⚙ Understand application resources and configuration files
- 📑 Produce professional penetration testing documentation

---

# 🧠 Skills You Will Gain

- Mobile Application Penetration Testing
- Static Mobile Analysis
- iOS Bundle Analysis
- Property List Inspection
- Python Automation
- Metadata Extraction
- Configuration Analysis
- Security Reporting
- Linux Administration
- Mobile Security Research

---

# 🛠 Technologies Used

## Mobile Platform

- iOS

## Operating System

- Ubuntu 22.04

## Programming Languages

- Python 3.10+
- Bash

## File Formats

- Property List (plist)
- XML
- JSON

## Python Libraries

- plistlib
- pathlib
- json
- os
- datetime

---

# 📚 Prerequisites

Before starting this lab, students should have:

- Basic Linux command-line knowledge
- Basic Python programming experience
- Understanding of XML syntax
- Familiarity with mobile application security
- Knowledge of directory structures

---

# 🖥 Lab Environment

The lab uses a preconfigured Ubuntu Linux virtual machine containing:

- Python 3.10+
- Tree
- Pip
- XML utilities
- JSON tools
- Linux command-line utilities

---

# 🏗 Lab Architecture

```text
                 Ubuntu Linux
                       │
                       ▼
          Simulated iOS Application
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
     App Bundle     Info.plist    Resources
         │
         ▼
 Python Bundle Analyzer
         │
         ▼
 Metadata Extraction
         │
         ▼
 Security Assessment
         │
         ▼
 JSON & HTML Reports
```

---

# 📂 Project Structure

```text
ios-bundle-analysis/
│
├── SampleApp.app/
│   ├── Info.plist
│   ├── embedded.mobileprovision
│   ├── PkgInfo
│   ├── Assets/
│   ├── Frameworks/
│   ├── Resources/
│   └── Config/
│
├── bundle_analyzer.py
├── plist_parser.py
├── metadata_report.py
│
├── reports/
└── logs/
```

---

# 🚀 Task 1 — Create a Simulated iOS Application Bundle

---

# 🎯 Objective

Create a realistic iOS application bundle that will be analyzed throughout this lab.

The bundle will contain application metadata, configuration files, and supporting resources similar to those found inside real iOS applications.

---

## Step 1 — Create the Working Directory

```bash
mkdir -p ~/ios-bundle-analysis

cd ~/ios-bundle-analysis
```

---

## Step 2 — Create the Application Bundle

```bash
mkdir -p SampleApp.app

mkdir -p SampleApp.app/{Resources,Frameworks,Assets,Config}
```

---

## Step 3 — Verify Directory Structure

```bash
tree SampleApp.app
```

---

### ✅ Expected Output

```text
SampleApp.app

├── Assets

├── Config

├── Frameworks

└── Resources
```

---

# 📁 Understanding the Bundle Structure

| Directory | Purpose |
|------------|----------|
| Assets | Images, icons, and media files |
| Config | Application configuration files |
| Frameworks | Embedded third-party frameworks |
| Resources | Localization and application resources |

---

# 🚀 Step 4 — Create the Info.plist File

Create the primary application metadata file.

```bash
cat > SampleApp.app/Info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"

"http://www.apple.com/DTDs/PropertyList-1.0.dtd">

<plist version="1.0">

<dict>

<key>CFBundleIdentifier</key>

<string>com.example.sampleapp</string>

<key>CFBundleName</key>

<string>SampleApp</string>

<key>CFBundleVersion</key>

<string>1.0</string>

<key>MinimumOSVersion</key>

<string>15.0</string>

<key>NSCameraUsageDescription</key>

<string>Camera access required</string>

</dict>

</plist>
EOF
```

---

# 📄 Info.plist Overview

The **Info.plist** file stores essential metadata used by iOS to identify and configure an application.

Common fields include:

| Key | Description |
|------|-------------|
| CFBundleIdentifier | Unique application identifier |
| CFBundleName | Application name |
| CFBundleVersion | Application version |
| MinimumOSVersion | Minimum supported iOS version |
| NSCameraUsageDescription | Camera permission description |

---

# 🚀 Step 5 — Create Additional Property List Files

Create an application configuration file.

```bash
cat > SampleApp.app/Config/AppConfig.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>

<plist version="1.0">

<dict>

<key>APIEndpoint</key>

<string>https://api.example.com</string>

<key>Environment</key>

<string>Production</string>

<key>EnableLogging</key>

<true/>

</dict>

</plist>
EOF
```

---

Create a preferences file.

```bash
cat > SampleApp.app/Config/Preferences.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>

<plist version="1.0">

<dict>

<key>Theme</key>

<string>Dark</string>

<key>NotificationsEnabled</key>

<true/>

<key>AutoLogin</key>

<false/>

</dict>

</plist>
EOF
```

---

# 📊 Property Lists Created

The simulated application now contains multiple plist files for analysis.

| File | Purpose |
|------|----------|
| Info.plist | Application metadata |
| AppConfig.plist | Application configuration |
| Preferences.plist | User preferences |

---

# 🚀 Step 6 — Install Required Tools

Update the package repository.

```bash
sudo apt update
```

Install required packages.

```bash
sudo apt install -y python3 python3-pip tree libxml2-utils
```

Verify Python installation.

```bash
python3 --version
```

Verify XML tools.

```bash
xmllint --version
```

---

# 📦 Installed Components

| Tool | Purpose |
|------|----------|
| Python 3 | Automation |
| Pip | Package Management |
| Tree | Directory Visualization |
| xmllint | XML Validation |

---

# 🎉 Part 1 Complete

You have successfully:

- ✅ Created a simulated iOS application bundle
- ✅ Built the application directory structure
- ✅ Created an Info.plist file
- ✅ Added additional Property List configuration files
- ✅ Installed the required tools
- ✅ Prepared the environment for automated bundle analysis

---

➡️ **Next:** **Part 2** covers:

- 📄 Parsing Info.plist Files
- 🐍 Building a Python Property List Parser
- 🏷 Extracting Application Metadata
- 🔍 Detecting Insecure Configurations
- 📊 Generating Automated Analysis Reports

- # 🚀 Task 2 — Analyze Info.plist and Property List Files

---

# 🎯 Objective

The goal of this task is to inspect the contents of an iOS application bundle, extract important metadata from **Property List (plist)** files, identify insecure configurations, and automate the analysis using Python.

Property List files contain valuable information that security professionals use during static mobile application assessments.

---

# 📄 What is a Property List?

A **Property List (plist)** is an XML or binary file used by iOS applications to store structured data such as:

- Application Metadata
- Configuration Settings
- User Preferences
- Feature Flags
- Permission Descriptions
- API Endpoints
- Bundle Information

Understanding these files helps identify application behavior and potential security issues.

---

# 📊 Analysis Workflow

```text
Locate Bundle
      │
      ▼
Locate Property Lists
      │
      ▼
Parse XML Files
      │
      ▼
Extract Metadata
      │
      ▼
Analyze Security Settings
      │
      ▼
Generate Reports
```

---

# 🛠 Step 1 — Create the Property List Parser

Create the following file.

```text
plist_parser.py
```

---

# 📦 Parser Responsibilities

The parser will automatically:

- Discover Property List files
- Parse XML content
- Read application metadata
- Display configuration values
- Export JSON results

---

# 🧩 Parser Architecture

```text
PlistParser
│
├── __init__()
├── discover_plists()
├── parse_plist()
├── extract_metadata()
├── export_json()
└── run()
```

---

# 🔍 Discover Property List Files

The parser recursively searches for files ending in:

```
*.plist
```

Typical files include:

```
Info.plist

AppConfig.plist

Preferences.plist
```

---

# 📖 Parse XML Files

The parser should validate and read each Property List before extracting values.

Useful Python module:

```python
plistlib
```

---

# 📄 Metadata to Extract

For each plist file, extract information such as:

- Bundle Identifier
- Application Name
- Version
- Minimum iOS Version
- Supported Permissions
- Configuration Options
- Feature Flags

---

# ▶ Execute the Parser

```bash
python3 plist_parser.py SampleApp.app/
```

---

# ✅ Expected Output

```text
Found Property Lists : 3

Metadata Extracted : Success

Configuration Parsed : Success

JSON Report Created
```

---

# 📄 Example JSON Output

```json
{
    "application":"SampleApp",
    "bundle_identifier":"com.example.sampleapp",
    "version":"1.0",
    "minimum_ios":"15.0"
}
```

---

# 🚀 Task 3 — Build the Bundle Analyzer

---

# 🎯 Objective

The Bundle Analyzer combines information from every Property List file and performs a security review of the application configuration.

Instead of manually reviewing multiple files, Python automates the entire process.

---

# 📊 Bundle Analysis Workflow

```text
Application Bundle
        │
        ▼
Locate plist Files
        │
        ▼
Extract Metadata
        │
        ▼
Analyze Configuration
        │
        ▼
Identify Security Issues
        │
        ▼
Generate Report
```

---

# 🛠 Step 1 — Create the Analyzer

Create

```text
bundle_analyzer.py
```

---

# 📦 Analyzer Responsibilities

The analyzer performs:

- Bundle Inspection
- Metadata Collection
- Configuration Analysis
- Permission Analysis
- Risk Classification
- Security Recommendations
- JSON Report Generation
- HTML Dashboard Generation

---

# 🧩 Class Design

```text
BundleAnalyzer
│
├── __init__()
├── scan_bundle()
├── analyze_permissions()
├── analyze_configuration()
├── classify_risk()
├── generate_report()
└── generate_html_dashboard()
```

---

# 🔍 Analyze Bundle Metadata

The analyzer reviews important application properties including:

- Bundle Identifier
- Version
- Build Number
- Minimum iOS Version
- Executable Name
- Display Name

---

# 🔐 Analyze Permission Usage

Permission descriptions provide insight into sensitive application capabilities.

Common permission keys include:

```
NSCameraUsageDescription

NSLocationWhenInUseUsageDescription

NSMicrophoneUsageDescription

NSPhotoLibraryUsageDescription

NSContactsUsageDescription
```

---

# ⚙ Analyze Configuration Files

Configuration files are checked for:

- Debug settings
- Logging enabled
- Hardcoded API endpoints
- Feature flags
- Environment settings

---

# 🔍 Detect Insecure Configurations

Examples of security findings include:

- Debug mode enabled
- Logging enabled in production
- Missing permission descriptions
- Weak configuration settings
- Development endpoints
- Insecure feature flags

---

# 📊 Risk Classification

| Risk Level | Description |
|------------|-------------|
| 🔴 High | Critical security issue |
| 🟠 Medium | Potential weakness |
| 🟢 Low | Secure implementation |

---

# 📈 Executive Summary

The analyzer generates a summary including:

- Files analyzed
- Metadata extracted
- Permissions discovered
- Configuration findings
- Overall application risk

---

# 💡 Security Recommendations

Typical recommendations include:

- Disable debug logging
- Remove unnecessary permissions
- Secure configuration files
- Use production API endpoints
- Minimize sensitive metadata exposure
- Validate permission usage

---

# 🌐 HTML Dashboard

In addition to JSON reports, the analyzer creates an HTML dashboard showing:

- Application Overview
- Bundle Metadata
- Permission Summary
- Security Findings
- Risk Rating
- Recommendations

---

# ▶ Execute the Bundle Analyzer

Create the reports directory.

```bash
mkdir -p reports
```

Run the analyzer.

```bash
python3 bundle_analyzer.py SampleApp.app/ -o reports/
```

---

# 📂 Review Generated Reports

```bash
ls -la reports/
```

Display the JSON report.

```bash
cat reports/bundle_report.json | python3 -m json.tool
```

---

# 🌍 View HTML Report

Open the HTML report in a browser.

```bash
firefox reports/bundle_report.html
```

Or inspect the source.

```bash
cat reports/bundle_report.html
```

---

# 📊 Expected Security Findings

The analyzer may identify:

- Debug logging enabled
- Hardcoded API endpoints
- Missing permission descriptions
- Insecure configuration values
- Development settings left enabled
- Excessive application permissions

---

# 🎯 Skills Developed

During this section you learned how to:

- ✅ Parse Property List files
- ✅ Extract application metadata
- ✅ Build a Python plist parser
- ✅ Analyze application configurations
- ✅ Review permission usage
- ✅ Detect insecure settings
- ✅ Generate JSON security reports
- ✅ Produce HTML assessment dashboards

---

# 🎉 Part 2 Complete

You have successfully:

- 📄 Built a Python Property List parser
- 🏷 Extracted application metadata
- 🔍 Automated bundle analysis
- 🔐 Reviewed application permissions
- ⚙ Evaluated configuration files
- 📊 Generated JSON reports
- 🌐 Created HTML security dashboards
- 🛡 Applied static analysis techniques used in professional iOS application security assessments

---

➡️ **Next:** **Part 3** covers:

- 📊 Advanced Security Assessment
- 📄 Report Generation
- ✅ Lab Verification
- 🛠 Troubleshooting Guide
- 📈 Expected Outcomes
- 🎓 Learning Summary
- 🔒 Security Best Practices
- 🤝 Contributing
- ⭐ Support
```
# 🚀 Task 4 — Generate Security Assessment Reports

---

# 🎯 Objective

The final stage of the assessment is transforming collected metadata into meaningful security findings and producing professional reports suitable for penetration testing engagements.

This task automates report generation, summarizes discovered issues, classifies security risks, and prepares documentation for remediation.

---

# 📊 Reporting Workflow

```text
Bundle Analysis
       │
       ▼
Collect Findings
       │
       ▼
Classify Risks
       │
       ▼
Generate JSON Report
       │
       ▼
Generate HTML Dashboard
       │
       ▼
Create Executive Summary
```

---

# 🛠 Step 1 — Create the Report Generator

Create the following file.

```text
metadata_report.py
```

---

# 📦 Report Generator Responsibilities

The report generator should:

- Read analysis results
- Summarize application metadata
- Classify security findings
- Assign risk levels
- Generate remediation guidance
- Export JSON reports
- Generate HTML dashboards
- Produce executive summaries

---

# 🧩 Report Generator Architecture

```text
MetadataReport
│
├── __init__()
├── load_analysis()
├── summarize_metadata()
├── summarize_findings()
├── generate_recommendations()
├── export_json()
├── export_html()
└── run()
```

---

# 📋 Executive Summary

The generated report should summarize:

- Application Name
- Bundle Identifier
- Version
- Number of Property Lists
- Permissions Detected
- Configuration Files
- Security Findings
- Overall Risk Rating

---

# 🔍 Security Findings

Common findings include:

- Debug logging enabled
- Development API endpoints
- Hardcoded URLs
- Missing permission descriptions
- Insecure configuration values
- Excessive application permissions

---

# 📊 Risk Classification

| Risk | Description |
|------|-------------|
| 🔴 High | Critical security issue requiring immediate attention |
| 🟠 Medium | Security weakness that should be addressed |
| 🟢 Low | Informational finding or secure implementation |

---

# 💡 Example Recommendations

Recommendations may include:

- Disable debug logging in production builds
- Remove unused permissions
- Secure sensitive configuration files
- Replace development endpoints with production services
- Minimize metadata exposure
- Encrypt sensitive application data
- Review third-party frameworks
- Regularly audit Property List files

---

# ▶ Execute the Report Generator

Create the reports directory.

```bash
mkdir -p reports
```

Run the report generator.

```bash
python3 metadata_report.py reports/bundle_report.json
```

---

# 📂 Review Generated Reports

```bash
ls -la reports/
```

Pretty-print the JSON report.

```bash
cat reports/security_summary.json | python3 -m json.tool
```

Open the HTML dashboard.

```bash
firefox reports/security_dashboard.html
```

---

# 📑 Example Executive Summary

```text
Application : SampleApp

Bundle Identifier : com.example.sampleapp

Version : 1.0

Property Lists : 3

Security Findings : 5

Overall Risk : Medium

Recommendations : 6
```

---

# 📂 Generated Reports

```text
reports/

├── bundle_report.json

├── security_summary.json

├── security_dashboard.html

└── executive_summary.txt
```

---

# ✅ Lab Verification

---

# 🎯 Verification Checklist

Verify that all required lab components have been completed successfully.

- ✅ Simulated application bundle created
- ✅ Property List files parsed
- ✅ Metadata extracted
- ✅ Bundle analyzed
- ✅ Security findings generated
- ✅ JSON report exported
- ✅ HTML dashboard created
- ✅ Executive summary generated

---

# Verify Project Structure

```bash
tree ios-bundle-analysis
```

---

# Expected Structure

```text
ios-bundle-analysis/

├── SampleApp.app/

│   ├── Assets/

│   ├── Config/

│   ├── Frameworks/

│   ├── Resources/

│   └── Info.plist

├── plist_parser.py

├── bundle_analyzer.py

├── metadata_report.py

├── reports/

└── logs/
```

---

# Verify Reports

```bash
ls -la reports/
```

Validate JSON.

```bash
python3 -m json.tool reports/security_summary.json
```

---

# 🛠 Troubleshooting Guide

---

## ❌ XML Parsing Errors

### Symptoms

```
XML parsing failed
```

### Solution

Validate the Property List.

```bash
xmllint SampleApp.app/Info.plist
```

Check file formatting.

```bash
cat SampleApp.app/Info.plist
```

---

## ❌ Missing Property Lists

Verify the application bundle.

```bash
find SampleApp.app -name "*.plist"
```

Expected output.

```text
Info.plist

Config/AppConfig.plist

Config/Preferences.plist
```

---

## ❌ Python Import Errors

Verify Python version.

```bash
python3 --version
```

Check syntax.

```bash
python3 -m py_compile plist_parser.py

python3 -m py_compile bundle_analyzer.py

python3 -m py_compile metadata_report.py
```

---

## ❌ Reports Not Generated

Verify output directory.

```bash
mkdir -p reports
```

Run the analyzer again.

```bash
python3 bundle_analyzer.py SampleApp.app/ -o reports/
```

---

# 🔒 Security Best Practices

When reviewing iOS application bundles:

- Remove unused permissions
- Avoid hardcoded secrets
- Disable debug logging in production
- Minimize exposed metadata
- Store sensitive data securely
- Validate all configuration files
- Remove development endpoints before release
- Regularly audit Property List files
- Review embedded frameworks
- Perform continuous security testing

---

# 📈 Skills Developed

After completing this lab, you will have practical experience with:

- iOS Application Bundle Analysis
- Property List Inspection
- Static Mobile Application Analysis
- Python Automation
- Metadata Extraction
- Configuration Review
- Security Assessment
- Risk Classification
- Report Generation
- Professional Documentation

---

# 🎓 Learning Outcomes

After completing this lab, you will be able to:

- Understand the structure of an iOS application bundle
- Analyze Info.plist and supporting Property List files
- Extract application metadata using Python
- Identify insecure application configurations
- Evaluate permission usage
- Generate professional security reports
- Produce HTML dashboards and executive summaries
- Apply static analysis techniques used in real-world mobile application penetration testing

---

# 📚 Key Takeaways

- Property List files contain critical application metadata that should be reviewed during every iOS security assessment.
- Misconfigured permissions and insecure configuration values can significantly increase application risk.
- Automating metadata extraction improves consistency and reduces manual effort.
- Executive summaries help communicate technical findings to developers and stakeholders.
- Static analysis is an essential phase of every professional mobile application penetration test.

---

# 🚀 Next Labs

Continue your Mobile Application Penetration Testing journey with:

- 📱 iOS Filesystem Analysis
- 🔐 Keychain Secrets Analysis
- 📦 IPA Reverse Engineering
- 🔍 Dynamic Application Analysis
- 🧩 Frida Runtime Instrumentation
- ⚙️ Objection Framework
- 🌐 Mobile API Security Testing
- 🔓 SSL Pinning Bypass
- 📡 Traffic Interception with Burp Suite
- 🤖 Mobile Security Automation

---

# ⚠ Disclaimer

This lab is provided **solely for educational purposes, cybersecurity training, and authorized security assessments**.

Only perform the techniques demonstrated in this repository on systems and applications for which you have explicit authorization. Unauthorized testing or access is illegal and unethical.

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- 📚 Adding new mobile security labs
- 🛠 Improving automation scripts
- 🐛 Reporting and fixing bugs
- 📝 Enhancing documentation
- 📊 Improving reporting capabilities
- 🚀 Optimizing analysis workflows

---

# ⭐ Support

If you found this repository helpful:

- ⭐ Star the repository
- 🍴 Fork the repository
- 📢 Share it with the cybersecurity community
- 🤝 Contribute to future improvements

---

<div align="center">

# 📱 Master iOS Application Bundle Analysis Through Hands-on Practice

### 🚀 Happy Hacking & Keep Learning!

</div>

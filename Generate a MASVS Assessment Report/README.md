# 📱 Generate a MASVS Assessment Report

> **CMAPE Lab Series — Mobile Application Security Assessment**

---

<div align="center">

# 📱 Generate a MASVS Assessment Report

### 🛡️ OWASP MASVS • Android Security Assessment • APK Analysis • Python Automation

Build an automated **OWASP Mobile Application Security Verification Standard (MASVS)** assessment framework to analyze Android applications, perform static security testing, and generate professional security assessment reports.

---

## 🛠️ Technology Stack

![OWASP MASVS](https://img.shields.io/badge/OWASP-MASVS-red?style=for-the-badge\&logo=owasp)
![Android](https://img.shields.io/badge/Android-Security-3DDC84?style=for-the-badge\&logo=android)
![APKTool](https://img.shields.io/badge/APKTool-Decompiler-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu)
![JSON](https://img.shields.io/badge/JSON-Reports-black?style=for-the-badge)
![Markdown](https://img.shields.io/badge/Markdown-Documentation-black?style=for-the-badge\&logo=markdown)
![HTML](https://img.shields.io/badge/HTML-Reporting-orange?style=for-the-badge\&logo=html5)
![Jinja2](https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge)
![XML](https://img.shields.io/badge/XML-Parsing-blue?style=for-the-badge)

</div>

---

# 📖 Overview

The **OWASP Mobile Application Security Verification Standard (MASVS)** is the industry-standard framework for assessing mobile application security. It provides a structured methodology for evaluating Android and iOS applications across multiple security domains.

In this lab, you will learn how to automate MASVS assessments by combining **APKTool**, **Python**, **XML parsing**, **JSON reporting**, and **Markdown report generation**. By the end of the exercise, you will have developed a reusable assessment framework capable of producing professional security reports suitable for penetration testing engagements and compliance documentation.

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

* ✅ Understand the OWASP MASVS framework
* ✅ Perform static analysis of Android APK files
* ✅ Build Python-based assessment tools
* ✅ Parse AndroidManifest.xml automatically
* ✅ Evaluate common Android security configurations
* ✅ Generate structured JSON assessment results
* ✅ Produce professional Markdown security reports
* ✅ Prepare assessment artifacts for distribution
* ✅ Understand compliance verification workflows

---

# 📚 Prerequisites

Before beginning this lab, ensure you have the following knowledge:

* 🐍 Basic Python programming
* 📱 Android application architecture
* 🐧 Linux command-line usage
* 🔐 Basic security assessment concepts
* 📝 Markdown syntax
* 📦 Basic understanding of APK files

---

# 🖥️ Lab Environment

Your cloud machine already contains everything required for the assessment.

### Included Software

* 🐧 Ubuntu Linux
* ☕ OpenJDK 11
* 🐍 Python 3
* 📦 APKTool
* 📄 Jinja2
* 📑 xmltodict
* 📱 Sample vulnerable Android APK
* 🔍 Static analysis utilities

---

# 📂 Lab Architecture

```text
                Android APK
                     │
                     ▼
             APKTool Decompile
                     │
                     ▼
        AndroidManifest.xml Analysis
                     │
                     ▼
          Python Assessment Engine
                     │
                     ▼
          JSON Assessment Results
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
 Markdown Report         HTML Report
          │                     │
          └──────────┬──────────┘
                     ▼
            Distribution Package
```

---

# 🧪 Task 1 — Set Up the MASVS Assessment Environment

---

# 🔹 Step 1.1 — Install Required Software

Prepare the operating system and install all required dependencies.

```bash
# Update packages
sudo apt update

# Install required software
sudo apt install -y \
python3 \
python3-pip \
python3-venv \
openjdk-11-jdk \
wget \
unzip
```

---

### 📁 Create Working Directory

```bash
mkdir -p ~/masvs-lab

cd ~/masvs-lab
```

---

### 🐍 Create Python Virtual Environment

```bash
python3 -m venv masvs-env
```

Activate it:

```bash
source masvs-env/bin/activate
```

---

### 📦 Install Python Packages

```bash
pip install jinja2 xmltodict
```

Expected output:

```text
Successfully installed

jinja2
xmltodict
```

---

# ✅ Verification

Check installed packages.

```bash
pip list
```

Expected:

```text
Jinja2

xmltodict

pip

setuptools
```

---

# 🔹 Step 1.2 — Install APK Analysis Tools

The primary tool used for Android static analysis is **APKTool**.

Download APKTool.

```bash
wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool

wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.7.0.jar
```

Make the script executable.

```bash
chmod +x apktool
```

Install APKTool.

```bash
sudo mv apktool /usr/local/bin/

sudo mv apktool_2.7.0.jar /usr/local/bin/apktool.jar
```

---

### ✅ Verify Installation

```bash
apktool --version
```

Example:

```text
2.7.0
```

---

# 🔹 Step 1.3 — Download the Sample Application

Create a directory for APK samples.

```bash
mkdir -p ~/masvs-lab/sample-apps

cd ~/masvs-lab/sample-apps
```

Download the vulnerable Android application.

```bash
wget https://github.com/payatu/diva-android/raw/master/diva-beta.apk
```

---

### Verify the APK

```bash
file diva-beta.apk
```

Expected output:

```text
diva-beta.apk:

Android application package
```

---

# 📁 Directory Structure

After completing Task 1, your workspace should resemble:

```text
masvs-lab/

├── masvs-env/

├── sample-apps/

│   └── diva-beta.apk

├── analysis/

└── reports/
```

---

# 💡 Why This Matters

A well-prepared assessment environment ensures:

* ✔ Consistent testing
* ✔ Repeatable assessments
* ✔ Reliable reporting
* ✔ Easy automation
* ✔ CI/CD compatibility
* ✔ Professional documentation

---

# 🎯 Task 1 Summary

You have successfully:

* ✅ Installed all required Linux dependencies
* ✅ Configured Python virtual environment
* ✅ Installed Jinja2 and XML libraries
* ✅ Installed APKTool
* ✅ Downloaded the vulnerable Android application
* ✅ Prepared the workspace for automated MASVS assessments

---

## ⏭️ Next Part

In **Part 2**, you will:

* 📦 Decompile the Android APK
* 🔍 Analyze AndroidManifest.xml
* 🛡️ Build the MASVS Assessment Framework
* 🐍 Develop Python classes for automated security testing
* 📊 Generate structured assessment results

# 🛡️ Task 2 — Decompile and Analyze the Android APK

> **CMAPE Lab Series — Generate a MASVS Assessment Report**

---

# 🎯 Objective

In this task, you will extract the contents of an Android APK, inspect its internal structure, analyze important security-related files, and prepare the application for an automated **OWASP MASVS** assessment.

---

# 🔍 Step 2.1 — Create Analysis Workspace

Create a dedicated directory for decompiled applications.

```bash
mkdir -p ~/masvs-lab/analysis

cd ~/masvs-lab/analysis
```

---

# 📦 Step 2.2 — Decompile the APK

Use **APKTool** to extract the application's resources and configuration files.

```bash
apktool d ~/masvs-lab/sample-apps/diva-beta.apk \
-o diva-decompiled
```

Expected output:

```text
I: Using Apktool...
I: Decoding AndroidManifest.xml...
I: Loading resource table...
I: Decoding resources...
I: Copying assets...
I: Copying unknown files...
I: Copying original files...
```

---

# 📂 Step 2.3 — Explore the Decompiled Project

Navigate into the extracted project.

```bash
cd diva-decompiled
```

Display the directory contents.

```bash
ls -la
```

Example structure:

```text
AndroidManifest.xml
apktool.yml
assets/
lib/
original/
res/
smali/
unknown/
```

---

# 📄 Step 2.4 — Inspect the Android Manifest

Display the beginning of the manifest.

```bash
cat AndroidManifest.xml | head -20
```

The manifest contains critical security information including:

* 📱 Application package name
* 🔐 Permissions
* 🚀 Activities
* 🔧 Services
* 📡 Broadcast Receivers
* 🗂 Content Providers
* ⚙ Application configuration

---

# 🔎 Step 2.5 — Review Application Permissions

Extract all requested permissions.

```bash
grep "uses-permission" AndroidManifest.xml
```

Example:

```xml
<uses-permission android:name="android.permission.INTERNET"/>

<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>

<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```

---

# 🛡️ Step 2.6 — Check Security Flags

Inspect important application configuration flags.

```bash
grep "android:debuggable\|android:allowBackup" AndroidManifest.xml
```

Potential findings:

```xml
android:debuggable="true"

android:allowBackup="true"
```

These settings may indicate security weaknesses depending on the application's deployment environment.

---

# 📁 Step 2.7 — Review Application Resources

Display available resources.

```bash
ls -la res/
```

Typical output:

```text
drawable/

layout/

menu/

values/

xml/

mipmap/
```

---

# ✅ Task 2 Summary

You have successfully:

* ✔ Decompiled an Android APK
* ✔ Extracted AndroidManifest.xml
* ✔ Reviewed application permissions
* ✔ Identified important security flags
* ✔ Explored the resource structure
* ✔ Prepared the application for automated assessment

---

# 🛠️ Task 3 — Create the MASVS Assessment Framework

---

# 🎯 Objective

Develop a reusable Python framework capable of performing automated MASVS security assessments and storing structured findings.

---

# 📁 Step 3.1 — Create the Assessment Framework

Create the framework source file.

```bash
cd ~/masvs-lab

nano masvs_framework.py
```

---

# 🏗️ Build the Assessment Class

Create a reusable Python class named:

```python
class MASVSAssessment:
```

The class should manage:

* 📋 Assessment metadata
* 📊 Test results
* 📈 Statistics
* 📝 Reporting data

---

## 🔹 Initialize Assessment

Inside the constructor:

* Store APK path
* Store application name
* Record assessment date
* Create empty results dictionary
* Initialize MASVS categories

Suggested categories:

```text
V1

V2

V3

V4

V5

V6

V7

V8
```

Each category should maintain:

* Tests
* Passed count
* Failed count
* Not Applicable count

---

# 🔹 Implement add_test_result()

Create a method that records each assessment result.

It should store:

* Test ID
* Description
* Status
* Details

It should also update summary counters automatically.

---

# 🔹 Implement get_summary()

Generate assessment statistics including:

* Total tests
* Passed tests
* Failed tests
* Not Applicable tests
* Pass percentage

The function should return a structured dictionary suitable for JSON serialization.

---

# 🔍 Step 3.2 — Implement Security Checks

Create helper functions for static analysis.

---

## 📄 Check Manifest Permissions

Implement:

```python
check_manifest_permissions()
```

The function should:

* Parse AndroidManifest.xml
* Enumerate all permissions
* Compare them against dangerous Android permissions
* Return detected permissions

Dangerous examples include:

* CAMERA
* READ_CONTACTS
* ACCESS_FINE_LOCATION
* READ_EXTERNAL_STORAGE
* WRITE_EXTERNAL_STORAGE

---

## 🐞 Check Debug Configuration

Implement:

```python
check_debug_flag()
```

The function should determine whether:

```xml
android:debuggable="true"
```

is present.

---

## 💾 Check Backup Configuration

Implement:

```python
check_backup_flag()
```

Verify whether:

```xml
android:allowBackup="true"
```

is enabled.

---

# 📄 Step 3.3 — Create the Assessment Driver

Create the execution script.

```bash
nano perform_assessment.py
```

---

# ⚙ Configure Assessment Workflow

The script should:

* Import the assessment framework
* Locate APK files
* Locate AndroidManifest.xml
* Initialize MASVSAssessment
* Execute every assessment category
* Collect findings
* Produce summary statistics

---

# 🛡️ Implement MASVS Categories

Evaluate all eight MASVS domains:

| Category | Description                            |
| -------- | -------------------------------------- |
| 🏗 V1    | Architecture, Design & Threat Modeling |
| 💾 V2    | Data Storage & Privacy                 |
| 🔑 V3    | Cryptography                           |
| 🔐 V4    | Authentication & Session Management    |
| 🌐 V5    | Network Communication                  |
| 📱 V6    | Platform Interaction                   |
| ⚙ V7     | Code Quality & Build Configuration     |
| 🔒 V8    | Resilience Against Reverse Engineering |

---

# 📊 Save Assessment Results

Export results as JSON.

Example:

```python
assessment_results.json
```

---

# ▶ Execute the Assessment

Activate the virtual environment.

```bash
source masvs-env/bin/activate
```

Run the assessment.

```bash
python3 perform_assessment.py
```

---

# 📑 View the Results

Pretty-print the generated JSON.

```bash
cat assessment_results.json | python3 -m json.tool | head -50
```

Example output:

```json
{
    "app_name": "DIVA",

    "assessment_date": "...",

    "summary": {

        "total_tests": 20,

        "passed": 15,

        "failed": 5,

        "pass_rate": 75
    }
}
```

---

# 🎯 Expected Outcome

By the end of Task 3 you will have:

* ✅ Developed a reusable MASVS assessment framework
* ✅ Parsed AndroidManifest.xml automatically
* ✅ Implemented multiple static security checks
* ✅ Evaluated all MASVS categories
* ✅ Generated structured JSON assessment results
* ✅ Created the foundation for professional reporting

---

# 🚀 Next Part

In **Part 3**, you will:

* 📝 Generate a professional Markdown assessment report
* 🌐 Create an HTML version of the report
* 📊 Build a complete executive summary
* 📈 Produce risk assessment matrices
* 📦 Package assessment artifacts for distribution
# 📑 Task 4 — Generate a Professional MASVS Assessment Report

> **CMAPE Lab Series — Generate a MASVS Assessment Report**

---

# 🎯 Objective

After completing the automated security assessment, the next step is transforming the collected findings into a **professional penetration testing report**. In this task, you will build a Python-based report generator that converts JSON assessment data into polished **Markdown** and **HTML** reports suitable for clients, auditors, and security teams.

---

# 📋 Step 4.1 — Create the Report Generator

Navigate to your working directory.

```bash
cd ~/masvs-lab
```

Create the report generation script.

```bash
nano report_generator.py
```

---

# 🐍 Build the Report Generator

Import the required Python modules.

```python
import json
from datetime import datetime
from jinja2 import Template
```

The generator should automate the complete reporting workflow.

---

# 📝 Implement `generate_markdown_report()`

Create a function that:

* 📂 Loads assessment JSON results
* 📊 Parses all MASVS categories
* 📝 Builds a Markdown report
* 💾 Saves the report to disk

Prototype:

```python
generate_markdown_report(results_file, output_file)
```

---

# 📖 Report Sections

Your report should contain the following professional sections.

---

## 📌 Executive Summary

Include:

* Application Name
* Assessment Date
* Overall Risk Rating
* MASVS Compliance Percentage
* Total Tests Executed
* Pass / Fail Statistics

Example:

```text
Application: DIVA

Assessment Date: 2026-06-27

Overall Compliance: 78%

Overall Risk: Medium
```

---

## 📌 Assessment Overview

Summarize:

* Assessment methodology
* Static analysis scope
* Tools used
* MASVS version
* APK analyzed

---

## 📌 Key Findings

Highlight the most significant discoveries.

Example:

* 🔴 Debug mode enabled
* 🔴 Backup allowed
* 🟠 Dangerous permissions requested
* 🟢 No hardcoded secrets detected

---

## 📌 Detailed MASVS Results

Create a section for every MASVS category.

Example:

```text
V1 Architecture

PASS

V2 Data Storage

FAIL

V3 Cryptography

PASS
```

Each category should include:

* Test ID
* Description
* Status
* Supporting evidence

---

## 📌 Risk Assessment Matrix

Create a visual summary.

| Severity         | Findings |
| ---------------- | -------: |
| 🔴 High          |        2 |
| 🟠 Medium        |        4 |
| 🟡 Low           |        6 |
| 🟢 Informational |        8 |

---

## 📌 Security Recommendations

Separate recommendations into priorities.

### 🔴 High Priority

* Disable Debug Mode
* Disable Backup
* Remove unnecessary permissions

---

### 🟠 Medium Priority

* Harden application configuration
* Review exported components
* Reduce attack surface

---

### 🟢 Low Priority

* Improve documentation
* Review build configuration
* Maintain secure development practices

---

## 📌 Compliance Status

Display the MASVS compliance summary.

Example:

```text
V1 ✅ PASS

V2 ❌ FAIL

V3 ✅ PASS

V4 N/A

V5 ✅ PASS

V6 N/A

V7 ❌ FAIL

V8 PASS
```

---

## 📌 Next Steps

Recommend follow-up activities such as:

* Dynamic analysis
* Penetration testing
* Secure code review
* Runtime instrumentation
* Manual verification

---

## 📌 Appendix

Include:

* Assessment timestamp
* Tool versions
* Framework version
* Analyst name
* Assessment environment

---

# 🖋 Render the Template

Use **Jinja2** to combine assessment data with the report template.

The generator should:

* Load JSON
* Render Markdown
* Save the report

Example output:

```text
MASVS_Assessment_Report.md
```

---

# 🌐 Step 4.2 — Generate an HTML Report

Implement:

```python
create_html_report()
```

The function should:

* Read the generated Markdown
* Wrap it inside HTML
* Apply basic CSS styling
* Save the final report

Output:

```text
MASVS_Assessment_Report.html
```

---

# ▶ Generate Reports

Execute the generator.

```bash
python3 report_generator.py
```

Expected output:

```text
Generating Markdown Report...

Generating HTML Report...

Report Created Successfully
```

---

# 👀 Review the Markdown Report

Open the report.

```bash
less MASVS_Assessment_Report.md
```

---

# 🌍 Open the HTML Report

Launch the report in a browser.

```bash
firefox MASVS_Assessment_Report.html &
```

---

# 📦 Step 4.3 — Create a Distribution Package

Create a packaging script.

```bash
nano package_report.py
```

---

# 📁 Package Assessment Artifacts

The packaging script should automatically collect:

* 📊 JSON Results
* 📝 Markdown Report
* 🌐 HTML Report

Copy them into a timestamped directory.

Example:

```text
MASVS_Assessment_20260627/
```

---

# 📄 Generate Package README

Automatically create a README file describing:

* Assessment Date
* Application Name
* Included Files
* Report Format
* Contact Information

---

# 🗜 Compress the Package

Generate a ZIP archive.

Example:

```text
MASVS_Assessment_Package_20260627.zip
```

---

# ▶ Execute Packaging

Run:

```bash
python3 package_report.py
```

Expected output:

```text
Packaging Assessment...

Copying Reports...

Creating ZIP Archive...

Package Created Successfully
```

---

# 📂 Package Structure

```text
MASVS_Assessment_Package/

├── assessment_results.json

├── MASVS_Assessment_Report.md

├── MASVS_Assessment_Report.html

└── README.md
```

---

# ✅ Expected Results

After completing this task, you should have successfully:

* ✔ Generated a professional Markdown report
* ✔ Produced an HTML security report
* ✔ Created an executive summary
* ✔ Documented assessment findings
* ✔ Organized results by MASVS category
* ✔ Produced a risk assessment matrix
* ✔ Added prioritized recommendations
* ✔ Packaged all deliverables into a ZIP archive

---

# 💡 Best Practices

For professional security reporting:

* 📑 Use consistent formatting
* 📊 Include clear statistics
* 📝 Write concise findings
* 🎯 Prioritize recommendations
* 🔒 Protect sensitive information
* 📦 Archive all assessment artifacts
* 📅 Timestamp every report
* 🧾 Maintain version history
* 📚 Reference MASVS controls
* ✔ Review reports before distribution

---

# 🚀 Next Part

In **Part 4**, you will:

* ✅ Validate assessment completeness
* 📊 Review failed security tests
* 📦 Verify distribution packages
* 🛠 Troubleshoot common issues
* 🎯 Review expected outcomes
* 📚 Explore MASVS best practices
* 🎓 Complete the lab with final recommendations and ethical guidance

# ✅ Task 5 — Validate and Review Assessment Results

> **CMAPE Lab Series — Generate a MASVS Assessment Report**

---

# 🎯 Objective

The final phase of the assessment process focuses on validating the generated artifacts, reviewing discovered security findings, verifying report completeness, and packaging all deliverables into a professional assessment bundle.

This stage ensures the assessment is:

* ✔ Accurate
* ✔ Complete
* ✔ Reproducible
* ✔ Ready for stakeholders
* ✔ Suitable for compliance reviews

---

# 🔍 Step 5.1 — Verify Assessment Completeness

Ensure all required files were successfully generated.

---

## 📄 Verify JSON Results

```bash
ls -la ~/masvs-lab/assessment_results.json
```

Expected:

```text
assessment_results.json
```

---

## 📝 Verify Markdown Report

```bash
ls -la ~/masvs-lab/MASVS_Assessment_Report.md
```

Expected:

```text
MASVS_Assessment_Report.md
```

---

## 🌐 Verify HTML Report

```bash
ls -la ~/masvs-lab/MASVS_Assessment_Report.html
```

Expected:

```text
MASVS_Assessment_Report.html
```

---

# 🔎 Validate JSON Structure

Run the following validation script.

```bash
python3 -c "
import json

with open('assessment_results.json','r') as f:
    data = json.load(f)

print(f'Application: {data[\"app_name\"]}')
print(f'Total Tests: {data[\"summary\"][\"total_tests\"]}')
print(f'Pass Rate: {data[\"summary\"][\"pass_rate\"]}%')
"
```

Example output:

```text
Application: DIVA

Total Tests: 24

Pass Rate: 79%
```

---

# 🔍 Step 5.2 — Review Security Findings

A security assessment is only useful if findings are properly analyzed.

---

## 🚨 Extract Failed Tests

Display all failed controls.

```bash
python3 -c "
import json

with open('assessment_results.json','r') as f:
    data = json.load(f)

print('FAILED TESTS:')

for category, results in data['results'].items():
    for test in results['tests']:
        if test['status'] == 'FAIL':
            print(f'{test[\"test_id\"]}: {test[\"description\"]}')
"
```

Example:

```text
FAILED TESTS:

V2-01: Dangerous Permissions Detected

V7-02: Debug Mode Enabled

V7-03: Backup Enabled
```

---

# 📊 Analyze Assessment Statistics

Review:

* 🟢 Passed Controls
* 🔴 Failed Controls
* 🟡 Informational Findings
* ⚪ Not Applicable Controls

Important metrics include:

| Metric      | Purpose                  |
| ----------- | ------------------------ |
| Total Tests | Assessment coverage      |
| Pass Count  | Compliance measurement   |
| Fail Count  | Security weaknesses      |
| Pass Rate   | Overall security posture |
| Risk Score  | Executive reporting      |

---

# 📦 Step 5.3 — Create Final Assessment Package

Package all assessment artifacts into a distributable archive.

---

## ▶ Execute Packaging Script

```bash
python3 package_report.py
```

Expected output:

```text
Collecting Assessment Files...

Creating Package Directory...

Generating README...

Creating ZIP Archive...

Package Successfully Created
```

---

## 📂 Verify Package Creation

```bash
ls -lh MASVS_Assessment_Package_*.zip
```

Example:

```text
MASVS_Assessment_Package_20260627.zip
```

---

## 📋 Inspect Archive Contents

```bash
unzip -l MASVS_Assessment_Package_*.zip
```

Expected:

```text
assessment_results.json

MASVS_Assessment_Report.md

MASVS_Assessment_Report.html

README.md
```

---

# 🎯 Expected Outcomes

Upon successful completion of this lab, you should have:

---

## 📱 Android Security Analysis

* ✅ Decompiled Android APKs
* ✅ Inspected AndroidManifest.xml
* ✅ Analyzed application permissions
* ✅ Identified insecure configurations

---

## 🐍 Python Security Automation

* ✅ Built a MASVS assessment framework
* ✅ Automated security checks
* ✅ Generated structured findings
* ✅ Produced JSON-based results

---

## 📑 Security Reporting

* ✅ Generated Markdown reports
* ✅ Generated HTML reports
* ✅ Created executive summaries
* ✅ Built risk assessment matrices

---

## 📦 Assessment Packaging

* ✅ Packaged all assessment artifacts
* ✅ Created reusable reporting workflows
* ✅ Prepared deliverables for distribution

---

# 🛠 Troubleshooting Guide

---

## ❌ APKTool Fails to Decompile

Verify Java installation.

```bash
java -version
```

Expected:

```text
OpenJDK 11
```

---

### Solution

```bash
sudo apt install openjdk-11-jdk
```

---

### Verify APK Integrity

```bash
file diva-beta.apk
```

Expected:

```text
Android application package
```

---

## ❌ Python Import Errors

Check virtual environment status.

```bash
which python3
```

Verify:

```bash
source masvs-env/bin/activate
```

Reinstall dependencies.

```bash
pip install --upgrade \
jinja2 \
xmltodict
```

---

## ❌ XML Parsing Errors

Verify the manifest exists.

```bash
ls -la AndroidManifest.xml
```

Validate XML syntax.

```bash
xmllint AndroidManifest.xml
```

Possible causes:

* Corrupted APK
* Invalid XML structure
* Parsing logic errors

---

## ❌ Report Generation Fails

Verify assessment results exist.

```bash
ls -la assessment_results.json
```

Validate JSON.

```bash
python3 -m json.tool assessment_results.json
```

Check:

* Template syntax
* File permissions
* JSON formatting

---

## ❌ ZIP Package Creation Fails

Verify package contents.

```bash
ls
```

Required files:

```text
assessment_results.json

MASVS_Assessment_Report.md

MASVS_Assessment_Report.html
```

Check disk space.

```bash
df -h
```

---

# 🔑 Key Learning Points

During this lab you learned how to:

* 📱 Analyze Android APK files
* 🛡 Understand MASVS methodology
* 📄 Parse Android manifests
* 🐍 Automate assessments using Python
* 📊 Structure security findings
* 📝 Generate professional reports
* 🌐 Produce web-based reports
* 📦 Package deliverables
* 🔄 Create repeatable assessment workflows

---

# 📚 Understanding MASVS Categories

The OWASP MASVS framework consists of eight major domains:

| Category | Description                            |
| -------- | -------------------------------------- |
| 🏗️ V1   | Architecture, Design & Threat Modeling |
| 💾 V2    | Data Storage & Privacy                 |
| 🔐 V3    | Cryptography                           |
| 👤 V4    | Authentication & Session Management    |
| 🌐 V5    | Network Communication                  |
| 📱 V6    | Platform Interaction                   |
| ⚙️ V7    | Code Quality & Build Configuration     |
| 🔒 V8    | Resilience Against Reverse Engineering |

Together these categories provide comprehensive coverage of mobile application security requirements.

---

# 🚀 Next Steps

Continue expanding your mobile security expertise by exploring:

### 📱 Mobile Penetration Testing

* Runtime analysis
* Dynamic testing
* Application instrumentation

---

### 🔥 Android Reverse Engineering

* JADX
* APKTool
* Smali analysis

---

### 🛡 OWASP Mobile Security

* MASVS
* MSTG
* Mobile Threat Modeling

---

### ⚙ CI/CD Security Automation

* Security pipelines
* Automated assessments
* Continuous compliance validation

---

### 📊 Advanced Reporting

* Executive dashboards
* Compliance mapping
* Risk scoring systems

---

# 🏆 Skills Acquired

After completing this lab, you now possess practical experience with:

* ✅ OWASP MASVS Framework
* ✅ Android Static Analysis
* ✅ APK Decompilation
* ✅ Security Configuration Review
* ✅ Python Security Automation
* ✅ XML Parsing
* ✅ JSON Reporting
* ✅ Markdown Documentation
* ✅ HTML Report Generation
* ✅ Assessment Packaging
* ✅ Compliance Validation

---

# 📖 Conclusion

This lab demonstrated how to build a complete **OWASP MASVS Assessment Framework** capable of analyzing Android applications and producing professional security deliverables.

You successfully learned how to:

* 📱 Decompile Android applications
* 🔍 Analyze security-relevant configurations
* 🛡 Implement MASVS security checks
* 🐍 Automate assessments using Python
* 📊 Generate structured findings
* 📝 Produce professional reports
* 📦 Package deliverables for stakeholders

The automation techniques developed in this exercise can be integrated into enterprise security workflows, vulnerability management programs, and CI/CD pipelines to provide continuous mobile application security validation.

---

# ⚖️ Ethical Use Notice

> This laboratory is intended solely for educational purposes, authorized security assessments, and compliance validation activities.
>
> Always obtain proper authorization before analyzing, testing, or assessing any application, infrastructure, or environment. Unauthorized security testing may violate organizational policies and applicable laws.

---

<div align="center">

# 🎉 Congratulations!

## 🏅 MASVS Assessment Lab Completed Successfully

You have successfully:

✅ Built a MASVS Assessment Framework
✅ Automated Android Security Analysis
✅ Generated Professional Security Reports
✅ Created Assessment Distribution Packages
✅ Practiced Mobile Application Compliance Verification

### 🚀 Continue Your Journey Toward Becoming a Professional Mobile Application Security Assessor

**Al Razzaq Certified Mobile Application Penetration Engineer (CMAPE)**

</div>


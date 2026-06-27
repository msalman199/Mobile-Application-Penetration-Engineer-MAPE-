# 📱 Extract Plist and SQLite Data from Mobile Apps

<div align="center">

# 🔍 Mobile Application Data Storage Analysis 

### SQLite Analysis • Property List Parsing • Python Automation • Mobile Data Extraction

![Platform](https://img.shields.io/badge/Platform-Mobile-black?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Mobile%20Forensics-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Data%20Extraction-success?style=for-the-badge)
![Environment](https://img.shields.io/badge/Linux-Ubuntu%2022.04-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Lab-Hands--On-brightgreen?style=for-the-badge)

</div>

---

# 📖 Overview

This hands-on lab introduces students to the techniques used during **mobile application security assessments** to extract and analyze data stored inside **SQLite databases** and **Property List (plist)** files.

Students will learn how to identify sensitive information such as API keys, authentication tokens, credentials, and application settings. They will also automate the analysis process using Python and generate professional security assessment reports.

These techniques are commonly used during **mobile penetration testing**, **application forensics**, and **secure code reviews**.

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

- 📱 Extract SQLite databases from mobile applications
- 📄 Parse Property List (plist) files
- 🔍 Identify sensitive application data
- 🔐 Detect insecure storage of credentials
- 🗄 Query SQLite databases using SQL
- 🐍 Automate analysis using Python
- 📊 Generate security assessment reports
- 🛡 Evaluate mobile application data storage security
- 📑 Document security findings professionally

---

# 🧠 Skills You Will Gain

- Mobile Application Security
- SQLite Database Analysis
- Property List Analysis
- Static Mobile Assessment
- Python Automation
- SQL Querying
- Sensitive Data Discovery
- Mobile Forensics
- Security Reporting
- Secure Storage Assessment

---

# 🛠 Technologies Used

## Mobile Platform

- Android
- iOS

## Operating System

- Ubuntu 22.04 LTS

## Databases

- SQLite

## File Formats

- Property List (plist)
- XML
- JSON
- CSV

## Programming Languages

- Python 3.10+
- SQL
- Bash

## Python Libraries

- sqlite3
- plistlib
- pathlib
- json
- datetime
- re

---

# 📚 Prerequisites

Before starting this lab, students should have:

- Basic Linux command-line knowledge
- Fundamental Python programming skills
- Understanding of SQL query syntax
- Familiarity with file systems
- Basic understanding of mobile application architecture

---

# 🖥 Lab Environment

The lab uses a preconfigured Ubuntu 22.04 virtual machine containing:

- SQLite3
- Python 3
- plistlib
- Sample mobile application data
- Preconfigured working directory
- Analysis utilities

---

# 🏗 Lab Architecture

```text
           Mobile Application
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
 SQLite Database         Property Lists
        │                       │
        └───────────┬───────────┘
                    ▼
          Python Analysis Engine
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
   Data Review  Risk Analysis  Reports
```

---

# 📂 Project Structure

```text
mobile_analysis/

├── sample_app/
│
├── Documents/
│   └── userdata.db
│
├── Library/
│   └── Preferences/
│       └── com.example.app.plist
│
├── plist_analyzer.py
├── mobile_analyzer.py
├── extraction_utils.py
│
├── reports/
├── exports/
└── logs/
```

---

# 🚀 Task 1 — Analyze SQLite Databases

---

# 🎯 Objective

Mobile applications frequently store application data inside **SQLite databases**.

During penetration testing and forensic investigations, these databases often contain sensitive information such as:

- User accounts
- Authentication tokens
- API keys
- Chat messages
- Encryption keys
- Configuration settings

In this task, you will inspect and query SQLite databases to identify sensitive information.

---

## Step 1 — Create the Working Environment

Create the required directory structure.

```bash
mkdir -p ~/mobile_analysis/sample_app/{Documents,Library/Preferences}

cd ~/mobile_analysis
```

---

## Step 2 — Verify Installed Tools

Verify SQLite.

```bash
sqlite3 --version
```

Verify Python.

```bash
python3 --version
```

---

### ✅ Expected Output

```text
SQLite version 3.x.x

Python 3.10.x
```

---

# 📦 Mobile Application Storage

Typical mobile application data is stored in:

| Location | Purpose |
|----------|----------|
| Documents | User-generated data |
| Library | Application configuration |
| Preferences | Property List files |
| Cache | Temporary application data |
| Databases | SQLite databases |

---

# 🚀 Step 3 — Create a Sample SQLite Database

Generate a sample application database.

```bash
sqlite3 sample_app/Documents/userdata.db
```

Inside the SQLite console, create the required tables and sample records as provided in the lab instructions.

Exit SQLite when finished.

```sql
.quit
```

---

# 📊 Database Schema

The sample database contains three tables.

| Table | Description |
|--------|-------------|
| users | User account information |
| app_settings | Application configuration |
| messages | User messages |

---

# 🚀 Step 4 — Explore the Database

Display all available tables.

```bash
sqlite3 sample_app/Documents/userdata.db ".tables"
```

---

View the complete schema.

```bash
sqlite3 sample_app/Documents/userdata.db ".schema"
```

---

### ✅ Expected Tables

```text
users

app_settings

messages
```

---

# 📄 Inspect User Data

Retrieve all user records.

```bash
sqlite3 sample_app/Documents/userdata.db "SELECT * FROM users;"
```

---

### Example Output

```text
1

john_doe

john@example.com

sha256:abc123

token_abc123
```

---

# ⚙ Review Application Settings

Display configuration values.

```bash
sqlite3 sample_app/Documents/userdata.db "SELECT * FROM app_settings;"
```

---

Example data may include:

- Encryption keys
- API endpoints
- Analytics identifiers
- Configuration values

---

# 📤 Export Database Tables

Export user data.

```bash
sqlite3 -header -csv sample_app/Documents/userdata.db \
"SELECT * FROM users;" > users_export.csv
```

Export application settings.

```bash
sqlite3 -header -csv sample_app/Documents/userdata.db \
"SELECT * FROM app_settings;" > settings_export.csv
```

---

# 📁 Exported Files

```text
users_export.csv

settings_export.csv
```

---

# 🚀 Step 5 — Search for Sensitive Information

Search for API keys and tokens.

```bash
sqlite3 sample_app/Documents/userdata.db \
"SELECT * FROM app_settings
WHERE key LIKE '%key%'
OR key LIKE '%token%';"
```

---

Search messages containing sensitive information.

```bash
sqlite3 sample_app/Documents/userdata.db \
"SELECT * FROM messages
WHERE content LIKE '%key%'
OR content LIKE '%password%'
OR content LIKE '%token%';"
```

---

# 📊 Count Database Records

Display record totals.

```bash
sqlite3 sample_app/Documents/userdata.db "
SELECT 'users',COUNT(*) FROM users
UNION
SELECT 'messages',COUNT(*) FROM messages
UNION
SELECT 'app_settings',COUNT(*) FROM app_settings;
"
```

---

# 🔍 Sensitive Data Indicators

During database analysis, look for:

- API Keys
- Passwords
- Authentication Tokens
- Session IDs
- Encryption Keys
- Email Addresses
- Personally Identifiable Information (PII)
- Internal Server URLs

---

# 📈 Skills Developed

By completing this section you have learned how to:

- ✅ Create SQLite databases
- ✅ Explore database schemas
- ✅ Execute SQL queries
- ✅ Export database contents
- ✅ Search for sensitive information
- ✅ Identify insecure data storage
- ✅ Analyze mobile application databases

---

# 🎉 Part 1 Complete

You have successfully:

- 📱 Created the mobile analysis workspace
- 🗄 Built a sample SQLite database
- 🔍 Queried database tables
- 📄 Exported application data
- 🔐 Identified sensitive information
- 📊 Evaluated application data storage

---

➡️ **Next:** **Part 2** covers:

- 📄 Parsing Property List (plist) Files
- 🐍 Building a Python Plist Analyzer
- 🔍 Identifying Sensitive Configuration Data
- 📊 JSON Report Generation
- 📑 Manual Plist Inspection
- 🛡 Security Assessment of Configuration Files

# 🚀 Task 2 — Parse Property List (Plist) Files

---

# 🎯 Objective

Property List (**plist**) files are one of the primary storage mechanisms used by iOS applications for configuration settings, user preferences, authentication data, and cached information.

During mobile application security assessments, improperly protected plist files often expose sensitive information such as:

- API Keys
- Authentication Tokens
- User Credentials
- Server URLs
- Debug Settings
- Application Preferences
- Encryption Keys

In this task, you will inspect plist files manually and develop a Python-based analyzer to automatically identify sensitive information.

---

# 📊 Plist Analysis Workflow

```text
           Property List
                 │
                 ▼
        Parse with plistlib
                 │
                 ▼
      Recursive Key Inspection
                 │
                 ▼
      Sensitive Pattern Matching
                 │
                 ▼
         Risk Classification
                 │
                 ▼
          JSON Security Report
```

---

# 🛠 Step 1 — Create a Sample Plist File

Create the application's preferences directory.

```bash
mkdir -p sample_app/Library/Preferences
```

Create the sample plist file.

```bash
nano sample_app/Library/Preferences/com.example.app.plist
```

Paste the provided Property List content from the lab manual and save the file.

---

# 📂 Typical iOS Plist Locations

| Directory | Purpose |
|-----------|----------|
| Preferences | User settings |
| Library | Application configuration |
| Cache | Cached data |
| Documents | User-generated files |

---

# 📄 Example Stored Information

A typical plist file may contain:

- API Keys
- User Credentials
- Server URLs
- Authentication Tokens
- Feature Flags
- Analytics IDs
- Debug Settings
- Application Preferences

---

# 🚀 Step 2 — Build the Plist Analyzer

Create the analyzer script.

```text
plist_analyzer.py
```

---

# 📦 Analyzer Responsibilities

The analyzer automatically:

- Parse Property List files
- Traverse nested dictionaries
- Detect sensitive keys
- Search for credentials
- Classify risk levels
- Export JSON reports

---

# 🧩 Script Architecture

```text
plist_analyzer.py

│
├── parse_plist_file()
├── identify_sensitive_keys()
├── generate_report()
└── main()
```

---

# 🔍 Parsing the Plist File

The parser should:

- Open the plist file
- Load XML or Binary plist
- Handle parsing exceptions
- Return structured Python objects

---

# 📄 Expected Output

```text
Successfully Parsed

Dictionary Keys

6

Nested Objects

2
```

---

# 🔐 Sensitive Information Detection

The analyzer searches for common security indicators.

---

## API Keys

Examples:

```text
APIKey

apikey

api_key
```

---

## Passwords

Examples:

```text
password

passwd

pwd
```

---

## Tokens

Examples:

```text
token

auth

bearer
```

---

## Secrets

Examples:

```text
secret

private

credential
```

---

## Email Addresses

Regular expression detects addresses such as:

```text
john@example.com

admin@company.com
```

---

# 📊 Risk Classification

Each finding is assigned a severity.

| Risk | Description |
|------|-------------|
| 🔴 High | Passwords, Secrets, API Keys |
| 🟠 Medium | Tokens, Credentials |
| 🟢 Low | Email Addresses, Configuration |

---

# 📁 Example Findings

```text
HIGH

APIKey

HIGH

Password

MEDIUM

JWT Token

LOW

Email Address
```

---

# 📄 Report Structure

The generated JSON report contains:

- Timestamp
- File Name
- Total Findings
- Risk Summary
- Sensitive Data
- Original Plist Data

---

# ▶ Save the Script

Create the file.

```bash
nano plist_analyzer.py
```

Paste the lab skeleton code.

Save and exit.

---

# ▶ Make Executable

```bash
chmod +x plist_analyzer.py
```

---

# ▶ Execute the Analyzer

```bash
python3 plist_analyzer.py
```

---

# 📊 Example Console Output

```text
=== Plist Analysis Tool ===

Parsing...

Searching...

Sensitive Findings

6

High Risk

3

Medium Risk

2

Low Risk

1

Report Saved
```

---

# 📂 Generated Report

```text
plist_analysis_report.json
```

---

# 📄 Example JSON Report

```json
{
    "risk":"HIGH",
    "findings":6,
    "high":3,
    "medium":2,
    "low":1
}
```

---

# 🚀 Step 3 — Manual Plist Inspection

Although automation is valuable, manual inspection often reveals additional context.

Display the raw plist.

```bash
cat sample_app/Library/Preferences/com.example.app.plist
```

---

# Pretty Print the Plist

Use Python's built-in plist parser.

```bash
python3 << EOF
import plistlib

with open(
"sample_app/Library/Preferences/com.example.app.plist",
"rb"
) as f:

    data = plistlib.load(f)

    print(data)

EOF
```

---

# Display Available Keys

```bash
python3 << EOF
import plistlib

with open(
"sample_app/Library/Preferences/com.example.app.plist",
"rb"
) as f:

    data = plistlib.load(f)

    print(list(data.keys()))

EOF
```

---

# Example Output

```text
APIKey

UserCredentials

ServerURL

DebugMode

LastLoginDate
```

---

# 🔎 Security Indicators

During manual review, pay close attention to:

- Hardcoded API Keys
- Plaintext Passwords
- Authentication Tokens
- JWT Tokens
- OAuth Credentials
- Internal URLs
- Debug Flags
- Test Credentials

---

# 📊 Common Mobile Storage Weaknesses

| Weakness | Risk |
|----------|------|
| Plaintext Passwords | 🔴 High |
| Hardcoded API Keys | 🔴 High |
| Stored Authentication Tokens | 🔴 High |
| Debug Enabled | 🟠 Medium |
| Internal URLs | 🟠 Medium |
| User Email Addresses | 🟢 Low |

---

# 📈 Skills Developed

By completing this section you have learned how to:

- ✅ Parse Property List files
- ✅ Use Python's `plistlib`
- ✅ Detect sensitive configuration values
- ✅ Identify authentication credentials
- ✅ Perform recursive data inspection
- ✅ Generate structured JSON reports
- ✅ Conduct manual configuration analysis

---

# 🎉 Part 2 Complete

You have successfully:

- 📄 Parsed Property List files
- 🐍 Built a Python plist analyzer
- 🔍 Detected sensitive configuration data
- 🔐 Classified security findings
- 📊 Generated JSON analysis reports
- 🛡 Reviewed application configuration manually

---

➡️ **Next:** **Part 3** covers:

- 🤖 Automated Mobile Application Analyzer
- 🗄 SQLite Database Automation
- 📄 Plist Enumeration
- 📊 HTML & JSON Report Generation
- 📁 CSV Export Utilities
- 🔎 Sensitive Pattern Detection
- 📈 Security Assessment Dashboard

# 🚀 Task 3 — Automate Mobile App Analysis with Python

---

# 🎯 Objective

Manually reviewing every SQLite database and Property List file can become time-consuming, especially when assessing large mobile applications.

In this task, you will build an automated **Mobile Application Analyzer** capable of locating application data, analyzing SQLite databases, parsing plist files, identifying sensitive information, and generating comprehensive security reports.

This approach reflects how professional mobile penetration testers and forensic analysts automate repetitive analysis tasks.

---

# 📊 Automated Analysis Workflow

```text
           Mobile Application
                    │
        ┌───────────┴────────────┐
        │                        │
        ▼                        ▼
   SQLite Databases        Property Lists
        │                        │
        └───────────┬────────────┘
                    ▼
          MobileAppAnalyzer
                    │
      ┌─────────────┼─────────────┐
      │             │             │
      ▼             ▼             ▼
 SQLite Scan   Plist Scan   Sensitive Data Scan
      │             │             │
      └─────────────┼─────────────┘
                    ▼
            JSON / HTML Reports
```

---

# 🛠 Step 1 — Create the Mobile Application Analyzer

Create the following file.

```text
mobile_analyzer.py
```

---

# 📦 Analyzer Responsibilities

The analyzer automatically:

- Discover SQLite databases
- Discover plist files
- Parse application data
- Identify sensitive information
- Generate security findings
- Export JSON reports
- Produce analysis statistics

---

# 🧩 Class Structure

```text
MobileAppAnalyzer
│
├── __init__()
├── find_files()
├── analyze_sqlite()
├── analyze_plist()
├── run_full_analysis()
├── export_report()
└── main()
```

---

# 📂 Locate Mobile Application Files

The analyzer recursively searches the application directory for:

```text
*.db

*.sqlite

*.sqlite3

*.plist
```

---

# 📁 Example Discovery Results

```text
Found

userdata.db

preferences.plist

settings.plist
```

---

# 🔍 Analyze SQLite Databases

Each discovered database should be inspected for:

- Database tables
- Table schemas
- Column names
- Sample records
- Sensitive columns
- Stored credentials

---

# 📊 Information Collected

For every database, gather:

| Information | Description |
|------------|-------------|
| Tables | Database tables |
| Schema | Column definitions |
| Row Count | Number of records |
| Sample Data | Example entries |
| Sensitive Fields | Passwords, Tokens, Keys |

---

# 🔐 Sensitive Database Columns

Examples include:

```text
password

passwd

token

secret

apikey

auth_token

jwt

private_key
```

---

# 📄 Analyze Property List Files

Each plist file should be examined for:

- API Keys
- Passwords
- Tokens
- Server URLs
- User Credentials
- Email Addresses
- Encryption Keys

---

# 📈 Risk Assessment

Every finding receives a severity rating.

| Risk | Meaning |
|------|----------|
| 🔴 High | Credentials, Secrets, API Keys |
| 🟠 Medium | Tokens, URLs |
| 🟢 Low | User Preferences |

---

# 🚀 Run Full Analysis

The analyzer performs the following sequence.

```text
Locate Files

↓

Analyze SQLite

↓

Analyze Plists

↓

Aggregate Findings

↓

Generate Report
```

---

# ▶ Execute the Analyzer

Make the script executable.

```bash
chmod +x mobile_analyzer.py
```

Run the analysis.

```bash
python3 mobile_analyzer.py
```

---

# 📊 Example Console Output

```text
SQLite Files

1

Plist Files

2

Sensitive Findings

11

High Risk

4

Medium Risk

5

Low Risk

2

Analysis Complete
```

---

# 📂 Generated Report

```text
analysis_report.json
```

---

# 📄 Example JSON Report

```json
{
    "sqlite_files":1,
    "plist_files":2,
    "total_findings":11,
    "high":4,
    "medium":5,
    "low":2
}
```

---

# 🚀 Step 2 — Create Data Extraction Utilities

Create

```text
extraction_utils.py
```

---

# 📦 Utility Responsibilities

The helper module should provide:

- SQLite Export
- CSV Generation
- Sensitive Pattern Detection
- HTML Report Generation

---

# 🧩 Module Structure

```text
extraction_utils.py

│
├── extract_sqlite_to_csv()
├── search_sensitive_patterns()
├── generate_html_report()
```

---

# 📤 Export SQLite Tables

Each SQLite table should be exported into a separate CSV file.

Example:

```text
users.csv

messages.csv

settings.csv
```

---

# 🔍 Search Sensitive Patterns

The analyzer searches extracted text for common Indicators of Exposure.

Supported patterns include:

- Email Addresses
- API Keys
- JWT Tokens
- IP Addresses

---

# 📧 Email Detection

Example:

```text
john@example.com

admin@company.com
```

---

# 🔑 API Key Detection

Examples:

```text
sk_live_xxxxx

pk_live_xxxxx
```

---

# 🔐 JWT Detection

Typical JWT tokens begin with:

```text
eyJ
```

---

# 🌐 IP Address Detection

Examples:

```text
192.168.1.10

10.0.0.5
```

---

# 📄 Generate HTML Report

The HTML report should include:

- Executive Summary
- Statistics
- Findings
- Risk Levels
- Color-Coded Severity
- Recommendations

---

# 📊 HTML Layout

```text
Summary

↓

Risk Statistics

↓

SQLite Findings

↓

Plist Findings

↓

Recommendations
```

---

# 📁 Generated Files

```text
analysis_report.json

analysis_report.html

users.csv

settings.csv

messages.csv
```

---

# ▶ Execute Complete Analysis

Run the automated analyzer.

```bash
python3 mobile_analyzer.py
```

---

# View Generated Files

```bash
ls -lh *.json *.csv *.html
```

---

# Display Report Summary

```bash
python3 << EOF
import json

with open("analysis_report.json") as f:
    report=json.load(f)

print("Analysis Time:",report["timestamp"])
print("SQLite Files:",len(report["sqlite_files"]))
print("Plist Files:",len(report["plist_files"]))
print("Total Findings:",len(report["findings"]))

EOF
```

---

# 📈 Skills Developed

During this section you learned how to:

- ✅ Build an automated mobile application analyzer
- ✅ Locate SQLite databases
- ✅ Locate Property List files
- ✅ Export SQLite tables to CSV
- ✅ Detect sensitive information automatically
- ✅ Generate HTML reports
- ✅ Generate JSON reports
- ✅ Perform large-scale mobile application assessments

---

# 🎉 Part 3 Complete

You have successfully:

- 🤖 Built a Mobile Application Analyzer
- 🗄 Automated SQLite database analysis
- 📄 Automated Property List inspection
- 🔍 Detected sensitive application data
- 📊 Generated JSON reports
- 🌐 Generated HTML security reports
- 📁 Exported application data to CSV

---

➡️ **Next:** **Part 4** covers:

- ✅ Lab Verification
- 🛠 Troubleshooting Guide
- 📊 Expected Outcomes
- 🎓 Learning Outcomes
- 🔒 Security Best Practices
- 📚 Key Takeaways
- ⚠ Disclaimer
- 🤝 Contributing
- ⭐ Support
# 🚀 Lab Verification & Final Assessment

---

# ✅ Lab Verification Checklist

Verify that each task has been completed successfully before finishing the lab.

| Verification Item | Status |
|-------------------|--------|
| Mobile Analysis Workspace Created | ✅ |
| SQLite Database Created | ✅ |
| SQLite Schema Reviewed | ✅ |
| Database Tables Queried | ✅ |
| Sensitive Database Data Identified | ✅ |
| CSV Exports Generated | ✅ |
| Property List File Parsed | ✅ |
| Sensitive Keys Detected | ✅ |
| Python Plist Analyzer Executed | ✅ |
| Mobile Application Analyzer Completed | ✅ |
| JSON Report Generated | ✅ |
| HTML Report Generated | ✅ |
| Security Findings Reviewed | ✅ |

---

# 📁 Expected Project Structure

```text
mobile_analysis/

├── sample_app/
│
├── Documents/
│   └── userdata.db
│
├── Library/
│   └── Preferences/
│       └── com.example.app.plist
│
├── plist_analyzer.py
├── mobile_analyzer.py
├── extraction_utils.py
│
├── users_export.csv
├── settings_export.csv
├── analysis_report.json
├── analysis_report.html
│
├── reports/
├── exports/
└── logs/
```

---

# 📊 Verify Generated Reports

Display generated reports.

```bash
ls -lh *.json *.html *.csv
```

---

Validate JSON formatting.

```bash
python3 -m json.tool analysis_report.json
```

---

Display CSV files.

```bash
cat users_export.csv
```

```bash
cat settings_export.csv
```

---

Open the HTML report using a browser.

```bash
xdg-open analysis_report.html
```

---

# 📈 Expected Outcomes

After successfully completing this lab, you should be able to:

- 📱 Analyze mobile application storage
- 🗄 Query SQLite databases
- 📄 Parse Property List (plist) files
- 🔍 Discover sensitive information
- 🔐 Detect insecure storage mechanisms
- 🐍 Automate analysis using Python
- 📊 Generate JSON security reports
- 🌐 Produce HTML assessment reports
- 📑 Export application data for forensic analysis
- 🛡 Assess mobile application storage security

---

# 🔍 Typical Security Findings

During assessments you may discover:

- Hardcoded API Keys
- Authentication Tokens
- Plaintext Passwords
- Email Addresses
- Session Identifiers
- Encryption Keys
- Internal Server URLs
- OAuth Credentials
- Analytics Tokens
- Debug Configuration

---

# 📊 Risk Classification

| Risk Level | Description |
|------------|-------------|
| 🔴 High | Passwords, Secrets, API Keys, Encryption Keys |
| 🟠 Medium | Tokens, URLs, Session IDs |
| 🟢 Low | Email Addresses, Preferences, Configuration |

---

# 🛠 Troubleshooting Guide

---

## ❌ SQLite Database Cannot Be Opened

### Symptoms

```text
Error: unable to open database file
```

### Solution

Verify that the database exists.

```bash
ls -lh sample_app/Documents/
```

Check file permissions.

```bash
chmod 644 sample_app/Documents/userdata.db
```

---

## ❌ Database Locked

### Symptoms

```text
database is locked
```

### Solution

Ensure no other SQLite sessions are using the database.

Retry after closing existing connections.

Optionally increase the timeout.

```bash
sqlite3 sample_app/Documents/userdata.db ".timeout 5000"
```

---

## ❌ Plist Parsing Fails

### Symptoms

```text
Invalid plist
```

### Solution

Verify file type.

```bash
file sample_app/Library/Preferences/com.example.app.plist
```

Confirm the plist is valid XML or Binary Property List format.

---

## ❌ Python Import Errors

### Symptoms

```text
ModuleNotFoundError
```

### Solution

Verify Python version.

```bash
python3 --version
```

Ensure the standard libraries (`plistlib`, `sqlite3`, `json`, `pathlib`) are available.

---

## ❌ No Sensitive Findings Detected

### Possible Causes

- Incorrect regular expressions
- Invalid search logic
- Empty data source
- Wrong file path

Verify the source files exist.

```bash
find sample_app -type f
```

---

## ❌ HTML Report Missing

Ensure the report generation function executed successfully.

Verify the output file.

```bash
ls -lh analysis_report.html
```

---

# 🔐 Security Best Practices

When assessing mobile applications:

- Store sensitive data using secure platform storage APIs.
- Never store passwords in plaintext.
- Encrypt local databases containing confidential information.
- Avoid embedding API keys directly inside applications.
- Use secure authentication tokens with proper expiration.
- Protect configuration files from unauthorized access.
- Minimize sensitive data stored on the device.
- Remove debug settings before production releases.

---

# 📚 Key Takeaways

- SQLite is the primary structured storage mechanism used by many mobile applications.
- Property List files frequently contain application configuration and user preferences.
- Sensitive information may be exposed through insecure local storage.
- Automated analysis significantly improves assessment efficiency and consistency.
- Combining manual review with scripting provides better security coverage.

---

# 🎓 Learning Outcomes

Upon completing this lab, you can:

- Analyze SQLite databases used by mobile applications.
- Inspect Property List files for configuration and credential data.
- Identify insecure storage of sensitive information.
- Automate mobile application assessments using Python.
- Export application data into CSV, JSON, and HTML formats.
- Produce professional mobile application security reports.

---

# 🚀 Next Labs

Continue your Mobile Application Penetration Testing journey with:

- 📱 Android Application Reverse Engineering
- 🍏 iOS Application Security Assessment
- 🔐 Secure Storage Analysis
- 🌐 Mobile API Security Testing
- 📡 Intercepting Mobile Network Traffic
- 🛠 Runtime Instrumentation with Frida
- 📦 APK & IPA Static Analysis
- 🔍 Mobile Malware Analysis
- ☁️ Cloud-Connected Mobile App Assessment
- 🤖 Automated Mobile Security Testing

---

# ⚠ Disclaimer

This laboratory is provided **solely for educational purposes, cybersecurity training, mobile application security research, and authorized security assessments**.

Only analyze applications and data that you own or have explicit authorization to test. Unauthorized access to application data may violate organizational policies, contracts, or applicable laws.

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

- 📚 Adding new mobile security labs
- 🐍 Improving Python automation scripts
- 📝 Enhancing documentation
- 🐛 Reporting bugs and issues
- 🚀 Optimizing analysis workflows
- 🔍 Expanding detection patterns
- 📊 Improving report generation

---

# ⭐ Support

If you found this repository helpful:

- ⭐ Star the repository
- 🍴 Fork the repository
- 📢 Share it with the cybersecurity community
- 🤝 Contribute to future improvements

---

<div align="center">

# 📱 Master Mobile Data Extraction & Security Analysis

### 🚀 Happy Learning & Secure Coding!

</div>
- 

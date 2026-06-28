# 📱 Scan Apps with MobSF and Analyze Findings

<div align="center">

# 🛡 Mobile Application Security Analysis 

## **Scan Apps with MobSF and Analyze Findings**

[![Android](https://img.shields.io/badge/Android-Security-3DDC84?style=for-the-badge\&logo=android)](https://developer.android.com/)
[![MobSF](https://img.shields.io/badge/MobSF-Mobile%20Security-blue?style=for-the-badge)]
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python)](https://python.org/)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-FCC624?style=for-the-badge\&logo=linux)]
[![APK](https://img.shields.io/badge/APK-Static%20Analysis-success?style=for-the-badge)]
[![REST API](https://img.shields.io/badge/REST-API-orange?style=for-the-badge)]
[![JSON](https://img.shields.io/badge/JSON-Reports-black?style=for-the-badge)]
[![OWASP](https://img.shields.io/badge/OWASP-Mobile%20Top%2010-red?style=for-the-badge)]
[![Automation](https://img.shields.io/badge/Python-Automation-purple?style=for-the-badge)]

---

# 🔍 Scan Apps with MobSF and Analyze Findings

### **Android Mobile Security Assessment Lab**

*Learn how to install Mobile Security Framework (MobSF), perform static analysis on Android applications, automate APK scanning using the MobSF API, and generate professional mobile security assessment reports.*

</div>

---

# 📖 Overview

The **Mobile Security Framework (MobSF)** is one of the most widely used open-source platforms for automated mobile application security testing. It performs comprehensive static analysis of Android APKs, helping security professionals identify vulnerabilities such as insecure configurations, hardcoded secrets, weak cryptography, exported components, insecure permissions, and many other security weaknesses.

In this lab, you will install and configure MobSF, analyze vulnerable Android applications, automate security assessments through the MobSF REST API, and build the foundation for scalable mobile application security testing.

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

* ✅ Install and configure Mobile Security Framework (MobSF)
* ✅ Analyze Android APKs using the MobSF Web Interface
* ✅ Perform automated APK uploads using the MobSF REST API
* ✅ Interpret MobSF vulnerability findings
* ✅ Automate APK scanning with Python
* ✅ Generate professional mobile security reports

---

# 📚 Prerequisites

Before starting this lab, you should have:

* 🐧 Basic Linux command-line skills
* 📱 Understanding of Android APK architecture
* 🐍 Basic Python programming knowledge
* 🔍 Familiarity with mobile security concepts
* 🛡 Basic understanding of the OWASP Mobile Top 10

---

# 🛠 Lab Environment

The lab environment includes:

* 🐧 Ubuntu 20.04 LTS (or later)
* ☕ OpenJDK 8
* 🐍 Python 3
* 📦 Git
* 📂 MobSF Framework
* 🌐 Internet Connectivity

### 💻 Recommended System Requirements

| Component        | Requirement         |
| ---------------- | ------------------- |
| Operating System | Ubuntu 20.04+       |
| RAM              | Minimum 4 GB        |
| Storage          | 20 GB Free Space    |
| CPU              | Dual Core or Higher |
| Network          | Internet Access     |

---

# 🚩 Task 1 — Install and Configure MobSF

Before scanning Android applications, you must install and configure the Mobile Security Framework.

This task prepares the analysis environment and downloads vulnerable APKs for testing.

---

# 🔹 Step 1.1 — Install System Dependencies

Update the operating system.

```bash
sudo apt update && sudo apt upgrade -y
```

---

Install the required packages.

```bash
sudo apt install python3 python3-pip python3-venv git wget openjdk-8-jdk -y
```

---

Verify the Java installation.

```bash
java -version
```

---

### ✅ Purpose

These packages provide:

* 🐍 Python Runtime
* 📦 Package Manager (pip)
* ☕ Java Development Kit
* 🌐 Git Repository Support
* ⬇ Download Utility (wget)

Without these dependencies, MobSF cannot be installed successfully.

---

# 🔹 Step 1.2 — Download MobSF

Create a workspace.

```bash
mkdir ~/security-tools

cd ~/security-tools
```

---

Clone the MobSF repository.

```bash
git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git
```

---

Navigate into the project.

```bash
cd Mobile-Security-Framework-MobSF
```

---

### 📂 Project Structure

The repository contains:

* 📄 Django Application
* 🔍 Static Analysis Engine
* 📱 Mobile Scanners
* 🌐 REST API
* 📊 Reporting Modules

---

# 🔹 Step 1.3 — Create Python Virtual Environment

Create a dedicated virtual environment.

```bash
python3 -m venv venv
```

---

Activate it.

```bash
source venv/bin/activate
```

---

### 💡 Why Use a Virtual Environment?

Using a virtual environment:

* ✔ Isolates project dependencies
* ✔ Prevents package conflicts
* ✔ Simplifies upgrades
* ✔ Keeps the host operating system clean

---

# 🔹 Step 1.4 — Install MobSF Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

---

Complete the MobSF setup.

```bash
./setup.sh
```

---

### 🔧 What Happens During Setup?

The setup process automatically:

* 📦 Installs Python packages
* ⚙ Configures Django
* 📄 Creates database files
* 📱 Downloads required components
* 🔍 Prepares static analysis engines

---

# 🔹 Step 1.5 — Start MobSF Server

Launch the MobSF web server.

```bash
python manage.py runserver 0.0.0.0:8000
```

Keep this terminal running.

---

Open another terminal and verify the server.

```bash
curl -I http://localhost:8000
```

---

### ✅ Expected Output

```text
HTTP/1.1 200 OK
```

This confirms that MobSF is running successfully.

---

# 🌐 Access the MobSF Dashboard

Open your web browser.

Visit:

```text
http://localhost:8000
```

The MobSF dashboard should appear, allowing you to upload APK files for analysis.

---

# 🔹 Step 1.6 — Download Sample APK Files

Create a directory for vulnerable Android applications.

```bash
mkdir ~/apk-samples

cd ~/apk-samples
```

---

Download **DIVA (Damn Insecure and Vulnerable App).**

```bash
wget https://github.com/payatu/diva-android/releases/download/v1.0/diva-beta.apk
```

---

Download **InsecureBankv2.**

```bash
wget https://github.com/dineshshetty/Android-InsecureBankv2/releases/download/v1.0/InsecureBankv2.apk
```

---

Verify the downloaded APK files.

```bash
ls -lh *.apk
```

---

### 📂 Expected Output

```text
diva-beta.apk
InsecureBankv2.apk
```

---

# 📱 Sample Applications

## 🔴 DIVA

The **Damn Insecure and Vulnerable App (DIVA)** is intentionally insecure and contains multiple mobile security vulnerabilities designed for learning and penetration testing.

Common issues include:

* 🔐 Hardcoded Secrets
* 💾 Insecure Data Storage
* 🌐 Insecure Communication
* 🔑 Weak Cryptography
* 📡 Exported Components

---

## 🏦 InsecureBankv2

InsecureBankv2 simulates a vulnerable banking application.

It contains:

* 🔓 Authentication Issues
* 💳 Insecure Banking APIs
* 📁 Sensitive Data Exposure
* 🛡 Weak Session Management
* 📱 Android Security Misconfigurations

---

# 🔍 MobSF Analysis Workflow

The overall workflow for static application analysis is shown below.

```text
APK File
    │
    ▼
Upload to MobSF
    │
    ▼
APK Extraction
    │
    ▼
Static Analysis
    │
    ▼
Security Detection
    │
    ▼
Report Generation
```

---

# 🎯 Skills Gained

After completing Task 1, you will be able to:

* ✔ Install MobSF from source
* ✔ Configure Python virtual environments
* ✔ Launch the MobSF web server
* ✔ Verify MobSF functionality
* ✔ Prepare Android applications for analysis
* ✔ Understand the MobSF static analysis workflow

---

# ✅ Task 1 Summary

In this task, you successfully prepared a complete mobile application security assessment environment by installing MobSF, configuring its dependencies, launching the analysis server, and downloading intentionally vulnerable Android applications for testing.

The environment is now ready for performing automated static analysis and exploring mobile application security findings.

---

➡ **Next:** **Task 2 — Perform Static Analysis with MobSF Using the Web Interface and REST API**
# 🚩 Task 2 — Perform Static Analysis with MobSF

With MobSF successfully installed and running, you can now begin analyzing Android applications. In this task, you will learn how to upload APKs manually through the MobSF web interface and automate the same process using the MobSF REST API.

By the end of this task, you will have a reusable Python tool capable of uploading APK files, initiating scans, and monitoring scan progress automatically.

---

# 🔹 Step 2.1 — Upload APK via the MobSF Web Interface

Open your browser and navigate to the MobSF dashboard.

```text id="b6r5jt"
http://localhost:8000
```

---

## 📋 Manual Upload Process

Follow these steps:

1. 🌐 Open the MobSF Dashboard.
2. 📤 Click the **Upload** button.
3. 📂 Browse to the sample APK directory.
4. 📱 Select **diva-beta.apk**.
5. ▶ Click **Start Scan**.
6. ⏳ Wait for the scan to complete (approximately **2–5 minutes**).

---

### 📊 What Happens During the Scan?

MobSF automatically performs several analysis stages:

```text id="8k9npa"
APK Upload
      │
      ▼
APK Extraction
      │
      ▼
Manifest Analysis
      │
      ▼
Code Analysis
      │
      ▼
Certificate Analysis
      │
      ▼
Permission Analysis
      │
      ▼
Report Generation
```

---

## 🔍 Static Analysis Performed by MobSF

During the scan, MobSF evaluates:

* 📄 AndroidManifest.xml
* 🔐 Hardcoded Secrets
* 📡 Exported Components
* 🔑 Cryptographic Implementations
* 🌐 Network Security Configuration
* 📁 Local Storage
* 📜 Certificates
* ⚙ Application Metadata
* 📦 Third-Party Libraries

---

# 🔹 Step 2.2 — Create an API Upload Script

While the web interface is convenient for individual applications, security engineers often automate scanning through the MobSF REST API.

Navigate to your scripts directory.

```bash id="f42o1y"
cd ~/security-tools/scripts
```

Create the upload script.

```bash id="z7h9rw"
cat > mobsf_upload.py << 'EOF'

(Paste the provided Python template here)

EOF
```

Make the script executable.

```bash id="cn4ep8"
chmod +x mobsf_upload.py
```

---

# 🧩 Script Overview

The upload script automates APK submission to MobSF using its REST API.

Students should complete every **TODO** section in the provided template.

---

# 📌 Function — `upload_apk_to_mobsf()`

Implement:

```python id="v0jq0s"
upload_apk_to_mobsf()
```

Responsibilities include:

* 📂 Verify that the APK file exists
* 📦 Prepare the file for upload
* 🌐 Send a POST request to the `/api/v1/upload` endpoint
* 📄 Parse the JSON response
* 🔑 Extract the uploaded file hash

---

### 📥 Upload Workflow

```text id="dovdxv"
APK File
      │
      ▼
File Validation
      │
      ▼
HTTP POST Request
      │
      ▼
MobSF Upload API
      │
      ▼
Receive File Hash
```

The returned **file hash** uniquely identifies the uploaded APK and is required for all future API operations.

---

# 📌 Function — `start_scan()`

Implement:

```python id="4dpcak"
start_scan()
```

The function should:

* 📋 Prepare the scan request
* 🔑 Include the uploaded file hash
* ▶ Send a POST request to `/api/v1/scan`
* ✅ Confirm that the scan has started successfully

---

### 📊 Scan Request

The request should include:

* File Hash
* Scan Type
* Authentication (if configured)

---

# 📌 Main Function

Complete the following tasks:

* 📥 Parse command-line arguments
* 📂 Validate the APK path
* 📤 Upload the APK
* ▶ Start the scan
* 📄 Display the file hash
* ✅ Report success or failure

---

# 🔹 Execute the Upload Script

Run the script.

```bash id="qg18n8"
python3 mobsf_upload.py diva-beta.apk
```

---

### 📋 Expected Output

```text id="ck5k7q"
Uploading APK...

Upload Successful

File Hash:
d9f4e8b0xxxxxxxxxxxxxxxxxxxxxxxx

Starting Static Analysis...

Scan Started Successfully
```

---

# 🔹 Step 2.3 — Monitor Scan Progress

Large applications require several minutes to analyze.

Instead of refreshing the browser repeatedly, create an automated monitoring script.

Create:

```bash id="18c8j8"
cat > monitor_scan.py << 'EOF'

(Paste the provided Python template here)

EOF
```

---

Make it executable.

```bash id="r03eqx"
chmod +x monitor_scan.py
```

---

# 🧩 Monitoring Script Overview

The monitoring script periodically queries the MobSF API until analysis is complete.

---

# 📌 Function — `check_scan_status()`

Implement:

```python id="kl8gsx"
check_scan_status()
```

Responsibilities:

* 🌐 Query the `/api/v1/scan_status` endpoint
* 📊 Parse the returned JSON
* 📋 Determine the current scan state

Possible responses include:

* 🟢 Completed
* 🟡 Running
* 🔴 Error

---

# 📌 Function — `wait_for_scan_completion()`

Implement:

```python id="g3tv1r"
wait_for_scan_completion()
```

The polling loop should:

* ⏳ Check scan status every **10 seconds**
* 🔁 Continue until completion
* ⌛ Stop after the configured timeout
* ✅ Return **True** when analysis finishes successfully

---

### 🔄 Polling Workflow

```text id="4jlwm2"
Start Monitoring
       │
       ▼
Request Status
       │
       ▼
Completed?
   │        │
  No       Yes
   │        │
Wait 10s    ▼
   │     Finish
   └───────────
```

---

# 📌 Main Function

The main routine should:

* Read the file hash from the command line
* Call `wait_for_scan_completion()`
* Display progress updates
* Notify the user when the scan completes

---

# 🔹 Run the Monitoring Script

Execute:

```bash id="vhv66d"
python3 monitor_scan.py <FILE_HASH>
```

Replace `<FILE_HASH>` with the hash returned by the upload script.

---

### 📋 Expected Output

```text id="8flqpd"
Checking Scan Status...

Status:
Running

Waiting...

Checking Again...

Status:
Completed

Static Analysis Finished Successfully
```

---

# 📱 MobSF REST API Workflow

The complete automated analysis process follows this sequence.

```text id="lxzjk7"
APK
 │
 ▼
Upload API
 │
 ▼
Receive Hash
 │
 ▼
Start Scan API
 │
 ▼
Monitor Scan
 │
 ▼
Scan Completed
 │
 ▼
Retrieve Report
```

---

# 🛡 Benefits of API Automation

Automating MobSF provides several advantages:

* ⚡ Faster APK processing
* 📦 Batch scanning support
* 🤖 CI/CD integration
* 📊 Consistent reporting
* 🔍 Reduced manual effort
* 📁 Scalable mobile security testing

---

# 📈 Skills Gained

After completing Task 2, you will be able to:

* ✔ Upload APKs through the MobSF Web Interface
* ✔ Use the MobSF REST API
* ✔ Automate APK submissions with Python
* ✔ Initiate static analysis programmatically
* ✔ Monitor scan progress automatically
* ✔ Build reusable security automation tools

---

# ✅ Task 2 Summary

In this task, you successfully learned both manual and automated methods for analyzing Android applications with MobSF. By creating Python scripts to upload APKs, trigger scans, and monitor their progress, you established the foundation for scalable mobile application security testing and future integration into automated security pipelines.

---

➡ **Next:** **Task 3 — Extract, Analyze, and Interpret MobSF Security Findings**
# 🚩 Task 3 — Analyze Security Findings

Once MobSF completes its static analysis, the next step is to retrieve the results, interpret the discovered vulnerabilities, and generate professional security reports. In this task, you will automate result extraction using the MobSF REST API, analyze the findings, and create an HTML security assessment report.

---

# 🔹 Step 3.1 — Extract Scan Results via API

Navigate to your scripts directory.

```bash
cd ~/security-tools/scripts
```

Create the results extraction script.

```bash
cat > extract_results.py << 'EOF'

(Paste the provided Python template here)

EOF
```

---

Make the script executable.

```bash
chmod +x extract_results.py
```

---

# 🧩 Script Overview

The extraction script communicates with the MobSF REST API and downloads the complete JSON report generated after static analysis.

Students should complete every **TODO** section in the provided template.

---

# 📌 Function — `get_scan_results()`

Implement:

```python
get_scan_results()
```

Responsibilities:

* 🌐 Send a POST request to the `/api/v1/report_json` endpoint
* 🔑 Supply the APK file hash
* 📄 Receive the JSON report
* 📥 Parse the response into a Python dictionary
* ✅ Return the complete scan results

---

### 📥 Data Retrieval Workflow

```text
APK Scan Completed
        │
        ▼
Report API
        │
        ▼
JSON Response
        │
        ▼
Python Dictionary
        │
        ▼
Security Analysis
```

---

# 📌 Function — `analyze_security_findings()`

Implement:

```python
analyze_security_findings()
```

This function should summarize the most important information from the MobSF report.

Display:

* 📱 Application Information
* 📦 Package Name
* 🔢 Version Information
* 📲 Target SDK
* 📊 Security Score
* ⚠ Overall Risk Level

---

## 🔍 Permission Analysis

Review all requested Android permissions.

Display:

* 🔐 Dangerous Permissions
* 📂 Storage Permissions
* 📍 Location Permissions
* 📷 Camera Access
* 🎤 Microphone Access
* 🌐 Internet Access

---

## 🚨 Vulnerability Analysis

Group vulnerabilities by severity.

Recommended categories:

| Severity         | Description                   |
| ---------------- | ----------------------------- |
| 🔴 High          | Immediate security risk       |
| 🟠 Medium        | Significant weakness          |
| 🟡 Low           | Minor issue                   |
| 🔵 Informational | Best-practice recommendations |

---

## 📋 Top Critical Findings

Display the five most important findings.

Example:

* 🔐 Hardcoded API Keys
* 💾 Insecure Data Storage
* 🌐 Cleartext HTTP Traffic
* 🔑 Weak Cryptography
* 📡 Exported Android Components

---

# 📌 Function — `save_results_to_file()`

Implement:

```python
save_results_to_file()
```

Responsibilities:

* 📄 Save the JSON report
* 🗂 Use formatted indentation
* 🕒 Include timestamps if desired
* 💾 Preserve all MobSF output

---

# 🔹 Execute the Script

Run the extractor.

```bash
python3 extract_results.py <FILE_HASH>
```

---

### 📋 Expected Output

```text
Application:
DIVA

Package:
jakhar.aseem.diva

Security Score:
24 / 100

Risk Level:
Critical

Permissions:
17

Dangerous Permissions:
6

High Severity Issues:
12
```

---

# 🔹 Step 3.2 — Review Key Security Findings

Understanding the report is just as important as generating it.

Focus your analysis on the following sections.

---

# 🔐 Security Score

MobSF assigns an overall security score.

Typical interpretation:

|  Score | Risk         |
| -----: | ------------ |
| 90–100 | 🟢 Excellent |
|  70–89 | 🟢 Good      |
|  50–69 | 🟡 Moderate  |
|  30–49 | 🟠 Poor      |
|   0–29 | 🔴 Critical  |

---

# 🔑 High Severity Issues

Pay special attention to vulnerabilities that require immediate remediation.

Examples include:

* 🔐 Hardcoded Secrets
* 🌐 Insecure Network Communication
* 💾 Sensitive Data Storage
* 🔓 Authentication Weaknesses
* 📡 Exported Components

---

# 📱 Dangerous Permissions

Review Android permissions carefully.

Common examples:

* 📍 ACCESS_FINE_LOCATION
* 📷 CAMERA
* 🎤 RECORD_AUDIO
* 📂 READ_EXTERNAL_STORAGE
* ✍ WRITE_EXTERNAL_STORAGE

Determine whether each permission is justified by the application's functionality.

---

# 🔒 Certificate Analysis

MobSF evaluates:

* 📜 Certificate Validity
* 🔑 Signature Algorithm
* 🔐 Key Strength
* 📅 Expiration Dates

Weak certificates may indicate insecure application distribution.

---

# 🌐 Network Security

Look for:

* ❌ HTTP Communication
* ❌ Missing TLS
* ❌ Weak SSL Configuration
* ❌ Certificate Validation Issues

Secure applications should always use encrypted communication channels.

---

# 💾 Storage Analysis

Review where sensitive information is stored.

Potential risks include:

* SharedPreferences
* SQLite Databases
* External Storage
* Cached Credentials
* Plaintext Files

---

# 🔹 Common Vulnerabilities in DIVA

The DIVA application intentionally contains numerous security flaws.

Typical findings include:

| Vulnerability              | Severity  |
| -------------------------- | --------- |
| 🔐 Hardcoded Credentials   | 🔴 High   |
| 💾 Insecure Data Storage   | 🔴 High   |
| 🌐 HTTP Communication      | 🔴 High   |
| 🔑 Weak Cryptography       | 🟠 Medium |
| 📡 Exported Components     | 🔴 High   |
| 🧩 Input Validation Issues | 🟠 Medium |
| 📱 Backup Enabled          | 🟡 Low    |

---

# 🔹 Step 3.3 — Generate an HTML Security Report

Create the report generator.

```bash
cat > generate_report.py << 'EOF'

(Paste the provided Python template here)

EOF
```

---

Make the script executable.

```bash
chmod +x generate_report.py
```

---

# 🧩 Report Generator Overview

The report generator converts the MobSF JSON report into a professional HTML document suitable for management, clients, or development teams.

---

# 📌 Function — `generate_html_report()`

Implement:

```python
generate_html_report()
```

The generated report should include:

* 📋 Executive Summary
* 📱 Application Information
* 📊 Security Score
* 🚨 Vulnerability Summary
* 🔐 Permissions Analysis
* 📄 Recommendations
* 📅 Assessment Date

---

# 📌 Function — `create_vulnerability_table()`

Implement:

```python
create_vulnerability_table()
```

Generate an HTML table containing:

* Severity
* Vulnerability Title
* Description
* Risk
* Recommendation

Use CSS styling to highlight severity levels for easier readability.

---

# 📄 Suggested HTML Report Structure

```text
Executive Summary
        │
        ▼
Application Information
        │
        ▼
Security Score
        │
        ▼
Vulnerability Summary
        │
        ▼
Permissions Analysis
        │
        ▼
Recommendations
```

---

# 🔹 Execute the Report Generator

Run:

```bash
python3 generate_report.py scan_results.json
```

---

### 📋 Expected Output

```text
Generating HTML Report...

Security Report Created Successfully

Output:
security_assessment_report.html
```

---

# 📊 Professional Report Sections

A complete report should contain:

* 📱 Application Details
* 📊 Security Score
* 🚨 Vulnerability Statistics
* 🔴 Critical Findings
* 🟠 Medium Findings
* 🟡 Low Findings
* 🔐 Permissions Analysis
* 📡 Network Security
* 📄 Certificate Information
* 💡 Security Recommendations

---

# 🛡 Security Assessment Workflow

```text
MobSF Report
      │
      ▼
JSON Extraction
      │
      ▼
Finding Analysis
      │
      ▼
Risk Assessment
      │
      ▼
HTML Report
      │
      ▼
Management Review
```

---

# 🎯 Skills Gained

After completing Task 3, you will be able to:

* ✔ Retrieve MobSF reports using the REST API
* ✔ Interpret static analysis findings
* ✔ Assess Android application security posture
* ✔ Identify critical vulnerabilities
* ✔ Evaluate application permissions
* ✔ Generate professional HTML assessment reports

---

# ✅ Task 3 Summary

In this task, you automated the retrieval and interpretation of MobSF scan results, transforming raw JSON data into meaningful security insights. By analyzing permissions, vulnerabilities, certificates, and network configurations—and presenting them in a professional HTML report—you developed practical reporting skills used in real-world mobile application security assessments.

---

➡ **Next:** **Task 4 — Automate Batch Scanning of Multiple APK Files and Generate Comparative Security Reports**

# 🚩 Task 4 — Automate Batch Scanning

Modern organizations often need to assess dozens or even hundreds of Android applications. Manually uploading each APK is inefficient, so automation becomes essential. In this task, you will build Python tools that scan multiple APKs, collect their results, and generate comparative security reports.

---

# 🔹 Step 4.1 — Create a Batch Processing Script

Navigate to the scripts directory.

```bash
cd ~/security-tools/scripts
```

Create the batch scanning script.

```bash
cat > batch_scan.py << 'EOF'

(Paste the provided Python template here)

EOF
```

---

Make the script executable.

```bash
chmod +x batch_scan.py
```

---

# 🧩 Script Overview

The **MobSFBatchScanner** automates the complete workflow:

* 📤 Upload APKs
* ▶ Start analysis
* ⏳ Wait for scan completion
* 📥 Retrieve scan results
* 📊 Store findings
* 📄 Generate summary reports

Students should complete every **TODO** section in the provided template.

---

# 📌 Class — `MobSFBatchScanner`

The scanner coordinates multiple APK scans and manages their results.

Responsibilities include:

* Managing concurrent scans
* Tracking scan progress
* Collecting JSON reports
* Producing summary metrics

---

# 📌 Function — `scan_apk()`

Implement:

```python
scan_apk()
```

Responsibilities:

* 📂 Validate the APK path
* 📤 Upload the APK through the MobSF API
* ▶ Initiate the static analysis
* ⏳ Wait until the scan completes
* 📥 Download the JSON report
* 💾 Return the results

---

### 📊 Single APK Workflow

```text
APK
 │
 ▼
Upload
 │
 ▼
Static Analysis
 │
 ▼
Wait
 │
 ▼
Retrieve Results
 │
 ▼
Store Report
```

---

# 📌 Function — `scan_directory()`

Implement:

```python
scan_directory()
```

The function should:

* 🔍 Locate all `.apk` files in the target directory
* 🧵 Use `ThreadPoolExecutor` for concurrent processing
* 📊 Monitor progress
* 📥 Store completed reports
* 📄 Return all results

---

### 🔄 Batch Processing Workflow

```text
APK Directory
      │
      ▼
Find APK Files
      │
      ▼
Thread Pool
      │
      ▼
Parallel Scans
      │
      ▼
Collect Results
```

---

# 📌 Function — `generate_summary_report()`

Implement:

```python
generate_summary_report()
```

The report should include:

* 📱 APK Name
* 📊 Security Score
* 🚨 High Severity Findings
* ⚠ Medium Severity Findings
* ✅ Overall Risk Rating

The summary may be generated as either **CSV** or **JSON**.

---

# 🔹 Execute the Batch Scanner

Run the scanner.

```bash
python3 batch_scan.py ~/apk-samples
```

---

### 📋 Expected Output

```text
Scanning APK Directory...

Found 2 APK Files

Uploading:
diva-beta.apk

Uploading:
InsecureBankv2.apk

Scanning...

Completed

Generating Summary Report...

Done
```

---

# 🔹 Step 4.2 — Create an APK Comparison Report

Create the comparison script.

```bash
cat > compare_apks.py << 'EOF'

(Paste the provided Python template here)

EOF
```

---

Grant execution permission.

```bash
chmod +x compare_apks.py
```

---

# 🧩 Script Overview

The comparison tool evaluates multiple MobSF reports and identifies:

* Best security score
* Worst security score
* Most common vulnerabilities
* Shared weaknesses
* Overall security posture

---

# 📌 Function — `compare_security_scores()`

Implement:

```python
compare_security_scores()
```

Responsibilities:

* 📊 Extract each application's security score
* 📋 Rank applications from highest to lowest
* 🏆 Identify the most secure application

---

# 📌 Function — `compare_vulnerabilities()`

Implement:

```python
compare_vulnerabilities()
```

The comparison should include:

* 🔴 High Severity Issues
* 🟠 Medium Severity Issues
* 🟡 Low Severity Issues
* 🔵 Informational Findings

Also identify vulnerabilities common to multiple applications.

---

# 📌 Function — `generate_comparison_report()`

Implement:

```python
generate_comparison_report()
```

Generate an HTML report containing:

* 📊 Security score comparison
* 📱 Application inventory
* 🚨 Vulnerability comparison matrix
* 📈 Charts or tables (optional)
* 💡 Security recommendations

---

### 📈 Comparison Workflow

```text
Multiple Reports
        │
        ▼
Load JSON Files
        │
        ▼
Compare Scores
        │
        ▼
Compare Findings
        │
        ▼
Generate HTML Report
```

---

# 🔹 Execute the Comparison Tool

Run:

```bash
python3 compare_apks.py
```

---

### 📋 Expected Output

```text
Loading Reports...

Comparing Security Scores...

Generating Comparison Report...

comparison_report.html created successfully.
```

---

# 🎯 Expected Outcomes

After completing this lab, you should have:

## 🛠 Functional Security Tools

* ✅ Working MobSF installation
* ✅ APK upload automation
* ✅ Scan monitoring tool
* ✅ JSON result extractor
* ✅ HTML report generator
* ✅ Batch scanning automation
* ✅ APK comparison tool

---

## 📄 Professional Reports

Generated reports should include:

* 📑 Static Analysis Report
* 📑 JSON Scan Results
* 📑 HTML Security Assessment
* 📑 Batch Scan Summary
* 📑 APK Comparison Report

---

## 🔍 Typical Findings (DIVA)

Expected observations include:

| Finding                 | Expected Result |
| ----------------------- | --------------- |
| 📊 Security Score       | 20–30 / 100     |
| 🔴 High Severity Issues | 10–15           |
| ⚠ Dangerous Permissions | 5–8             |
| 🔐 Hardcoded Secrets    | Present         |
| 💾 Insecure Storage     | Present         |
| 🌐 Cleartext Traffic    | Present         |
| 🔑 Weak Cryptography    | Present         |
| 📡 Exported Components  | Present         |

---

# 🛡 Security Best Practices

When reviewing MobSF findings, prioritize the following improvements:

* 🔐 Remove hardcoded credentials and secrets.
* 🌐 Enforce HTTPS and secure TLS configurations.
* 🔑 Replace weak cryptographic algorithms with modern alternatives.
* 📱 Disable unnecessary exported components.
* 📂 Minimize dangerous Android permissions.
* 💾 Encrypt sensitive data stored on the device.
* 🔄 Regularly update third-party libraries.
* 🧪 Integrate static analysis into the secure development lifecycle.

---

# 🐞 Troubleshooting

## ❌ MobSF Server Won't Start

Possible causes:

* Virtual environment not activated
* Port **8000** already in use
* Missing dependencies

Check port usage:

```bash
sudo lsof -i :8000
```

Review MobSF logs for additional details.

---

## ❌ APK Upload Fails

Verify:

* APK size is within supported limits.
* File is a valid Android APK.
* MobSF server is running.
* Network connectivity is available.

---

## ❌ Scan Takes Too Long

Large applications may require additional time.

Recommendations:

* Increase available RAM.
* Reduce concurrent scans.
* Wait for analysis to complete before requesting reports.

---

## ❌ API Returns Empty Results

Verify:

* The scan has completed successfully.
* The correct file hash is being used.
* The proper API endpoint is called.
* The JSON response is valid.

---

# 📚 Skills Gained

After completing this lab, you can confidently:

## 📱 Mobile Security

* ✔ Install and configure MobSF
* ✔ Perform Android static analysis
* ✔ Interpret vulnerability findings
* ✔ Evaluate application security posture

---

## 🤖 Security Automation

* ✔ Automate APK uploads
* ✔ Trigger scans through REST APIs
* ✔ Monitor analysis progress
* ✔ Process multiple applications concurrently

---

## 📊 Security Reporting

* ✔ Generate JSON reports
* ✔ Create HTML assessment reports
* ✔ Compare multiple APKs
* ✔ Prioritize remediation activities

---

# 🚀 Next Steps

Continue building your mobile application security expertise by exploring:

* 📱 Dynamic Analysis with MobSF
* 🔍 Runtime Instrumentation (Frida)
* 🛡 OWASP Mobile Security Testing Guide (MSTG)
* 📦 Android Reverse Engineering
* 🔐 Secure Mobile Development Practices
* 🤖 CI/CD Security Automation
* ☁ Cloud-based Mobile Security Testing

---

# 📖 Conclusion

This lab provided hands-on experience with the **Mobile Security Framework (MobSF)** for automated Android application security assessment. You learned how to install and configure MobSF, perform static analysis on APK files, automate interactions through the REST API, retrieve and interpret scan results, and generate professional security reports. By extending the workflow to support batch processing and comparative analysis, you established a scalable approach to assessing multiple mobile applications efficiently.

These practical skills are directly applicable to mobile penetration testing, secure application development, vulnerability management, and DevSecOps workflows, enabling organizations to identify security weaknesses early and improve the overall security posture of Android applications.

---

<div align="center">

# 🎉 Congratulations!

You have successfully completed the

# 📱 **Scan Apps with MobSF and Analyze Findings**

### Mobile Application Security Assessment Lab

---

## 🏆 What You Accomplished

✅ Installed and Configured **MobSF**

✅ Performed **Static APK Analysis**

✅ Automated **MobSF REST API Workflows**

✅ Retrieved and Interpreted **Security Findings**

✅ Generated **Professional HTML & JSON Reports**

✅ Built **Batch APK Scanning Automation**

✅ Created **Comparative Security Assessment Reports**

---

### 🚀 Keep Practicing • Keep Automating • Build More Secure Mobile Applications

**Happy Hacking & Secure Coding! 🔐**

</div>

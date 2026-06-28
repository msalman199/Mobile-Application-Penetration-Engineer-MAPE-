# 📱 Modify App Behavior Using Frida's CLI Toolkit

<div align="center">

# 🛡️ Al Razzaq Certified Mobile Application Penetration Engineer (CMAPE)

### **Dynamic Android Application Instrumentation using Frida CLI**

![Android](https://img.shields.io/badge/Platform-Android-3DDC84?style=for-the-badge\&logo=android\&logoColor=white)
![Frida](https://img.shields.io/badge/Frida-Dynamic%20Instrumentation-EF6C00?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Frida%20Scripts-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![ADB](https://img.shields.io/badge/ADB-Android%20Debug%20Bridge-34A853?style=for-the-badge)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Bash-FCC624?style=for-the-badge\&logo=linux\&logoColor=black)
![Security](https://img.shields.io/badge/Mobile-Penetration%20Testing-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-blue?style=for-the-badge)

</div>

---

# 📖 Overview

This hands-on lab introduces students to **Frida's Command-Line Toolkit** for Android application penetration testing. Throughout the exercises, students will dynamically instrument Android applications, intercept runtime method calls, modify application behavior, automate security testing with Python, and discover common mobile application vulnerabilities.

Unlike static reverse engineering, Frida allows researchers to **observe and manipulate applications while they are running**, making it one of the most powerful tools used during professional mobile application security assessments.

> ⚠️ **Educational Use Only**
>
> The techniques demonstrated in this lab must only be performed against applications and devices that you own or are explicitly authorized to test.

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

* ✅ Install and configure Frida CLI Toolkit
* ✅ Hook Android Java methods at runtime
* ✅ Modify application behavior dynamically
* ✅ Analyze application security controls
* ✅ Develop reusable Frida JavaScript hooks
* ✅ Automate penetration testing using Python
* ✅ Understand runtime instrumentation techniques

---

# 🛠 Technology Stack

| Technology                    | Purpose                        |
| ----------------------------- | ------------------------------ |
| 🤖 Android                    | Target Mobile Platform         |
| 🔥 Frida CLI                  | Runtime Instrumentation        |
| 🐍 Python 3.8+                | Automation Framework           |
| 📜 JavaScript                 | Frida Hook Development         |
| 📱 Android Debug Bridge (ADB) | Device Communication           |
| 💻 Ubuntu Linux               | Lab Environment                |
| 🧪 InsecureBankv2             | Vulnerable Android Application |
| 📂 Bash                       | Command-Line Operations        |

---

# 📚 Prerequisites

Before beginning this lab, students should have:

* ✔️ Basic Linux command-line knowledge
* ✔️ Android application architecture fundamentals
* ✔️ JavaScript syntax familiarity
* ✔️ Python programming basics
* ✔️ Mobile application security concepts
* ✔️ Understanding of Android Activities and Components

---

# 🖥️ Lab Environment

Your cloud lab environment includes:

| Component                | Description         |
| ------------------------ | ------------------- |
| 🐧 Ubuntu 20.04 LTS      | Operating System    |
| 🔥 Frida Toolkit         | Pre-installed       |
| 📱 Android Emulator      | Configured          |
| 🔌 Android Debug Bridge  | Ready to Use        |
| 🐍 Python 3.8+           | With Frida Bindings |
| 📦 InsecureBankv2.apk    | Vulnerable Target   |
| 🛠 Required Dependencies | Installed           |

Everything has already been configured for you.

---

# 📂 Lab Directory Structure

```text
frida-lab/
│
├── login_hook.js
├── advanced_hook.js
├── vulnerability_scanner.js
├── auth_bypass.js
├── validation_bypass.js
│
├── frida_automation.py
├── advanced_testing_suite.py
├── continuous_testing.py
│
└── InsecureBankv2.apk
```

---

# 🚩 Task 1 — Configure Frida and Hook Application Methods

---

# 🔹 Step 1 — Verify Environment & Launch Target Application

## 🎯 Objective

Verify that Frida is installed correctly and prepare the Android testing environment.

---

## 📌 Verify Frida Installation

```bash
frida --version

python3 -c "import frida; print(frida.__version__)"
```

---

## 📌 Start Android Emulator

```bash
emulator -avd test_device -no-snapshot-load &
sleep 120
```

---

## 📌 Verify Device Connection

```bash
adb devices
```

Expected Output

```text
List of devices attached

emulator-5554 device
```

---

## 📌 Install Target Application

```bash
cd ~/Downloads

adb install InsecureBankv2.apk
```

---

## 📌 Launch Application

```bash
adb shell am start -n \
com.android.insecurebankv2/.PostLogin
```

---

## 📌 Verify Running Process

```bash
frida-ps -U | grep insecurebank
```

---

### ✅ Success Criteria

You should confirm:

* ✔ Frida installed correctly
* ✔ Emulator running
* ✔ ADB device connected
* ✔ Application installed
* ✔ Target process visible

---

# 🔹 Step 2 — Create Your First Frida Hook

## 🎯 Objective

Create a JavaScript hook to intercept Android login methods.

---

## 📁 Create Working Directory

```bash
mkdir -p ~/frida_scripts

cd ~/frida_scripts
```

---

## 📄 Create Script

```bash
nano login_hook.js
```

---

## 🧩 Starter Template

```javascript
Java.perform(function() {

    console.log("[+] Frida Script Loaded");

    // TODO:
    // Obtain PostLogin class

    // var LoginActivity =
    // Java.use("com.android.insecurebankv2.PostLogin");

    // TODO:
    // Hook performLogin()

    // TODO:
    // Log username

    // TODO:
    // Log password

    // TODO:
    // Call original method

    console.log("[+] Hook Installed");

});
```

---

## 🎓 Student Exercise

Complete the following tasks:

* 🔹 Reference the **PostLogin** activity
* 🔹 Hook **performLogin()**
* 🔹 Capture usernames
* 🔹 Capture passwords
* 🔹 Execute original function
* 🔹 Return original response

---

## 🎯 Learning Outcome

After this step you should understand:

* ✔ Java.perform()
* ✔ Java.use()
* ✔ Method implementation replacement
* ✔ Runtime interception
* ✔ Original method invocation

---

# 🔹 Step 3 — Execute Hook Script

## 🎯 Objective

Inject your Frida script into the running Android application.

---

## 🚀 Spawn Application with Injection

```bash
frida -U \
-f com.android.insecurebankv2 \
-l login_hook.js \
--no-pause
```

---

## 🚀 Attach to Running Application

```bash
frida -U \
com.android.insecurebankv2 \
-l login_hook.js
```

---

## 🧪 Testing Procedure

Inside the application:

1. Enter username
2. Enter password
3. Press Login

Observe the Frida console.

---

## Expected Behavior

```text
[+] Frida Script Loaded

Username : admin

Password : password123

[+] Hook Installed
```

---

### ✅ Success Criteria

* ✔ Script loads successfully
* ✔ Login function intercepted
* ✔ Credentials captured
* ✔ Application continues normally

---

# 🔹 Step 4 — Create Advanced Multi-Method Hooks

## 🎯 Objective

Expand your instrumentation to multiple security-sensitive methods.

---

## 📄 Create Script

```bash
nano advanced_hook.js
```

---

## 🧩 Starter Template

```javascript
Java.perform(function(){

    console.log("[+] Advanced Hook Started");

    try{

        // TODO
        // Hook Authentication

        // TODO
        // Hook Crypto

        // TODO
        // Hook SharedPreferences

    }

    catch(error){

        console.log(error);

    }

});
```

---

## 🎯 Hook Targets

### 🔐 Authentication

Intercept

```text
performLogin()
```

Goal

* Capture credentials
* Modify authentication
* Observe login logic

---

### 🔑 Cryptography

Intercept

```text
CryptoClass.encrypt()
```

Goal

* Observe plaintext
* Analyze encryption usage
* Modify returned values

---

### 💾 SharedPreferences

Intercept

```text
putString()
```

Goal

* Log sensitive values
* Detect insecure storage
* Monitor saved credentials

---

## 🎓 Student Exercise

Implement hooks that:

* ✔ Modify authentication behavior
* ✔ Inspect encryption
* ✔ Capture stored secrets
* ✔ Preserve application functionality

---

## 📌 Expected Console Output

```text
[+] Authentication Hooked

Username : admin

Password : password123

Encryption Input :

SensitiveData

SharedPreference

token = eyJhbGciOi...

```

---

# 🔹 Step 5 — Test Advanced Hooks

## 🎯 Objective

Validate runtime behavior modifications using Frida.

---

## 🚀 Execute Script

```bash
frida -U \
-f com.android.insecurebankv2 \
-l advanced_hook.js \
--no-pause
```

---

## 🧪 Test Scenarios

Perform the following actions:

* 🔐 Login
* 💾 Save application settings
* 🔑 Trigger encryption
* 📱 Navigate application features

---

## Observe

Watch for:

* ✔ Authentication interception
* ✔ Encryption hooks
* ✔ Stored secrets
* ✔ Runtime behavior changes

---

## ✅ Expected Results

You should successfully:

* Capture authentication attempts
* Monitor cryptographic operations
* Observe SharedPreferences writes
* Modify application behavior dynamically

---

# 🎉 Task 1 Complete

Congratulations!

You have successfully:

* ✅ Installed and verified Frida CLI
* ✅ Connected to an Android emulator
* ✅ Hooked Android Java methods
* ✅ Intercepted login functionality
* ✅ Created multi-method hooks
* ✅ Modified application behavior during runtime

---

➡️ **Continue with Part 2**, where you'll build vulnerability scanners, implement authentication bypass techniques, and exploit common mobile application security weaknesses using Frida.

# 🚩 Task 2 — Identify and Exploit Application Vulnerabilities

---

# 🔍 Overview

In this task, you will use **Frida's dynamic instrumentation capabilities** to identify common Android security weaknesses and observe how runtime hooks can reveal insecure application behavior. You will also build scripts to analyze authentication logic and input validation mechanisms.

> ⚠️ **Important**
>
> These exercises are intended for **authorized security testing and defensive education only**. The goal is to understand application behavior and identify weaknesses in a controlled lab environment.

---

# 🔹 Step 1 — Create a Vulnerability Scanner

## 🎯 Objective

Develop a Frida script that monitors security-sensitive API usage and reports potential vulnerabilities.

---

## 📄 Create the Script

```bash
nano vulnerability_scanner.js
```

---

## 🧩 Starter Template

```javascript
Java.perform(function () {

    console.log("[+] Vulnerability Scanner Started");

    // TODO
    // Hook SharedPreferences

    // TODO
    // Hook HttpURLConnection

    // TODO
    // Hook WebView.loadUrl()

    console.log("[+] Scanner Hooks Installed");

});
```

---

## 🎯 Security Checks

### 💾 Check 1 — Insecure Data Storage

Hook:

```text
SharedPreferences.Editor.putString()
```

Look for sensitive information such as:

* 🔑 Passwords
* 🎟 Tokens
* 🔐 API Keys
* 🍪 Session IDs
* 👤 User Credentials

---

### 🌐 Check 2 — Insecure Network Communication

Hook:

```text
HttpURLConnection.setRequestMethod()
```

Monitor requests for:

* HTTP instead of HTTPS
* Plaintext communication
* Weak transport security

---

### 🌍 Check 3 — Unsafe WebView Usage

Hook:

```text
WebView.loadUrl()
```

Detect:

* javascript: URLs
* Dynamic script execution
* Potential XSS vectors

---

## 🎓 Student Exercise

Complete the script so it can:

* ✅ Monitor SharedPreferences
* ✅ Detect sensitive information
* ✅ Inspect HTTP requests
* ✅ Monitor WebView activity
* ✅ Display findings in the Frida console

---

## 📌 Example Console Output

```text
[+] Scanner Started

[!] Sensitive Value Stored

Key:
password

Value:
admin123

--------------------------------

[!] HTTP Connection Detected

http://example.com/login

--------------------------------

[!] JavaScript URL Loaded

javascript:alert(document.cookie)
```

---

## ✅ Success Criteria

✔ Storage monitoring works

✔ HTTP requests detected

✔ WebView URLs monitored

✔ Sensitive values identified

---

# 🔹 Step 2 — Analyze Authentication Logic

## 🎯 Objective

Observe how authentication-related methods operate during runtime and identify where credential validation occurs.

---

## 📄 Create Script

```bash
nano auth_analysis.js
```

---

## 🧩 Starter Template

```javascript
Java.perform(function(){

    console.log("[+] Authentication Analysis Started");

    // TODO

    // Enumerate loaded classes

    // Identify authentication classes

    // Monitor credential validation

});
```

---

## 🔍 Investigation Goals

Locate classes containing names similar to:

```text
Login

Authentication

Auth

User

Credential

Session
```

Observe methods responsible for:

* Username validation
* Password comparison
* Session generation
* Token creation
* Login status

---

## 🎓 Student Exercise

Complete the script to:

* 🔹 Enumerate loaded classes
* 🔹 Filter authentication-related classes
* 🔹 Monitor credential verification
* 🔹 Record authentication flow

---

## 📌 Expected Output

```text
Authentication Class Found

com.android.insecurebankv2.LoginManager

--------------------------------

Method Invoked

checkUserCredentials()

--------------------------------

Username

admin

Password

********
```

---

## ✅ Success Criteria

✔ Authentication classes identified

✔ Validation methods observed

✔ Runtime credential flow understood

---

# 🔹 Step 3 — Analyze Input Validation

## 🎯 Objective

Study how Android applications validate and sanitize user input.

---

## 📄 Create Script

```bash
nano validation_analysis.js
```

---

## 🧩 Starter Template

```javascript
Java.perform(function(){

    console.log("[+] Validation Analysis Started");

    // TODO

    // Hook String.matches()

    // Hook replaceAll()

    // Hook String.length()

});
```

---

## 🔍 Monitor Validation Functions

### ✔ Regular Expression Checks

Observe

```text
String.matches()
```

Identify:

* Email validation
* Password complexity
* Username restrictions
* Input filtering

---

### ✔ Sanitization

Observe

```text
String.replaceAll()
```

Detect:

* Character filtering
* HTML sanitization
* SQL sanitization
* Input normalization

---

### ✔ Length Validation

Observe

```text
String.length()
```

Understand how applications enforce:

* Username length
* Password length
* PIN length
* Form restrictions

---

## 🎓 Student Exercise

Implement hooks that:

* Monitor regex validation
* Display validation patterns
* Observe sanitization logic
* Record length checks

---

## 📌 Expected Output

```text
Regex Validation

^[A-Za-z0-9]{8,20}$

-------------------------

replaceAll()

Pattern

<.*?>

-------------------------

Input Length

32
```

---

## ✅ Success Criteria

✔ Validation logic observed

✔ Sanitization functions monitored

✔ Length restrictions identified

---

# 🔹 Step 4 — Execute Security Analysis

## 🎯 Objective

Run your monitoring scripts and document discovered security findings.

---

## ▶ Run Vulnerability Scanner

```bash
frida -U com.android.insecurebankv2 \
-l vulnerability_scanner.js
```

---

## ▶ Run Authentication Analysis

```bash
frida -U com.android.insecurebankv2 \
-l auth_analysis.js
```

---

## ▶ Run Validation Analysis

```bash
frida -U com.android.insecurebankv2 \
-l validation_analysis.js
```

---

## 🧪 Testing Activities

Perform the following actions inside the application:

* 🔑 Login
* 📱 Navigate menus
* 💾 Save settings
* 🌐 Trigger network requests
* 📝 Submit forms
* 🔍 Use search functionality

---

## 📋 Document Findings

Record observations including:

| Category          | Observation        |
| ----------------- | ------------------ |
| 🔐 Authentication | Validation methods |
| 💾 Storage        | Sensitive values   |
| 🌐 Network        | HTTP/HTTPS usage   |
| 🌍 WebView        | JavaScript URLs    |
| 📝 Validation     | Regex patterns     |
| 🧼 Sanitization   | Input filtering    |
| 📏 Length Checks  | Restrictions       |

---

# 📊 Expected Results

By the end of Task 2 you should be able to identify:

* ✅ Authentication workflows
* ✅ Sensitive data storage
* ✅ Network communication patterns
* ✅ WebView behavior
* ✅ Input validation mechanisms
* ✅ Sanitization routines
* ✅ Potential security weaknesses

---

# 🔍 Key Observations

During analysis you should notice:

* 🔥 Authentication decisions occur at runtime.
* 🔑 Sensitive information may be written to local storage.
* 🌐 Applications often expose valuable networking information.
* 📱 WebView components can reveal client-side behavior.
* 📝 Validation logic becomes visible through runtime instrumentation.
* 📊 Dynamic analysis complements static reverse engineering.

---

# 💡 Best Practices

While performing runtime analysis:

* ✔ Monitor only relevant methods.
* ✔ Log meaningful security events.
* ✔ Avoid excessive hooks that impact performance.
* ✔ Keep scripts modular and reusable.
* ✔ Document all findings for later review.
* ✔ Validate observations through repeated testing.

---

# 🎉 Task 2 Complete

Congratulations!

You have successfully:

* ✅ Built a runtime vulnerability scanner
* ✅ Monitored sensitive storage APIs
* ✅ Analyzed authentication workflows
* ✅ Investigated input validation logic
* ✅ Observed network communication
* ✅ Documented security-relevant application behavior

---

➡️ **Continue with Part 3**, where you'll automate Frida operations using Python, build an advanced testing framework, and implement continuous security monitoring.
# 🚩 Task 3 — Automate Frida Testing with Python

---

# 🤖 Overview

In this task, you will combine **Frida** with **Python** to build an automated mobile application security testing framework.

Rather than manually launching Frida scripts every time, Python will automate:

* 📱 Application startup
* 🔌 Device connection
* 🔥 Frida attachment
* 📜 Script loading
* 📊 Result collection
* 📝 Security reporting

Automation dramatically improves the speed and consistency of mobile penetration testing.

---

# 🔹 Step 1 — Build a Python Automation Framework

## 🎯 Objective

Create a reusable Python framework capable of managing Frida sessions and executing JavaScript hooks automatically.

---

## 📄 Create the Automation Script

```bash
nano frida_automation.py
```

---

## 🧩 Framework Structure

Your framework should include:

```text
FridaAutomation

│

├── connect_device()

├── start_application()

├── attach_to_process()

├── load_script()

├── on_message()

└── run_automated_test()
```

---

## 📦 Required Python Modules

```python
import frida
import sys
import time
import subprocess
```

---

## 🎯 Implement Device Connection

Complete

```python
connect_device()
```

Responsibilities:

* 🔌 Connect to Android device
* 📱 Verify USB connection
* ⚠ Handle connection errors
* ✅ Return connection status

---

## 🚀 Launch Target Application

Complete

```python
start_application()
```

Responsibilities

* Launch application using ADB
* Wait for initialization
* Verify startup

---

## 🔥 Attach Frida

Complete

```python
attach_to_process()
```

Responsibilities

* Attach Frida session
* Store session object
* Handle failures

---

## 📜 Load JavaScript Hooks

Complete

```python
load_script()
```

Responsibilities

* Read JS file
* Create Frida script
* Register callback
* Execute hook

---

## 📨 Receive Messages

Complete

```python
on_message()
```

Process:

* send()
* errors
* console output
* logging

---

## 🎮 Run Automation

Complete

```python
run_automated_test()
```

Workflow

```text
Connect Device

↓

Launch App

↓

Attach Frida

↓

Load Script

↓

Collect Results

↓

Exit Cleanly
```

---

## ▶ Execute Framework

```bash
python3 frida_automation.py \
com.android.insecurebankv2 \
login_hook.js
```

---

## ✅ Expected Result

```text
[+] Device Connected

[+] Application Started

[+] Attached Successfully

[+] Script Loaded

[+] Monitoring...
```

---

# 🔹 Step 2 — Build an Advanced Security Testing Suite

## 🎯 Objective

Create a reusable testing framework capable of executing multiple Frida-based security tests.

---

## 📄 Create Script

```bash
nano advanced_testing_suite.py
```

---

## 🏗 Framework Design

```text
AdvancedFridaTestSuite

│

├── test_authentication()

├── test_crypto()

├── test_storage()

├── execute_test()

├── run_all_tests()

└── generate_report()
```

---

## 🔐 Authentication Test

Create

```python
test_authentication()
```

Purpose

* Monitor login logic
* Observe credential handling
* Detect authentication workflow

---

## 🔑 Cryptography Test

Create

```python
test_crypto()
```

Purpose

* Observe encryption APIs
* Monitor sensitive data
* Analyze crypto implementation

---

## 💾 Data Storage Test

Create

```python
test_storage()
```

Purpose

* Monitor SharedPreferences
* Detect stored secrets
* Identify insecure storage

---

## ▶ Execute Individual Test

Implement

```python
execute_test()
```

Responsibilities

* Attach Frida
* Load script
* Receive events
* Return results

---

## 📊 Execute Complete Test Suite

Implement

```python
run_all_tests()
```

Workflow

```text
Launch Application

↓

Authentication Test

↓

Crypto Test

↓

Storage Test

↓

Generate Report
```

---

## 📑 Generate Report

Implement

```python
generate_report()
```

The report should include

* Test Name
* Findings
* Severity
* Recommendations
* Timestamp

---

## ▶ Execute Test Suite

```bash
python3 advanced_testing_suite.py \
com.android.insecurebankv2
```

---

## 📋 Example Output

```text
Authentication Test

PASS

----------------------

Crypto Test

PASS

----------------------

Storage Test

WARNING

Sensitive Token Found

----------------------

JSON Report Saved
```

---

# 🔹 Step 3 — Implement Continuous Security Monitoring

## 🎯 Objective

Develop a monitoring solution that continuously scans the target application for security-relevant activity.

---

## 📄 Create Script

```bash
nano continuous_testing.py
```

---

## 🏗 Framework Structure

```text
ContinuousFridaTesting

│

├── monitor_application()

├── is_app_running()

├── run_security_scan()

└── log_results()
```

---

## ⏱ Continuous Monitoring Loop

Implement

```python
monitor_application()
```

Responsibilities

* Infinite monitoring loop
* Verify application status
* Launch scans
* Sleep between scans

---

## 📱 Verify Application Status

Complete

```python
is_app_running()
```

Tasks

* Query ADB
* Verify process
* Return Boolean

---

## 🔍 Security Scan

Implement

```python
run_security_scan()
```

Scan for

* 🔑 Authentication activity
* 💾 Sensitive storage
* 🌐 Network requests
* 🔒 Cryptographic operations
* 📜 Runtime hooks

---

## 📝 Logging

Implement

```python
log_results()
```

Store

* Timestamp
* Findings
* Severity
* Test Count
* Device Status

---

## ▶ Start Continuous Monitoring

```bash
python3 continuous_testing.py \
com.android.insecurebankv2 \
300
```

(Default interval: 5 minutes)

---

## 📋 Sample Output

```text
Monitoring Started

-------------------

Scan #1

No Critical Findings

-------------------

Scan #2

Sensitive Data Stored

Severity

Medium

-------------------

Results Logged
```

---

# 📊 Expected Outcomes

After completing Task 3 you should have created:

* ✅ Python automation framework
* ✅ Automated Frida launcher
* ✅ JavaScript execution manager
* ✅ Multi-test security suite
* ✅ Continuous monitoring system
* ✅ Automated report generation
* ✅ Reusable penetration testing workflow

---

# 💡 Best Practices

While automating Frida:

* ✔ Keep scripts modular.
* ✔ Separate JavaScript from Python.
* ✔ Handle exceptions gracefully.
* ✔ Record all findings.
* ✔ Reuse common helper functions.
* ✔ Store reports in structured formats.
* ✔ Validate device connectivity before execution.

---

# 🎉 Task 3 Complete

Congratulations!

You have successfully built:

* 🤖 A Python-based Frida automation framework
* 🔥 Automated Frida script execution
* 📱 Android application monitoring
* 📊 Security reporting capabilities
* 🔍 Continuous security scanning
* 📋 A reusable mobile penetration testing toolkit

Your automation framework now provides a solid foundation for scaling dynamic Android application security assessments and integrating Frida into larger penetration testing workflows.

---

➡️ **Continue with Part 4**, where you'll execute the complete automation workflow, review expected outcomes, troubleshoot common issues, explore defensive recommendations, and conclude the lab with best practices and next steps.

# 🚩 Task 4 — Execute the Automated Testing Framework

---

# 🎯 Objective

Validate the complete Frida automation framework by executing all developed scripts, reviewing generated findings, and confirming that the testing workflow operates correctly from start to finish.

---

# 🔹 Step 1 — Prepare the Environment

Before running the automation framework, make sure all Python scripts are executable.

```bash
chmod +x frida_automation.py
chmod +x advanced_testing_suite.py
chmod +x continuous_testing.py
```

---

# 🔹 Step 2 — Execute Basic Automation

Run the automation framework with your login hook.

```bash
python3 frida_automation.py \
com.android.insecurebankv2 \
login_hook.js
```

### ✅ Expected Output

```text
[+] Device Connected

[+] Application Started

[+] Attached Successfully

[+] Script Loaded

[+] Waiting For Events...
```

---

# 🔹 Step 3 — Execute Complete Testing Suite

Launch the comprehensive security testing framework.

```bash
python3 advanced_testing_suite.py \
com.android.insecurebankv2
```

The framework should automatically perform:

* 🔐 Authentication Analysis
* 🔑 Cryptography Monitoring
* 💾 Sensitive Storage Detection
* 🌐 Runtime Activity Collection
* 📊 Report Generation

---

# 🔹 Step 4 — Start Continuous Monitoring

Launch long-term monitoring.

```bash
python3 continuous_testing.py \
com.android.insecurebankv2 \
300
```

The framework performs automated scans every **300 seconds** (5 minutes).

Example output:

```text
Scan #1

Application Running

No Critical Findings

----------------------------

Scan #2

Sensitive Token Detected

Medium Severity

----------------------------

Results Saved
```

---

# 📊 Expected Lab Outcomes

After completing this lab you should have successfully:

* ✅ Configured Frida CLI Toolkit
* ✅ Connected Frida to Android applications
* ✅ Created JavaScript runtime hooks
* ✅ Intercepted authentication methods
* ✅ Monitored cryptographic operations
* ✅ Detected insecure storage
* ✅ Observed application runtime behavior
* ✅ Built reusable Frida scripts
* ✅ Developed Python automation frameworks
* ✅ Generated security reports
* ✅ Implemented continuous monitoring

---

# 🔍 Key Learning Points

Throughout this lab you discovered that:

* 🔥 Frida enables runtime instrumentation without modifying APK files.
* 📱 Android applications expose valuable runtime information through Java APIs.
* 🔐 Authentication logic can be observed during execution.
* 🔑 Cryptographic operations can be analyzed dynamically.
* 💾 Sensitive information may be written to local storage.
* 🐍 Python greatly improves testing efficiency through automation.
* 📊 Continuous monitoring helps identify security issues over time.

---

# 🛠 Troubleshooting Guide

---

## ❌ Frida Cannot Connect to Device

### Verify Device

```bash
adb devices
```

Expected

```text
emulator-5554 device
```

---

### Restart ADB

```bash
adb kill-server

adb start-server
```

---

### Verify Frida

```bash
frida --version

frida-ps -U
```

---

### Check Emulator

Ensure:

* ✔ Emulator is running
* ✔ USB debugging is enabled
* ✔ Device is visible in ADB

---

## ❌ Hook Not Triggering

Possible causes:

* Incorrect class name
* Incorrect method name
* Wrong package
* Script loaded before Java runtime
* Application obfuscation

Recommendations:

* Verify class names using JADX.
* Use `Java.perform()` correctly.
* Confirm the application process is running.
* Validate package identifiers.

---

## ❌ JavaScript Errors

Check for:

* Missing semicolons
* Incorrect method signatures
* Wrong parameter count
* Invalid return types
* Syntax mistakes

Use:

```javascript
try{

   // Hook

}

catch(error){

   console.log(error);

}
```

---

## ❌ Python Import Errors

Verify Python version.

```bash
python3 --version
```

Install Frida bindings.

```bash
pip3 install frida-tools
```

Confirm installation.

```bash
python3 -c "import frida"
```

---

## ❌ Application Closes Unexpectedly

Possible causes:

* Invalid hook implementation
* Hooking incorrect overload
* Returning wrong object type
* Runtime exceptions

Recommendations:

* Hook one method at a time.
* Test incrementally.
* Review Frida console logs.
* Add proper exception handling.

---

# 📋 Best Practices

When performing runtime instrumentation:

* ✔ Hook only required methods.
* ✔ Keep JavaScript hooks modular.
* ✔ Separate automation from hook logic.
* ✔ Record meaningful events.
* ✔ Store reports in JSON or CSV.
* ✔ Handle all runtime exceptions.
* ✔ Reuse common helper functions.
* ✔ Document every security finding.

---

# 🛡 Defensive Recommendations

Mobile application developers should consider implementing:

* 🔒 Runtime integrity verification
* 🔍 Frida detection techniques
* 📱 Emulator detection
* 🛡 Root detection
* 🔑 Strong cryptographic implementations
* 🌐 Secure network communications
* 📦 Secure local storage
* 🔐 Certificate Pinning
* 🧩 Code obfuscation
* 📊 Runtime monitoring and anomaly detection

These controls increase resistance against dynamic instrumentation and runtime analysis.

---

# 🚀 Next Steps

Expand your knowledge by exploring:

* 📱 Advanced Frida JavaScript APIs
* 🔥 Native function hooking
* ⚙ Hooking JNI methods
* 🧬 ARM64 native instrumentation
* 🔍 Android Binder interception
* 📊 Automated mobile security pipelines
* 🤖 Continuous mobile penetration testing
* 🛡 Anti-Frida detection bypass research
* 📦 Runtime malware analysis
* 📱 Real-world Android application assessments (with authorization)

---

# 🏆 Skills Gained

After completing this lab you have developed practical experience with:

* ✅ Frida CLI Toolkit
* ✅ Android Runtime Instrumentation
* ✅ Java Method Hooking
* ✅ Dynamic Security Analysis
* ✅ Authentication Analysis
* ✅ Cryptography Monitoring
* ✅ Sensitive Data Discovery
* ✅ JavaScript Hook Development
* ✅ Python Automation
* ✅ Mobile Penetration Testing
* ✅ Continuous Security Monitoring
* ✅ Automated Report Generation

---

# 📚 Summary

This laboratory introduced the practical use of **Frida's CLI Toolkit** for dynamic Android application security testing.

During the exercises you learned how to:

* 🔥 Instrument Android applications at runtime
* 📱 Observe application behavior without modifying the APK
* 🔐 Monitor authentication mechanisms
* 🔑 Analyze cryptographic operations
* 💾 Detect insecure data storage
* 🐍 Automate testing with Python
* 📊 Build reusable penetration testing frameworks
* 🛡 Generate structured security findings

These techniques form an essential foundation for professional Android application penetration testing and security research.

---

# ⚖️ Ethical Use Notice

> **This lab is provided exclusively for educational purposes, authorized penetration testing, security research, and defensive assessments.**
>
> Only perform these techniques against applications, devices, or environments for which you have explicit written authorization. Unauthorized testing may violate organizational policies and applicable laws.

---

<div align="center">

# 🎉 Congratulations!

## 🏅 Lab Successfully Completed

You have completed the **Modify App Behavior Using Frida's CLI Toolkit** lab.

You now possess the foundational skills required to perform dynamic Android application instrumentation using **Frida**, develop **Python automation frameworks**, and conduct professional **mobile application penetration testing**.

### 🚀 Happy Ethical Hacking!

**Al Razzaq Certified Mobile Application Penetration Engineer (CMAPE)**

</div>


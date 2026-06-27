# 📱 Abuse Exposed Components via Drozer

<div align="center">

![Android](https://img.shields.io/badge/Platform-Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Drozer](https://img.shields.io/badge/Tool-Drozer-blue?style=for-the-badge)
![ADB](https://img.shields.io/badge/ADB-Platform--Tools-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![Linux](https://img.shields.io/badge/Linux-Ubuntu%2022.04-orange?style=for-the-badge&logo=ubuntu)
![Security](https://img.shields.io/badge/Mobile-Security-red?style=for-the-badge)

</div>

---

# 📖 Overview

Android applications expose multiple components that enable communication with other applications and the operating system. If these components are improperly configured or lack adequate access controls, they can become entry points for attackers.

This lab demonstrates how to use **Drozer**, one of the most widely used Android security assessment frameworks, to identify exposed components, interact with them, test for common weaknesses, and automate security assessments using Python.

> **Educational Purpose:** This lab is intended for authorized security testing and mobile application security training.

---

# 🎯 Objectives

After completing this lab you will be able to:

- ✅ Install and configure Drozer
- ✅ Connect Drozer to Android emulator
- ✅ Enumerate installed applications
- ✅ Discover exported Activities
- ✅ Discover exported Services
- ✅ Discover Broadcast Receivers
- ✅ Enumerate Content Providers
- ✅ Interact with exposed components
- ✅ Automate component discovery using Python
- ✅ Generate professional security reports
- ✅ Recommend remediation techniques

---

# 🧠 Skills You'll Gain

- Android Application Reconnaissance
- Component Enumeration
- Intent Manipulation
- ADB Usage
- Drozer Framework
- Python Automation
- Mobile Penetration Testing
- Security Reporting

---

# 🛠 Prerequisites

Before beginning this lab you should understand:

- Android application architecture
- Android components
- Linux command line
- Android Debug Bridge (ADB)
- Python programming basics
- Mobile application security fundamentals

---

# 💻 Lab Environment

The cloud lab includes:

- Ubuntu 22.04 LTS
- Android SDK
- Android Emulator
- ADB Platform Tools
- Python 3.x
- Drozer Framework
- Vulnerable Android Applications
- Internet Connectivity

---

# 🧰 Technologies Used

| Category | Technology |
|----------|------------|
| Mobile OS | Android |
| Framework | Drozer |
| Programming | Python 3 |
| Shell | Bash |
| Emulator | Android Emulator |
| Communication | ADB |
| Operating System | Ubuntu 22.04 |

---

# 📂 Lab Tasks

| Task | Description |
|------|-------------|
| Task 1 | Configure Drozer Environment |
| Task 2 | Discover Exposed Components |
| Task 3 | Interact with Components |
| Task 4 | Automate Testing with Python |

---

# 🚀 Task 1 — Environment Setup

---

# Step 1.1 Verify Android Environment

Confirm the Android SDK and emulator are functioning correctly.

### Check ADB Version

```bash
adb version
```

Expected output:

```text
Android Debug Bridge version 1.x.x
```

---

### List Connected Devices

```bash
adb devices
```

Example:

```text
List of devices attached

emulator-5554 device
```

---

### Start Emulator

```bash
emulator -avd test_device -no-snapshot &
```

Wait approximately 30 seconds.

```bash
adb devices
```

The emulator should now appear as an online device.

---

# ✅ Step 1.2 Install Drozer

Update package repositories.

```bash
sudo apt update
```

Install Python dependencies.

```bash
sudo apt install -y python3-pip python3-dev
```

Install Drozer.

```bash
pip3 install drozer
```

Verify installation.

```bash
drozer --help
```

Expected output displays available Drozer commands.

---

# ✅ Step 1.3 Install Drozer Agent

Download the Android Agent.

```bash
wget https://github.com/FSecureLABS/drozer/releases/download/2.4.4/drozer-agent-2.4.4.apk
```

Install it.

```bash
adb install drozer-agent-2.4.4.apk
```

Verify installation.

```bash
adb shell pm list packages | grep drozer
```

Forward Drozer communication port.

```bash
adb forward tcp:31415 tcp:31415
```

---

# 📱 Emulator Configuration

Inside Android Emulator:

1. Open **Drozer Agent**
2. Enable **Embedded Server**
3. Confirm server status

Expected message:

```text
Server started on port 31415
```

---

# ✅ Step 1.4 Connect to Drozer

Launch the console.

```bash
drozer console connect
```

Successful connection:

```text
dz>
```

Test communication.

```text
dz> run app.package.list
```

Drozer should return installed applications.

---

# 🎉 Task 1 Complete

At this point you have:

- Installed Drozer
- Installed the Android Agent
- Connected to Android Emulator
- Verified communication
- Prepared the assessment environment

- # 🔍 Task 2 — Identify Exposed Components

One of Drozer's most powerful capabilities is discovering Android application components that are unintentionally exposed. Exported components without proper permission checks may allow attackers to launch activities, communicate with services, trigger broadcast receivers, or access sensitive data through content providers.

---

# 🎯 Objective

In this task you will:

- Enumerate installed applications
- Identify exported Activities
- Discover exposed Services
- Locate Broadcast Receivers
- Enumerate Content Providers
- Determine attack surface for exploitation

---

# 📦 Step 2.1 Reconnaissance

Begin by gathering information about installed applications.

---

## List Installed Packages

```text
dz> run app.package.list
```

Example Output

```text
Package: com.android.settings
Package: com.android.browser
Package: com.example.vulnerable
Package: com.android.contacts
```

---

## View Package Information

```text
dz> run app.package.info -a com.android.browser
```

Example

```text
Package Name: com.android.browser

Version: 10.1

UID: 10056

Permissions:
android.permission.INTERNET
android.permission.ACCESS_NETWORK_STATE
```

---

## Search Packages Using Permissions

Applications requesting dangerous permissions are often worth investigating.

```text
dz> run app.package.list -p android.permission.INTERNET
```

Example

```text
com.android.browser

com.example.vulnerable

com.example.notes
```

---

# 📊 Reconnaissance Summary

Information gathered includes:

- Installed applications
- Requested permissions
- Package metadata
- Application versions
- UID assignments

---

# 🚀 Step 2.2 Scan Exported Activities

Activities can often be launched externally if marked as exported.

These components are common attack targets.

---

## List All Exported Activities

```text
dz> run app.activity.info
```

Example

```text
Package:

com.example.vulnerable

Activity:

LoginActivity

Exported: true
```

---

## Search Activities Within One Package

```text
dz> run app.activity.info -a com.example.vulnerable
```

Example

```text
MainActivity

Exported

SettingsActivity

Exported

AdminActivity

Exported
```

---

## Find Activities with Intent Filters

Intent Filters often expose components to external applications.

```text
dz> run app.activity.info -i
```

Example

```text
Activity:

ShareActivity

Intent Filter:

android.intent.action.SEND
```

---

# 🔍 What to Look For

Prioritize activities that:

- Accept external Intents
- Require no authentication
- Handle files
- Process URLs
- Receive user input
- Open privileged screens

---

# 🚀 Step 2.3 Scan Exported Services

Services execute background operations and frequently expose sensitive functionality.

---

## List Exported Services

```text
dz> run app.service.info
```

Example

```text
Package:

com.example.vulnerable

Service:

SyncService

Exported: true
```

---

## Search Package Services

```text
dz> run app.service.info -a com.example.vulnerable
```

Example

```text
BackgroundService

Exported

DataSyncService

Exported

BackupService

Exported
```

---

# 🔍 Interesting Services

Focus on services that perform:

- File operations
- Network communication
- Database updates
- Authentication
- Backup functionality
- Administrative tasks

---

# 📡 Step 2.4 Scan Broadcast Receivers

Broadcast Receivers respond to Android system broadcasts and custom application events.

Improperly exported receivers may allow unauthorized command execution.

---

## List Exported Receivers

```text
dz> run app.broadcast.info
```

Example

```text
Receiver:

BootReceiver

Exported: true
```

---

## Search Receivers by Package

```text
dz> run app.broadcast.info -a com.example.vulnerable
```

Example

```text
UpdateReceiver

Exported

NotificationReceiver

Exported

AdminReceiver

Exported
```

---

# 🔍 High-Risk Broadcast Receivers

Investigate receivers responding to:

- BOOT_COMPLETED
- PACKAGE_ADDED
- CONNECTIVITY_CHANGE
- Custom application actions
- Device administration events

---

# 📂 Step 2.5 Scan Content Providers

Content Providers frequently expose databases and application storage.

Poorly protected providers can leak sensitive information.

---

## List Providers

```text
dz> run app.provider.info
```

Example

```text
Provider:

com.example.provider

Authority:

content://com.example.provider
```

---

## Search Specific Package

```text
dz> run app.provider.info -a com.example.vulnerable
```

---

## Query Provider

```text
dz> run app.provider.query content://com.example.provider/data
```

Example

```text
ID

Username

Email

PasswordHash
```

---

# 🚨 High-Risk Provider Indicators

Look for providers exposing:

- User credentials
- Authentication tokens
- API keys
- Configuration files
- Personal information
- Internal databases

---

# 📊 Component Enumeration Summary

| Component | Discovery Command |
|-----------|-------------------|
| Activities | `run app.activity.info` |
| Services | `run app.service.info` |
| Broadcast Receivers | `run app.broadcast.info` |
| Content Providers | `run app.provider.info` |
| Installed Packages | `run app.package.list` |
| Package Details | `run app.package.info` |

---

# 📝 Documentation Checklist

Record the following information for each exposed component:

- Component name
- Component type
- Package name
- Export status
- Required permissions
- Intent filters
- Potential security impact

---

# ✅ Task 2 Complete

At this stage you have successfully:

- Enumerated installed Android applications
- Identified exported Activities
- Identified exposed Services
- Enumerated Broadcast Receivers
- Located accessible Content Providers
- Mapped the application's attack surface
- Collected targets for exploitation in the next task

- # ⚔️ Task 3 — Interact with Exposed Components

After identifying exported Android components, the next step is to interact with them to understand their behavior and determine whether they expose unintended functionality. In this task, you'll use Drozer to communicate with Activities, Services, Broadcast Receivers, and Content Providers in a controlled lab environment.

> **Note:** Perform these actions only against applications you own or are explicitly authorized to test.

---

# 🎯 Objective

In this task you will:

- Interact with exported Activities
- Communicate with exposed Services
- Send custom Broadcast Intents
- Access Content Providers
- Observe application behavior
- Document security findings

---

# 🚀 Step 3.1 Interact with Activities

Activities can often be launched externally if they are exported.

---

## Launch an Activity

```text
dz> run app.activity.start --component com.example.vulnerable com.example.MainActivity
```

Expected behavior:

```text
Launching activity...
Activity started successfully.
```

---

## Launch Activity with Intent Extras

```text
dz> run app.activity.start \
--component com.example.vulnerable \
com.example.MainActivity \
--extra string username admin \
--extra string password test123
```

Observe how the application processes externally supplied input.

---

## Launch Activity with File URI

```text
dz> run app.activity.start \
--component com.example.vulnerable \
com.example.FileActivity \
--data-uri file:///etc/passwd
```

Document whether the application validates or safely handles the supplied URI.

---

## Launch Using a Custom Intent Action

```text
dz> run app.activity.start \
--action android.intent.action.VIEW
```

This helps determine whether activities respond to common Android intent actions.

---

# 📋 Document

Record:

- Activity name
- Exported status
- Required permissions
- Accepted intent actions
- Observed behavior
- Security concerns

---

# ⚙️ Step 3.2 Interact with Services

Android Services perform background processing.

Exported services should enforce appropriate authorization before accepting requests.

---

## Start a Service

```text
dz> run app.service.start \
--component com.example.vulnerable \
com.example.BackgroundService
```

---

## Send Intent Extras

```text
dz> run app.service.start \
--component com.example.vulnerable \
com.example.DataService \
--extra string data "example_input"
```

Observe whether the service accepts and processes the supplied input.

---

## Stop the Service

```text
dz> run app.service.stop \
--component com.example.vulnerable \
com.example.BackgroundService
```

---

# 📋 Record

- Service name
- Exported status
- Accepted parameters
- Observed functionality
- Authentication requirements
- Potential impact

---

# 📡 Step 3.3 Send Broadcast Intents

Broadcast Receivers listen for Android system events and custom application broadcasts.

---

## Send Custom Broadcast

```text
dz> run app.broadcast.send \
--action com.example.CUSTOM_ACTION
```

---

## Send System Broadcast

```text
dz> run app.broadcast.send \
--action android.intent.action.BOOT_COMPLETED
```

Use only in the controlled lab environment to observe how the receiver responds.

---

## Send Broadcast with Data URI

```text
dz> run app.broadcast.send \
--action android.intent.action.VIEW
```

Observe whether the receiving component processes the broadcast appropriately.

---

# 📋 Document

- Receiver name
- Trigger action
- Exported status
- Response observed
- Access controls
- Security implications

---

# 🗂 Step 3.4 Access Content Providers

Content Providers expose structured application data.

---

## Query Provider

```text
dz> run app.provider.query \
content://com.example.provider/users
```

Example Output

```text
ID

Username

Email

Role
```

---

## Retrieve Additional Records

```text
dz> run app.provider.query \
content://com.example.provider/data
```

Document the structure and sensitivity of any accessible data.

---

# 🔍 What to Look For

Identify whether providers expose:

- User information
- API tokens
- Authentication data
- Configuration settings
- Internal application records
- Personally identifiable information (PII)

---

# 📊 Component Interaction Checklist

| Component | Tested | Notes |
|-----------|--------|-------|
| Activity | ✅ | Behavior documented |
| Service | ✅ | Input handling observed |
| Broadcast Receiver | ✅ | Response recorded |
| Content Provider | ✅ | Accessible data documented |

---

# 📝 Findings Template

Use the following format for each component:

```text
Component:

Package:

Type:

Exported:

Permissions Required:

Observed Behavior:

Potential Security Impact:

Recommended Mitigation:
```

---

# 🛡 Security Best Practices

When reviewing Android components, verify that applications:

- Export only components that require external access
- Validate all incoming intent data
- Restrict privileged functionality to authorized callers
- Protect sensitive content providers with permissions
- Minimize the attack surface by disabling unnecessary exports

---

# 🎯 Task 3 Summary

During this task you:

- Interacted with exported Activities
- Communicated with exposed Services
- Triggered Broadcast Receivers
- Queried Content Providers
- Observed component behavior
- Collected evidence for security documentation

These findings will be used in the next task to automate component enumeration and generate assessment reports using Python.

---

# ✅ Task 3 Complete

You have successfully:

- Tested exported Android components
- Documented observed behavior
- Assessed potential security risks
- Prepared for automated analysis and reporting in **Task 4**

- # 🤖 Task 4 — Automate Component Enumeration with Python

Manual testing is effective for understanding application behavior, but automation enables faster and more consistent security assessments. In this task, you'll create Python utilities to enumerate Android components, interact with them in a controlled manner, and generate structured assessment reports.

> **Note:** These scripts are intended for authorized testing and educational use.

---

# 🎯 Objective

In this task you will:

- Build a Python component scanner
- Automate Drozer command execution
- Generate scan reports
- Create configurable test payloads
- Record assessment results
- Produce professional security documentation

---

# 🐍 Step 4.1 Create Component Scanner

Create the scanner.

```bash
nano component_scanner.py
```

Paste the provided skeleton and implement the **TODO** sections.

---

## Features to Implement

### Execute Drozer Commands

```python
def run_drozer_command(self, command, timeout=30):
```

Implement:

- Execute Drozer using `subprocess`
- Handle execution errors
- Implement timeout protection
- Return command output

---

### Scan Activities

```python
def scan_activities(self):
```

Implement:

- Execute

```text
run app.activity.info
```

- Parse results
- Save exported activities
- Return discovered components

---

### Scan Services

```python
def scan_services(self):
```

Implement:

- Execute

```text
run app.service.info
```

- Parse output
- Save discovered services

---

### Scan Broadcast Receivers

```python
def scan_receivers(self):
```

Implement:

- Execute

```text
run app.broadcast.info
```

- Parse receiver information

---

### Scan Content Providers

```python
def scan_providers(self):
```

Implement:

- Execute

```text
run app.provider.info
```

- Store provider information

---

### Run Complete Enumeration

```python
def run_full_scan(self):
```

Implement:

- Activities
- Services
- Receivers
- Providers
- Summary
- Report generation

---

### Save Results

```python
def save_results(self):
```

Generate a readable report.

Example:

```text
Activities

MainActivity

Exported

SettingsActivity

Exported

Services

SyncService

Exported

Receivers

BootReceiver

Providers

UserProvider
```

---

## Execute Scanner

```bash
chmod +x component_scanner.py
```

Run against a target package.

```bash
python3 component_scanner.py com.example.vulnerable
```

---

# 🚀 Step 4.2 Create Automation Script

Create the exploitation helper.

```bash
nano exploit_automation.py
```

Complete every TODO section.

---

## Load Configuration

```python
def load_payloads(self):
```

Read payload definitions from JSON.

Store them for testing.

---

## Activity Interaction

```python
def exploit_activity(self):
```

Implement:

- Build Drozer command
- Execute command
- Record outcome
- Save result

---

## Service Interaction

```python
def exploit_service(self):
```

Implement:

- Execute service command
- Record observations
- Save results

---

## Broadcast Interaction

```python
def exploit_receiver(self):
```

Implement:

- Send broadcast
- Capture outcome
- Log findings

---

## Input Validation Tests

Implement a set of benign test inputs to evaluate whether components properly validate externally supplied data.

```python
def test_input_validation(self):
```

Example inputs:

```text
Special characters

Long strings

Unexpected data types

Malformed URIs
```

Observe whether components safely handle these inputs without unexpected behavior.

---

## File Path Handling Tests

Implement tests that verify whether applications correctly validate file path input.

```python
def test_file_validation(self):
```

Example values:

```text
file:///sdcard/example.txt

content://example.provider/file
```

Record how the application processes each request.

---

## Run Complete Assessment

```python
def run_exploitation(self):
```

Execute:

- Activity testing
- Service testing
- Receiver testing
- Validation tests
- Report generation

---

## Generate JSON Report

```python
def generate_report(self):
```

Example structure

```json
{
    "activities_tested":5,
    "services_tested":2,
    "receivers_tested":3,
    "providers_tested":1,
    "issues_found":4
}
```

---

# 📄 Step 4.3 Create Payload Configuration

Create the configuration file.

```bash
nano payloads.json
```

Example

```json
{
  "activity_payloads":[
      {
         "name":"Input Validation",
         "extras":{
            "input":"example"
         }
      },
      {
         "name":"URI Test",
         "data_uri":"content://example.provider/data"
      }
  ],
  "broadcast_payloads":[
      {
         "name":"Custom Broadcast",
         "action":"com.example.TEST_ACTION"
      }
  ]
}
```

Using a configuration file allows test cases to be updated without modifying Python code.

---

# ▶️ Step 4.4 Execute Automated Assessment

Make scripts executable.

```bash
chmod +x component_scanner.py
```

```bash
chmod +x exploit_automation.py
```

Run component enumeration.

```bash
python3 component_scanner.py com.example.vulnerable
```

Run automated interaction tests.

```bash
python3 exploit_automation.py com.example.vulnerable
```

Review generated reports.

```bash
cat scan_results.txt
```

```bash
cat exploit_report.json
```

---

# 📊 Expected Results

Your automation should generate reports similar to:

```text
Activities Found:

5

Services Found:

2

Broadcast Receivers:

3

Content Providers:

1

Assessment Completed Successfully
```

---

# 📁 Expected Project Structure

```text
drozer-component-lab/

├── component_scanner.py
├── exploit_automation.py
├── payloads.json
│
├── scan_results.txt
├── exploit_report.json
│
├── reports/
├── screenshots/
└── logs/
```

---

# 📝 Security Assessment Checklist

| Assessment | Status |
|------------|--------|
| Environment Configured | ✅ |
| Drozer Connected | ✅ |
| Applications Enumerated | ✅ |
| Activities Identified | ✅ |
| Services Identified | ✅ |
| Broadcast Receivers Identified | ✅ |
| Content Providers Enumerated | ✅ |
| Python Automation Completed | ✅ |
| Reports Generated | ✅ |
| Findings Documented | ✅ |

---

# 📈 Expected Outcomes

Upon completing this lab you should be able to:

- Configure Drozer for Android assessments
- Enumerate exported application components
- Interact with Activities, Services, Broadcast Receivers, and Content Providers
- Automate component discovery using Python
- Generate structured security reports
- Document findings and recommend mitigations

---

# 🛡 Security Best Practices

During mobile application development:

- Set `android:exported="false"` unless external access is required.
- Protect exported components with appropriate permissions.
- Validate all incoming Intent data before processing.
- Apply the principle of least privilege to inter-application communication.
- Review exported components during every security assessment.
- Include automated component enumeration in CI/CD security testing.

---

# 🔧 Troubleshooting

## ❌ Drozer Cannot Connect

Verify port forwarding.

```bash
adb forward --list
```

Restart the Drozer Agent and reconnect.

---

## ❌ Emulator Not Detected

Restart ADB.

```bash
adb kill-server
```

```bash
adb start-server
```

Verify device status.

```bash
adb devices
```

---

## ❌ Python Automation Fails

Confirm Drozer is installed.

```bash
which drozer
```

Verify the emulator is running and accessible before executing automation scripts.

---

## ❌ No Components Detected

Check that the target application is installed.

```bash
adb shell pm list packages
```

Verify the package name supplied to the script matches the installed application.

---

# 🎓 Key Takeaways

- Drozer provides comprehensive visibility into Android application components.
- Exported components should be intentionally exposed and protected with appropriate permissions.
- Python automation improves consistency and scalability of mobile security assessments.
- Well-structured reports support remediation efforts and security reviews.
- Regular audits help reduce the attack surface of Android applications.

---

# 🚀 Next Steps

Continue your Mobile Application Penetration Testing journey with:

- 🔍 Static APK Analysis
- ⚙️ Dynamic Analysis with Frida
- 📱 Android Runtime Instrumentation
- 🌐 Mobile API Security Testing
- 🔐 Android Keystore Assessment
- 📦 APK Reverse Engineering
- 🧠 Android Malware Analysis
- 📡 HTTPS Traffic Interception
- 🛡 Mobile Threat Modeling
- 📋 Comprehensive Mobile Security Reporting

---

# ⚠ Disclaimer

This lab is intended **solely for educational purposes, cybersecurity training, and authorized mobile application security assessments**.

Only test applications and devices that you own or have explicit permission to assess. Unauthorized testing may violate organizational policies, contractual obligations, or applicable laws.

---

# 🤝 Contributing

Contributions are welcome!

You can help improve this repository by:

- 📚 Adding new Android security labs
- 🐍 Enhancing Python automation scripts
- 🔧 Expanding Drozer workflows
- 📝 Improving documentation
- 🐛 Reporting issues
- 🚀 Optimizing assessment tools
- 📊 Adding additional reporting features

---

# ⭐ Support

If you found this repository useful:

- ⭐ Star the repository
- 🍴 Fork the repository
- 📢 Share it with the cybersecurity community
- 🤝 Contribute new mobile security content

---

<div align="center">

# 📱 Master Android Component Security with Drozer

### 🚀 Happy Learning & Happy Hacking (Ethically)!

</div>

# 🔓 Bypass Certificate Pinning Using Frida

<div align="center">

![Frida](https://img.shields.io/badge/Frida-Dynamic_Instrumentation-red?style=for-the-badge)
![Android](https://img.shields.io/badge/Android-Mobile_Security-3DDC84?style=for-the-badge\&logo=android\&logoColor=white)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Frida_Scripting-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![ADB](https://img.shields.io/badge/ADB-Android_Debug_Bridge-green?style=for-the-badge)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-Traffic_Analysis-orange?style=for-the-badge)
![SSL/TLS](https://img.shields.io/badge/SSL/TLS-Certificate_Pinning-blue?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)

</div>

---

# 📖 Overview

Certificate Pinning is a defense-in-depth security mechanism used by Android applications to prevent Man-in-the-Middle (MITM) attacks. While it significantly improves application security, security professionals often need to bypass certificate pinning during authorized penetration testing and mobile application assessments.

In this lab, you will learn how to use **Frida**, a dynamic instrumentation toolkit, to bypass common SSL/TLS certificate pinning implementations in Android applications. You'll also automate the bypass process with Python and analyze encrypted traffic using Burp Suite.

---

# 🎯 Objectives

By the end of this lab, you will be able to:

* 🔍 Understand SSL certificate pinning mechanisms.
* 📱 Configure Frida for Android dynamic instrumentation.
* ✍️ Write Frida JavaScript hooks to bypass certificate pinning.
* 🌐 Intercept HTTPS traffic using Burp Suite.
* 🤖 Automate certificate pinning bypass with Python.
* 📊 Analyze encrypted application traffic securely.

---

# 📚 Prerequisites

Before beginning this lab, ensure you have:

* ✅ Basic understanding of SSL/TLS protocols
* ✅ Familiarity with certificate validation
* ✅ Basic JavaScript programming knowledge
* ✅ Python programming experience
* ✅ Understanding of Android application architecture
* ✅ Linux command-line experience

---

# 🛠 Technology Stack

| Technology                    | Purpose                 |
| ----------------------------- | ----------------------- |
| 🐍 Python 3                   | Automation Scripts      |
| 📜 JavaScript                 | Frida Hook Scripts      |
| 📱 Frida                      | Dynamic Instrumentation |
| 🤖 Android Emulator           | Target Device           |
| 🔧 Android Debug Bridge (ADB) | Device Communication    |
| 🌐 Burp Suite Community       | HTTPS Proxy & Analysis  |
| 🐧 Ubuntu Linux               | Lab Platform            |

---

# 📂 Lab Environment

The cloud environment already contains all required tools.

## 💻 Pre-installed Software

* ✅ Frida
* ✅ Python 3
* ✅ frida-tools
* ✅ Android Emulator
* ✅ Android Debug Bridge (ADB)
* ✅ Burp Suite Community Edition
* ✅ Nano & Vim Editors

No additional installation is required.

---

# 📁 Lab Directory Structure

```text
/home/student/
│
├── apps/
│     └── pinning-test.apk
│
├── scripts/
│     ├── ssl_bypass.js
│     ├── advanced_bypass.js
│     ├── traffic_monitor.js
│     ├── auto_bypass.py
│     └── config_bypass.py
│
└── tools/
      └── frida-server
```

---

# 🚩 Task 1 — Environment Setup and Verification

Before bypassing SSL pinning, verify that the Android environment and Frida are correctly configured.

---

# 🔹 Step 1 — Verify Frida Installation

Check the installed Frida version.

```bash
frida --version
```

Example output:

```text
16.5.2
```

---

List all connected Android devices.

```bash
frida-ps -U
```

Expected output:

```text
PID     Name
-----------------------
System UI
Settings
Launcher
```

---

## 💡 Why Verify Frida?

This confirms:

* ✔ Frida is installed.
* ✔ USB communication is working.
* ✔ The Android device is accessible.
* ✔ Dynamic instrumentation is available.

---

# 🔹 Step 2 — Start the Android Environment

Launch the Android emulator.

```bash
emulator -avd test_device -no-snapshot &
```

Wait until Android is fully booted.

```bash
adb wait-for-device
```

Verify the emulator is connected.

```bash
adb devices
```

Example output:

```text
List of devices attached

emulator-5554    device
```

---

## 📌 Verification Checklist

Ensure:

* ✅ Emulator starts successfully.
* ✅ Device state is **device**.
* ✅ No offline devices are listed.

---

# 🔹 Step 3 — Deploy Frida Server

Frida requires a server component running inside Android.

Copy the server to the device.

```bash
adb push /home/student/tools/frida-server /data/local/tmp/
```

Expected output:

```text
frida-server: 1 file pushed.
```

---

Grant execution permissions.

```bash
adb shell chmod 755 /data/local/tmp/frida-server
```

---

Start the Frida server with root privileges.

```bash
adb shell "su -c '/data/local/tmp/frida-server &'"
```

---

Verify the server is running.

```bash
frida-ps -U
```

Example:

```text
PID     Name
--------------------------
Android System
System UI
Settings
Launcher
```

---

## 🔍 Deployment Workflow

```text
Host Machine
      │
      ▼
Copy frida-server
      │
      ▼
Grant Permissions
      │
      ▼
Start Server
      │
      ▼
Verify Connection
```

---

# 🔹 Step 4 — Install the Test Application

Install the vulnerable Android application.

```bash
adb install /home/student/apps/pinning-test.apk
```

Example output:

```text
Success
```

---

Verify installation.

```bash
adb shell pm list packages | grep pinning
```

Expected output:

```text
package:com.example.pinningtest
```

---

Launch the application.

```bash
adb shell am start -n com.example.pinningtest/.MainActivity
```

Example:

```text
Starting:
Intent { cmp=com.example.pinningtest/.MainActivity }
```

---

# 📊 Environment Verification Checklist

Your environment is ready when all of the following are successful:

| Component                           | Status   |
| ----------------------------------- | -------- |
| ✅ Frida Installed                   | Verified |
| ✅ Android Emulator Running          | Verified |
| ✅ ADB Connected                     | Verified |
| ✅ Frida Server Running              | Verified |
| ✅ Test APK Installed                | Verified |
| ✅ Application Launches Successfully | Verified |

---

# 🎯 Task 1 Summary

At this stage, you have successfully prepared the Android security testing environment.

You accomplished:

* ✅ Verified Frida installation
* ✅ Started the Android emulator
* ✅ Connected using ADB
* ✅ Deployed the Frida server
* ✅ Installed the vulnerable application
* ✅ Confirmed the target application is ready for dynamic instrumentation

---

# ➡️ Next Step

In **Part 2**, you will begin writing **Frida JavaScript hooks** to bypass common SSL certificate pinning implementations, including:

* 🔓 TrustManager bypass
* 🌐 HostnameVerifier bypass
* 📡 OkHttp CertificatePinner bypass
* 🚀 Advanced SSLContext hooks
* 🛡️ Android Conscrypt bypass

These techniques form the foundation for intercepting encrypted HTTPS traffic during authorized mobile application security assessments.
# 🚩 Task 2 — Create Certificate Pinning Bypass Scripts

After preparing the Android environment, the next step is to dynamically bypass SSL certificate pinning using **Frida**. In this task, you will create JavaScript hooks that intercept certificate validation routines and allow HTTPS traffic to be inspected during authorized security assessments.

> ⚠️ **Educational Use Only:** These techniques are intended solely for authorized penetration testing, security research, and training.

---

# 🔹 Step 1 — Create a Basic SSL Pinning Bypass Script

Navigate to the scripts directory.

```bash
cd /home/student/scripts
```

Create the JavaScript bypass script.

```bash
nano ssl_bypass.js
```

Paste the provided lab template into the file.

---

## 📜 Script Overview

The script targets three common certificate validation mechanisms used by Android applications:

* 🔐 `X509TrustManager`
* 🌐 `HostnameVerifier`
* 📡 `OkHttp CertificatePinner`

Students will complete the **TODO** sections to implement the bypass logic.

---

# 🧩 Hook 1 — TrustManager Bypass

The Android **TrustManager** validates server certificates before a secure connection is established.

```javascript
Java.use("javax.net.ssl.X509TrustManager");
```

Complete the following methods:

* ✔ `checkClientTrusted()`
* ✔ `checkServerTrusted()`
* ✔ `getAcceptedIssuers()`

---

### 🎯 Objective

Modify these methods so certificate validation is bypassed during testing.

Example console message:

```text
[+] Bypassing checkServerTrusted
```

---

### 🔄 TrustManager Workflow

```text
Application
      │
      ▼
TrustManager
      │
Certificate Validation
      │
      ▼
Frida Hook
      │
      ▼
Validation Bypassed
```

---

# 🧩 Hook 2 — HostnameVerifier Bypass

Applications often validate the server hostname after certificate validation.

Hook:

```javascript
Java.use("javax.net.ssl.HostnameVerifier");
```

Override:

```javascript
verify(hostname, session)
```

---

### 🎯 Objective

Modify the method to always allow the hostname.

Expected console output:

```text
[+] Bypassing hostname verification
```

---

### 🌐 Hostname Verification Flow

```text
HTTPS Request
      │
      ▼
Hostname Check
      │
      ▼
Frida Hook
      │
      ▼
Allowed
```

---

# 🧩 Hook 3 — OkHttp CertificatePinner

Many modern Android applications use the **OkHttp** networking library.

Hook:

```javascript
okhttp3.CertificatePinner
```

Override:

```javascript
check()
```

---

### 🎯 Objective

Prevent OkHttp from rejecting custom certificates during testing.

Expected message:

```text
[+] Bypassing OkHttp pinning
```

---

### 📡 OkHttp Workflow

```text
Application
      │
      ▼
OkHttp
      │
CertificatePinner
      │
      ▼
Frida Hook
      │
      ▼
Certificate Accepted
```

---

# 🔹 Step 2 — Execute the Basic Bypass Script

Launch the application with Frida.

```bash
frida -U \
-f com.example.pinningtest \
-l /home/student/scripts/ssl_bypass.js \
--no-pause
```

---

## 📊 Expected Output

```text
[+] SSL Pinning Bypass Started

[+] Bypassing checkServerTrusted

[+] Bypassing hostname verification

[+] Bypassing OkHttp pinning

[+] Bypass script loaded successfully
```

---

## ✅ Verification Checklist

Confirm:

* ✔ Frida attaches successfully.
* ✔ No application crashes occur.
* ✔ Console displays bypass messages.
* ✔ HTTPS requests continue normally.

---

# 🔹 Step 3 — Create an Advanced SSL Bypass Script

Create a second script.

```bash
nano advanced_bypass.js
```

Paste the provided lab template.

---

# 🧩 Advanced Hook 1 — Custom TrustManager

Instead of modifying the existing TrustManager, create a new implementation.

Use:

```javascript
Java.registerClass()
```

Implement:

* ✔ `checkClientTrusted()`
* ✔ `checkServerTrusted()`
* ✔ `getAcceptedIssuers()`

---

### 🎯 Goal

Inject a TrustManager that accepts every certificate.

---

### 🔄 Custom TrustManager Workflow

```text
SSLContext
      │
      ▼
Original TrustManager
      │
      ▼
Custom TrustManager
      │
      ▼
Accept All Certificates
```

---

# 🧩 Advanced Hook 2 — SSLContext.init()

Applications typically initialize SSL through:

```javascript
SSLContext.init()
```

Hook:

```javascript
SSLContext.init(...)
```

Replace the original TrustManager with the custom implementation.

---

### Expected Console Output

```text
[+] SSLContext.init hooked
```

---

# 🧩 Advanced Hook 3 — Android Conscrypt

Android 7+ commonly uses **Conscrypt**.

Hook:

```javascript
com.android.org.conscrypt.TrustManagerImpl
```

Override:

```javascript
checkTrustedRecursive()
```

---

### 🎯 Goal

Return an empty trusted certificate list so validation succeeds.

Example output:

```text
[+] Bypassing Conscrypt TrustManager
```

---

### 🔄 Conscrypt Workflow

```text
Android App
      │
      ▼
Conscrypt
      │
Certificate Validation
      │
      ▼
Frida Hook
      │
      ▼
Validation Skipped
```

---

# 📊 Expected Console Output

```text
[+] Advanced SSL Bypass Loaded

[+] SSLContext.init hooked

[+] Bypassing Conscrypt TrustManager

[+] Advanced bypass configured
```

---

# 🔍 Testing Checklist

Verify the following after loading the advanced script:

| Test                      | Expected Result |
| ------------------------- | --------------- |
| ✔ Application Starts      | Success         |
| ✔ Frida Hooks Loaded      | Success         |
| ✔ SSLContext Hooked       | Success         |
| ✔ TrustManager Replaced   | Success         |
| ✔ Conscrypt Bypassed      | Success         |
| ✔ HTTPS Requests Continue | Success         |

---

# 💡 Security Concepts Learned

During this task you explored several key Android networking components:

### 🔐 X509TrustManager

Responsible for validating certificate chains presented by remote servers.

---

### 🌐 HostnameVerifier

Ensures that the hostname matches the certificate's Common Name (CN) or Subject Alternative Name (SAN).

---

### 📡 CertificatePinner

Provides an additional layer of security by verifying a predefined certificate or public key.

---

### ⚙️ SSLContext

Initializes SSL/TLS connections and determines which TrustManager implementation is used.

---

### 🛡️ Conscrypt

Android's default cryptographic provider responsible for certificate validation on modern Android versions.

---

# 🎯 Task 2 Summary

In this task, you successfully prepared Frida scripts capable of bypassing multiple certificate pinning implementations.

### ✔ Skills Acquired

* 🔓 Hooking `X509TrustManager`
* 🌐 Bypassing `HostnameVerifier`
* 📡 Disabling `OkHttp CertificatePinner`
* ⚙️ Replacing TrustManagers with custom implementations
* 🛡️ Hooking Android Conscrypt
* 📜 Writing reusable Frida JavaScript hooks
* 🚀 Launching Android applications with injected scripts

---

# ➡️ Next Step

In **Part 3**, you will move beyond bypassing certificate validation and begin **intercepting live HTTPS traffic**. You will:

* 🌐 Configure **Burp Suite** as an interception proxy
* 📡 Monitor network requests with Frida
* 🔍 Capture URLs, HTTP methods, headers, and responses
* 📊 Analyze encrypted traffic after SSL pinning has been bypassed

These skills are essential for dynamic mobile application security testing and network traffic analysis.
# 🚩 Task 3 — Intercept and Analyze SSL/TLS Traffic

After successfully bypassing SSL certificate pinning, the next step is to observe and analyze the application's encrypted network communications. In this task, you will configure **Burp Suite** as an interception proxy and use **Frida** to monitor network activity in real time.

---

# 🔹 Step 1 — Configure Burp Suite Proxy

Launch Burp Suite.

```bash
burpsuite &
```

Wait for Burp Suite to finish loading.

---

## 🌐 Configure Android Proxy

Configure the Android emulator to forward all HTTP and HTTPS traffic through Burp Suite.

```bash
adb shell settings put global http_proxy 127.0.0.1:8080
```

Verify the proxy configuration.

```bash
adb shell settings get global http_proxy
```

Expected output:

```text
127.0.0.1:8080
```

---

## 🔐 Install Burp Suite CA Certificate

If HTTPS traffic is not visible, install Burp Suite's CA certificate on the emulator.

General workflow:

1. Export the Burp CA certificate.
2. Push or download it to the Android device.
3. Install it through Android Settings.
4. Trust the certificate.

---

### 🔄 Proxy Workflow

```text
Android Application
        │
        ▼
 HTTPS Request
        │
        ▼
 Burp Proxy (8080)
        │
        ▼
 Remote Server
```

---

# 🔹 Step 2 — Create a Traffic Monitoring Script

Navigate to the scripts directory.

```bash
cd /home/student/scripts
```

Create the monitoring script.

```bash
nano traffic_monitor.js
```

Paste the provided lab template.

---

# 🧩 Script Overview

The monitoring script observes network behavior without modifying application functionality.

The script should:

* 🌐 Log accessed URLs
* 📥 Monitor HTTP responses
* 📡 Capture OkHttp requests
* 📄 Display HTTP methods
* 📋 Print request headers

---

# 📌 Hook 1 — URL Monitoring

Hook the Java URL constructor.

```javascript
Java.use("java.net.URL");
```

Override:

```javascript
URL.$init(String url)
```

---

### 🎯 Objective

Display every URL accessed by the application.

Example console output:

```text
[+] URL Access:
https://api.example.com/login
```

---

### 🔄 URL Monitoring Workflow

```text
Application
      │
      ▼
URL Created
      │
      ▼
Frida Hook
      │
      ▼
Console Output
```

---

# 📌 Hook 2 — Monitor HTTP Responses

Hook:

```javascript
java.net.HttpURLConnection
```

Override:

```javascript
getResponseCode()
```

---

### 🎯 Objective

Capture:

* HTTP Status Code
* Destination URL
* Response Metadata

Example output:

```text
[+] Response Code: 200
```

---

### 🔄 Response Workflow

```text
HTTP Request
      │
      ▼
Server Response
      │
      ▼
Frida Hook
      │
      ▼
Log Status Code
```

---

# 📌 Hook 3 — Monitor OkHttp Requests

Many Android applications use OkHttp.

Hook:

```javascript
okhttp3.OkHttpClient
```

Intercept:

```javascript
newCall()
```

---

### 🎯 Display

For every request:

* 🌐 URL
* 📄 Method
* 📋 Headers

Example:

```text
[+] OkHttp Request

URL:
https://api.example.com

Method:
POST
```

---

### 🔄 OkHttp Monitoring

```text
Application
      │
      ▼
OkHttp Request
      │
      ▼
Frida Hook
      │
      ▼
Display Metadata
```

---

# 🔹 Step 3 — Run Both Scripts Together

Launch the application while loading both Frida scripts.

```bash
frida -U \
-f com.example.pinningtest \
-l /home/student/scripts/ssl_bypass.js \
-l /home/student/scripts/traffic_monitor.js \
--no-pause
```

---

## 📊 Expected Console Output

```text
[+] SSL Pinning Bypass Started

[+] Traffic Monitor Started

[+] URL Access:
https://api.example.com/login

[+] OkHttp Request

Method:
POST

Response Code:
200
```

---

## 📌 Verify Burp Suite

Burp Suite should now display:

* ✔ HTTPS Requests
* ✔ HTTPS Responses
* ✔ Headers
* ✔ Cookies
* ✔ JSON Bodies
* ✔ Authentication Tokens

---

# 📊 Traffic Verification Checklist

| Item                  | Expected Result |
| --------------------- | --------------- |
| SSL Pinning Bypassed  | ✅               |
| Burp Proxy Working    | ✅               |
| HTTPS Traffic Visible | ✅               |
| URLs Logged           | ✅               |
| Headers Captured      | ✅               |
| Responses Logged      | ✅               |

---

# 🚩 Task 4 — Automate the Bypass with Python

Manual Frida execution becomes repetitive during penetration tests.

Automation provides:

* ⚡ Faster assessments
* 📦 Reusable tooling
* 🤖 Consistent execution
* 📊 Easier reporting

---

# 🔹 Step 1 — Create the Automation Script

Navigate to the scripts directory.

```bash
cd /home/student/scripts
```

Create the Python script.

```bash
nano auto_bypass.py
```

Paste the provided lab template.

---

# 🧩 Script Overview

The **SSLBypassAutomation** class automates the complete workflow.

Responsibilities include:

* Connecting to Android devices
* Launching applications
* Injecting Frida scripts
* Monitoring execution
* Cleaning up resources

Students should complete every **TODO** section in the provided template.

---

# 📌 Function — `connect_device()`

Implement:

```python
connect_device()
```

Responsibilities:

* 📱 Connect using `frida.get_usb_device()`
* ✔ Verify device availability
* ⚠ Handle connection errors

Expected console output:

```text
[+] Connected to Android device
```

---

### 🔄 Connection Workflow

```text
Python
     │
     ▼
Frida
     │
     ▼
USB Device
     │
     ▼
Connected
```

---

# 📌 Function — `load_bypass_script()`

Implement:

```python
load_bypass_script()
```

This method should generate or return the JavaScript code responsible for bypassing certificate validation.

The generated script should include:

* 🔐 TrustManager hooks
* 🌐 HostnameVerifier hooks
* 📡 OkHttp CertificatePinner hooks

---

# 📌 Function — `spawn_and_attach()`

Implement:

```python
spawn_and_attach()
```

Responsibilities:

* 🚀 Spawn the target application
* 📎 Attach Frida to the process
* 📜 Load the JavaScript bypass script
* ▶ Resume execution
* 📡 Register the message callback

---

### 🔄 Spawn Workflow

```text
Python Script
      │
      ▼
Spawn App
      │
      ▼
Attach Frida
      │
      ▼
Inject Script
      │
      ▼
Resume Process
```

---

# 📌 Function — `on_message()`

Implement:

```python
on_message()
```

The callback should:

* 📩 Process normal messages (`send`)
* ❌ Handle runtime errors (`error`)
* 🖥 Display formatted console output

Example:

```text
[+] Hook Loaded

[+] HTTPS Request Captured

[-] Error Loading Hook
```

---

# 📌 Function — `monitor()`

Implement:

```python
monitor()
```

Responsibilities:

* ⏱ Keep Frida active
* 📊 Display monitoring progress
* ⌛ Run for the specified duration

---

# 📌 Function — `cleanup()`

Implement:

```python
cleanup()
```

Responsible for:

* 🧹 Unloading scripts
* 🔌 Detaching Frida
* ✔ Releasing resources

---

# 🎯 Task 3 Summary

At this point you have successfully:

* 🌐 Configured Burp Suite as an interception proxy
* 🔓 Bypassed SSL certificate pinning
* 📡 Logged application network activity
* 📄 Monitored URLs and HTTP responses
* 🤖 Begun automating Frida with Python
* 🚀 Built reusable dynamic instrumentation workflows

These capabilities provide the foundation for scalable dynamic mobile application security testing.

---

# ➡️ Next Step

In **Part 4**, you will complete the lab by:

* ⚙️ Building a **configuration-driven SSL bypass framework**
* 📁 Creating reusable JSON configuration files
* 🤖 Supporting multiple target applications
* 📊 Reviewing expected outcomes
* 🛠 Troubleshooting common Frida issues
* 🎯 Summarizing the skills gained and recommended next steps for advanced mobile security testing.
# 🚩 Task 4 — Configuration-Based SSL Pinning Bypass Automation

Large-scale mobile application assessments often require testing multiple applications with different certificate pinning implementations. Rather than modifying Frida scripts manually for every target, you can build a **configuration-driven framework** that automatically generates the required hooks based on a JSON configuration file.

---

# 🔹 Step 2 — Create a Configuration-Based Automation Script

Navigate to the scripts directory.

```bash
cd /home/student/scripts
```

Create the configuration-based automation script.

```bash
nano config_bypass.py
```

Paste the provided lab template into the file.

---

# 🧩 Script Overview

The **ConfigurableBypass** class enables reusable and scalable SSL pinning bypass automation.

It should support:

* 📱 Multiple Android applications
* ⚙ Feature-based hook generation
* 📄 JSON configuration files
* 🤖 Automatic Frida deployment
* 📊 Centralized monitoring

Students should complete all **TODO** sections in the provided template.

---

# 📌 Function — `load_config()`

Implement:

```python
load_config()
```

Responsibilities:

* 📂 Read a JSON configuration file.
* ✔ Validate required fields.
* 📋 Load target application settings.
* ⚠ Handle invalid configurations gracefully.

Example configuration:

```json
{
  "targets": [
    {
      "package": "com.example.pinningtest",
      "bypass_trustmanager": true,
      "bypass_hostname_verifier": true,
      "bypass_okhttp": true,
      "custom_hooks": []
    }
  ],
  "monitor_duration": 120
}
```

---

### 🔄 Configuration Workflow

```text
JSON Configuration
        │
        ▼
Load File
        │
        ▼
Validate Data
        │
        ▼
Generate Hooks
```

---

# 📌 Function — `generate_script()`

Implement:

```python
generate_script()
```

The generated JavaScript should include only the enabled features.

Possible modules include:

* 🔐 TrustManager Bypass
* 🌐 HostnameVerifier Bypass
* 📡 OkHttp CertificatePinner
* 🛡 SSLContext Hook
* ⚙ Custom Java Hooks

---

### Script Generation Workflow

```text
Configuration
      │
      ▼
Selected Features
      │
      ▼
JavaScript Builder
      │
      ▼
Frida Script
```

---

# 📌 Function — `process_target()`

Implement:

```python
process_target()
```

Responsibilities:

* 📱 Spawn the target application.
* 🔗 Attach Frida.
* 📜 Load the generated script.
* ▶ Resume application execution.
* 💾 Store active session information.

---

# 📌 Function — `run_all_targets()`

Implement:

```python
run_all_targets()
```

Responsibilities:

* 📂 Iterate through every configured application.
* 🚀 Deploy the appropriate Frida script.
* 📊 Monitor all active sessions.
* ⚠ Handle failures without stopping the remaining scans.

---

# 📌 Function — `create_sample_config()`

Implement:

```python
create_sample_config()
```

Responsibilities:

* 📝 Generate a sample JSON configuration.
* 💾 Save the file.
* ✔ Display the configuration location.

---

# 🔹 Step 3 — Test the Automation Scripts

Make both Python scripts executable.

```bash
chmod +x /home/student/scripts/auto_bypass.py
chmod +x /home/student/scripts/config_bypass.py
```

---

Generate a sample configuration.

```bash
python3 /home/student/scripts/config_bypass.py --create-config
```

Edit the configuration file if required.

```bash
nano /home/student/scripts/bypass_config.json
```

Run the basic automation script.

```bash
python3 /home/student/scripts/auto_bypass.py \
com.example.pinningtest \
--monitor-time 30
```

Run the configuration-based automation.

```bash
python3 /home/student/scripts/config_bypass.py \
--config /home/student/scripts/bypass_config.json
```

---

## 📊 Expected Console Output

```text
[+] Connected to Android device

[+] Spawning application...

[+] Injecting SSL bypass hooks...

[+] Monitoring traffic...

[+] Session completed successfully.
```

---

# 🎯 Expected Outcomes

After completing this lab, you should be able to:

## 🔓 SSL Pinning Assessment

* ✅ Bypass SSL certificate pinning
* ✅ Understand common pinning implementations
* ✅ Intercept encrypted HTTPS traffic
* ✅ Analyze secure communications

---

## 📱 Dynamic Instrumentation

* ✅ Deploy Frida to Android devices
* ✅ Hook Java SSL classes
* ✅ Inject custom JavaScript hooks
* ✅ Monitor runtime behavior

---

## 🤖 Security Automation

* ✅ Automate Frida deployments
* ✅ Generate reusable bypass scripts
* ✅ Build configuration-driven tooling
* ✅ Support multiple Android applications

---

## 🌐 Network Analysis

* ✅ Configure Burp Suite
* ✅ Capture HTTPS requests
* ✅ Inspect request headers
* ✅ Analyze server responses

---

# ✔ Verification Checklist

| Test                          | Expected Result |
| ----------------------------- | --------------- |
| Frida Server Running          | ✅               |
| SSL Bypass Loaded             | ✅               |
| HTTPS Traffic Visible         | ✅               |
| Burp Proxy Working            | ✅               |
| Application Functional        | ✅               |
| Python Automation Successful  | ✅               |
| Configuration-Based Execution | ✅               |

---

# 🛠 Troubleshooting

## ❌ Frida Server Not Running

Verify the server process.

```bash
adb shell ps | grep frida-server
```

Restart the server if necessary.

```bash
adb shell "su -c 'killall frida-server'"
adb shell "su -c '/data/local/tmp/frida-server &'"
```

---

## ❌ Application Crashes During Hooking

Possible causes:

* Incorrect method signature
* Invalid Java class
* Unsupported Android version

Identify hook targets using:

```bash
frida-trace -U \
-f com.example.pinningtest \
-j '*!*check*/i'
```

---

## ❌ No HTTPS Traffic Appears in Burp Suite

Verify:

* ✔ Proxy settings
* ✔ Burp CA certificate installation
* ✔ Emulator network connectivity
* ✔ Application restarted after proxy configuration

Check the configured proxy.

```bash
adb shell settings get global http_proxy
```

---

## ❌ Script Injection Fails

Verify:

* Correct package name

```bash
adb shell pm list packages
```

* Frida device connection

```bash
frida-ps -U
```

* Target application is installed.

---

# 💡 Best Practices

When performing authorized mobile application security testing:

* 🔒 Use Frida only with explicit authorization.
* 🌐 Validate proxy and certificate configurations before testing.
* 📜 Keep reusable hook scripts organized.
* 🤖 Automate repetitive workflows where possible.
* 📊 Document findings thoroughly.
* 🔄 Test multiple SSL implementations.
* 🛡 Keep Frida and Android tools updated.

---

# 📚 Skills Gained

Throughout this lab, you developed practical experience with:

## 📱 Android Security Testing

* ✔ Certificate pinning concepts
* ✔ SSL/TLS validation
* ✔ Runtime application instrumentation
* ✔ HTTPS traffic analysis

---

## 🔧 Frida Development

* ✔ JavaScript hook creation
* ✔ Java class interception
* ✔ SSL bypass implementation
* ✔ Runtime monitoring

---

## 🐍 Python Automation

* ✔ Device management
* ✔ Frida scripting
* ✔ Configuration-driven automation
* ✔ Session lifecycle management

---

## 🌐 Network Security

* ✔ HTTPS interception
* ✔ Proxy configuration
* ✔ Traffic inspection
* ✔ Secure communication analysis

---

# 🚀 Next Steps

Continue expanding your mobile application security expertise by exploring:

* 🛡 Anti-Frida detection and evasion techniques
* ⚙ Native (JNI) certificate pinning implementations
* 📦 Runtime application instrumentation with Objection
* 🔬 Android reverse engineering using JADX and APKTool
* 🔐 OWASP Mobile Security Testing Guide (MSTG)
* ☁ DevSecOps integration for mobile application testing
* 🤖 Automated dynamic security testing pipelines

---

# 📖 Conclusion

This lab provided practical experience with **Frida** for dynamically bypassing SSL certificate pinning in Android applications. You configured a complete mobile testing environment, created JavaScript hooks to intercept certificate validation routines, monitored encrypted network traffic using Burp Suite, and automated the entire workflow with Python.

By implementing both basic and advanced bypass techniques, you gained insight into common SSL/TLS validation mechanisms used by Android applications and learned how dynamic instrumentation can be applied during authorized mobile security assessments. The addition of configuration-driven automation further demonstrated how these techniques can scale across multiple applications in professional penetration testing and security research environments.

These skills are fundamental for mobile application security testing, secure software validation, vulnerability research, and modern DevSecOps practices.

---

<div align="center">

# 🎉 Congratulations!

You have successfully completed the

# 🔓 **Bypass Certificate Pinning Using Frida**

### Android Dynamic Instrumentation & SSL/TLS Analysis Lab

---

## 🏆 What You Accomplished

✅ Configured Frida for Android Dynamic Instrumentation

✅ Deployed and Managed Frida Server

✅ Bypassed SSL Certificate Pinning

✅ Hooked TrustManager, HostnameVerifier, and OkHttp

✅ Intercepted HTTPS Traffic with Burp Suite

✅ Created Reusable Frida JavaScript Hooks

✅ Automated SSL Bypass with Python

✅ Built a Configuration-Driven Instrumentation Framework

---

### 🚀 Keep Learning • Keep Testing • Build More Secure Mobile Applications

**Happy Hacking & Secure Coding! 🔐**

</div>





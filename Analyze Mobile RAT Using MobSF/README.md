# 📱 Analyze Mobile RAT Using MobSF

<div align="center">

# 🛡️ Mobile Malware Analysis 

## Analyze Android Remote Access Trojans (RATs) Using MobSF

**Learn Mobile Malware Static Analysis, Threat Detection, and Security Automation**

![Platform](https://img.shields.io/badge/Platform-Android-success?style=for-the-badge)
![Framework](https://img.shields.io/badge/Tool-MobSF-blue?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge)
![Security](https://img.shields.io/badge/Focus-Mobile%20Malware-red?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)

</div>

---

# 📖 Overview

This lab provides hands-on experience in **Android Remote Access Trojan (RAT) analysis** using the **Mobile Security Framework (MobSF)**. Students will learn how to perform static malware analysis, identify malicious application behavior, inspect dangerous permissions, detect persistence mechanisms, analyze command-and-control (C2) communication, and automate malware assessment using the MobSF REST API with Python.

The lab focuses on defensive malware analysis techniques used by SOC analysts, DFIR teams, mobile security researchers, and threat intelligence professionals.

---

# 🎯 Objectives

By the end of this lab, you will be able to:

* ✅ Install and configure Mobile Security Framework (MobSF)
* ✅ Perform static analysis of Android RAT APKs
* ✅ Identify dangerous permissions and malicious components
* ✅ Detect suspicious communication patterns
* ✅ Use MobSF REST API for automated analysis
* ✅ Build Python automation for RAT detection
* ✅ Generate comprehensive malware assessment reports

---

# 📚 Prerequisites

Before beginning this lab, ensure you have:

* Basic Android application knowledge
* Understanding of APK structure
* Linux command-line experience
* Basic Python programming
* REST API fundamentals
* JSON data format familiarity

---

# 🖥️ Lab Environment

The lab environment includes:

| Component        | Details                  |
| ---------------- | ------------------------ |
| Operating System | Linux                    |
| Analysis Tool    | MobSF                    |
| Python           | 3.8+                     |
| RAT Samples      | `/home/student/samples/` |
| MobSF URL        | `http://localhost:8000`  |

---

# 📂 Repository Structure

```text
Analyze-Mobile-RAT-Using-MobSF/
│
├── README.md
├── rat-analysis/
│   ├── rat_detector.py
│   ├── network_analyzer.py
│   ├── batch_analysis.py
│   └── reports/
│
├── samples/
│   └── android-rat-sample.apk
│
└── screenshots/
```

---

# 🚀 Task 1 — Configure MobSF and Upload RAT Sample

---

## ✅ Step 1.1 Verify MobSF Installation

Navigate to the MobSF installation directory.

```bash
cd /opt/Mobile-Security-Framework-MobSF
```

Verify installation files.

```bash
ls -la
```

Check Python dependencies.

```bash
pip3 list | grep -E "django|requests|lxml"
```

---

## ✅ Step 1.2 Start MobSF Server

Launch the MobSF web application.

```bash
cd /opt/Mobile-Security-Framework-MobSF

python3 manage.py runserver 0.0.0.0:8000
```

> **Note:** Keep this terminal open during analysis.

---

## ✅ Step 1.3 Open MobSF Dashboard

Open Firefox and browse to:

```text
http://localhost:8000
```

You should see the MobSF upload dashboard.

---

## ✅ Step 1.4 Upload RAT APK

List available malware samples.

```bash
ls -lh /home/student/samples/
```

Inside MobSF:

1. Click **Upload & Analyze**
2. Select

```text
/home/student/samples/android-rat-sample.apk
```

3. Click **Analyze**
4. Wait 2–3 minutes

---

## ✅ Step 1.5 Review Analysis Dashboard

Inspect the following sections:

* 📦 App Information
* 🔐 Security Score
* 🔑 Permissions
* ⚙️ Components
* 📡 Network Security
* 🧠 Code Analysis

---

# 🔍 Task 2 — Analyze RAT Characteristics

---

## 🔐 Step 2.1 Dangerous Permissions

Identify permissions commonly abused by RAT malware.

| Permission           | Purpose              |
| -------------------- | -------------------- |
| CAMERA               | Remote surveillance  |
| RECORD_AUDIO         | Audio recording      |
| ACCESS_FINE_LOCATION | GPS tracking         |
| READ_SMS             | SMS theft            |
| SEND_SMS             | SMS abuse            |
| CALL_PHONE           | Remote calls         |
| READ_CONTACTS        | Contact exfiltration |
| SYSTEM_ALERT_WINDOW  | Overlay attacks      |
| DEVICE_ADMIN         | Device persistence   |

📌 Document every dangerous permission found.

---

## ⚙️ Step 2.2 Analyze Components

Create a workspace.

```bash
mkdir -p ~/rat-analysis

cd ~/rat-analysis
```

Create notes.

```bash
nano component_analysis.txt
```

Look for suspicious:

* Remote services
* Device admin activities
* Accessibility abuse
* Boot receivers
* SMS receivers
* Phone state listeners

---

## 🌐 Step 2.3 Network Analysis

Inspect the **Network Security** section.

Check for:

* HTTP communication
* Hardcoded IP addresses
* Embedded URLs
* URL shorteners
* Non-standard ports
* Cleartext traffic

Document every suspicious endpoint.

---

## 🧠 Step 2.4 Code Analysis

Review findings including:

* Reflection
* Dynamic loading
* Obfuscation
* Native code
* Cryptography
* Runtime execution

Create a list of the **Top 5 security issues**.

---

# 🤖 Task 3 — Automate RAT Detection

---

## 🔑 Step 3.1 Generate MobSF API Key

Retrieve the existing key.

```bash
cd /opt/Mobile-Security-Framework-MobSF

grep "MOBSF_API_KEY" MobSF/settings.py
```

Or generate one.

```bash
python3 manage.py generate_api_key
```

Save the generated API key.

---

## 🐍 Step 3.2 Create RAT Detection Script

Create the detector.

```bash
nano ~/rat-analysis/rat_detector.py
```

The detector should include modules for:

* APK upload
* REST API communication
* Report retrieval
* Permission analysis
* Component analysis
* RAT scoring
* Report generation

Key features:

* Automated APK upload
* JSON parsing
* Risk scoring
* Security recommendations
* Report export

Make executable.

```bash
chmod +x ~/rat-analysis/rat_detector.py
```

---

## 🌐 Step 3.3 Create Network Analysis Module

Create:

```bash
nano ~/rat-analysis/network_analyzer.py
```

Implement detection for:

* URLs
* IP addresses
* Domains
* URL shorteners
* Dynamic DNS
* Paste services
* Command-and-Control indicators
* Encryption detection

---

## ▶️ Step 3.4 Test the Detector

Run analysis.

```bash
cd ~/rat-analysis

python3 rat_detector.py \
/home/student/samples/android-rat-sample.apk \
YOUR_API_KEY
```

Expected output:

* RAT Score
* Risk Level
* Dangerous Permissions
* Suspicious Components
* C2 Indicators
* Recommendations

---

## 📦 Step 3.5 Batch Analysis

Create:

```bash
nano batch_analysis.py
```

The script should:

* Discover APK files
* Upload each APK
* Collect reports
* Calculate statistics
* Generate a summary

---

# 📊 Expected Outcomes

Upon successful completion, students will have:

✅ Functional MobSF environment

✅ Android malware analysis skills

✅ Automated RAT detection scripts

✅ Security assessment reports

✅ Mobile malware indicators

---

# 🚩 RAT Indicators

Common RAT indicators include:

### 🔐 Dangerous Permissions

* CAMERA
* RECORD_AUDIO
* READ_SMS
* SEND_SMS
* ACCESS_FINE_LOCATION
* READ_CONTACTS

---

### 🔄 Persistence

* BOOT_COMPLETED receiver
* DEVICE_ADMIN
* Accessibility services

---

### 🌐 Network Activity

* Hardcoded IPs
* HTTP communication
* Dynamic DNS
* URL shorteners
* Unknown domains

---

### ⚙️ Suspicious Components

* Remote control services
* Hidden activities
* Background services
* Accessibility abuse

---

# 🛠️ Troubleshooting

---

## ❌ MobSF Won't Start

Check port usage.

```bash
sudo netstat -tulpn | grep 8000
```

Terminate the existing process.

```bash
sudo kill -9 <PID>
```

Install dependencies.

```bash
pip3 install -r requirements.txt
```

Verify Java.

```bash
java -version
```

---

## ❌ API Authentication Failed

Verify:

* API key
* Authorization header
* Key expiration
* MobSF configuration

---

## ❌ Slow Analysis

Check disk space.

```bash
df -h
```

Monitor logs.

```bash
tail -f logs/mobsf.log
```

Restart MobSF if required.

---

## ❌ Python Import Errors

Install dependencies.

```bash
pip3 install requests
```

Verify Python path.

```bash
echo $PYTHONPATH
```

Run using Python 3.

```bash
python3 rat_detector.py
```

---

# 🏆 Skills Gained

After completing this lab, you will understand:

* Android malware analysis
* MobSF static analysis
* RAT behavior identification
* Android permissions analysis
* Component inspection
* Network indicator discovery
* Python automation
* REST API integration
* Malware reporting
* Mobile threat hunting

---

# 📖 Key Takeaways

* Static analysis reveals malware behavior without execution.
* Permission combinations often indicate malicious intent.
* Boot receivers and device administrators enable persistence.
* Network indicators expose command-and-control infrastructure.
* Automation significantly improves malware triage efficiency.
* MobSF provides an effective framework for Android application security analysis.

---

# 🚀 Next Steps

Continue learning by exploring:

* Android dynamic malware analysis
* Android emulators
* Frida instrumentation
* Obfuscation analysis
* Threat intelligence integration
* CI/CD malware scanning
* Real-world Android malware research

---

# ⚠️ Security Note

> **Always analyze malware in isolated and controlled environments. Never install untrusted APKs on production or personal devices. Use virtual machines or dedicated malware analysis environments to prevent accidental compromise.**

---

<div align="center">

## 🎓 Lab Completed Successfully

**You have learned how to analyze Android RAT malware using MobSF, identify malicious behavior through static analysis, automate detection using the MobSF REST API, and generate professional mobile malware assessment reports.**

⭐ Happy Learning & Stay Secure!

</div>

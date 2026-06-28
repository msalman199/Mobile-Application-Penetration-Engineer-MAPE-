# 🔐 Evaluate Crypto Libraries (AES in ECB Mode)

<div align="center">

# 🔒 Android Mobile Security 

### **Evaluate Crypto Libraries (AES in ECB Mode)**

[![Android](https://img.shields.io/badge/Android-Security-3DDC84?style=for-the-badge\&logo=android)](https://developer.android.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python)](https://python.org/)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-FCC624?style=for-the-badge\&logo=linux)]
[![APKTool](https://img.shields.io/badge/APKTool-Reverse%20Engineering-blue?style=for-the-badge)]
[![PyCryptodome](https://img.shields.io/badge/PyCryptodome-Cryptography-red?style=for-the-badge)]
[![AES](https://img.shields.io/badge/AES-Cryptography-orange?style=for-the-badge)]
[![Mobile Security](https://img.shields.io/badge/Mobile-Security-success?style=for-the-badge)]
[![Static Analysis](https://img.shields.io/badge/Static-Analysis-purple?style=for-the-badge)]

---

### 🎯 **Lab:** Evaluate Crypto Libraries (AES in ECB Mode)

*Learn to identify insecure cryptographic implementations, demonstrate AES-ECB weaknesses, automate APK crypto analysis, and recommend secure encryption practices.*

</div>

---

# 📖 Overview

Weak cryptographic implementations remain one of the most common security issues in Android applications. This lab focuses on identifying insecure encryption methods such as **AES in ECB mode**, detecting hardcoded cryptographic secrets, and building automated analysis tools that help security professionals assess Android applications efficiently.

By completing this lab, students will understand why ECB mode should never be used for sensitive information and how to replace insecure implementations with modern cryptographic standards.

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

* ✅ Identify insecure cryptographic implementations in Android applications
* ✅ Understand vulnerabilities of AES in ECB (Electronic Codebook) mode
* ✅ Analyze encryption patterns that reveal security weaknesses
* ✅ Automate cryptographic vulnerability detection
* ✅ Recommend secure alternatives to weak encryption methods

---

# 📚 Prerequisites

Before starting this lab, you should have:

* 🐍 Basic Python programming knowledge
* 🔐 Understanding of AES encryption
* 💻 Linux command-line experience
* 📱 Familiarity with Android APK structure
* 🧠 Basic knowledge of static code analysis

---

# 🛠 Lab Environment

The lab environment includes:

* 🐧 Linux Virtual Machine
* 🐍 Python 3
* 📦 APKTool
* 🔍 Android reverse engineering tools
* 🔐 PyCryptodome
* 📁 Sample vulnerable APK

---

# 📂 Lab Directory Structure

```text
crypto-lab/
│── apk-files/
│── extracted-apk/
│── scripts/
│── results/
```

---

# 🚩 Task 1 — Identify Insecure Cryptographic Implementations

## 🔹 Step 1 — Create Working Directory

```bash
mkdir -p ~/crypto-lab/{apk-files,extracted-apk,scripts,results}
cd ~/crypto-lab
```

✔ Creates the project workspace.

---

## 🔹 Step 2 — Create Cryptographic Pattern Scanner

📄 Create:

```text
scripts/crypto_scanner.py
```

The scanner should detect:

* 🔍 AES/ECB usage
* 🔑 Hardcoded encryption keys
* ⚠ Weak algorithms
* 🔐 Cipher instances
* 📄 File names
* 📍 Line numbers

Implement the TODO sections to:

* ✔ Walk through extracted APK directories
* ✔ Read Java, Smali and XML files
* ✔ Search using Regular Expressions
* ✔ Record findings
* ✔ Generate a vulnerability report

---

## 🔹 Step 3 — Extract APK

```bash
cd ~/crypto-lab/apk-files

apktool d sample-vulnerable-app.apk \
-o ../extracted-apk/vulnerable-app
```

---

## 🔹 Step 4 — Run Scanner

```bash
cd ~/crypto-lab/scripts

chmod +x crypto_scanner.py

python3 crypto_scanner.py \
../extracted-apk/vulnerable-app \
> ../results/scan_results.txt
```

---

## 🔹 Step 5 — Review Results

```bash
cat ~/crypto-lab/results/scan_results.txt
```

Expected findings include:

* 🚨 AES/ECB/PKCS5Padding
* 🔑 Hardcoded Keys
* ⚠ Weak Algorithms
* ❌ Missing IVs

---

# 🚩 Task 2 — Demonstrate ECB Mode Vulnerabilities

## 🔹 Step 1 — Install Crypto Library

```bash
pip3 install pycryptodome
```

---

## 🔹 Step 2 — Create ECB Demonstration Script

📄 Create

```text
scripts/ecb_demo.py
```

The script should implement:

* 🔐 AES ECB Encryption
* 🔓 AES ECB Decryption
* 📊 Pattern demonstration
* 🔄 ECB vs CBC comparison
* 📝 Security recommendations

Implement every TODO inside the provided template.

---

## 🔹 Step 3 — Execute Demonstration

```bash
cd ~/crypto-lab/scripts

chmod +x ecb_demo.py

python3 ecb_demo.py \
> ../results/ecb_demo_results.txt

cat ../results/ecb_demo_results.txt
```

---

## 🔹 Step 4 — Observe ECB Weakness

Document the following observations:

✅ Identical plaintext blocks produce identical ciphertext blocks

✅ Data patterns remain visible

✅ Repeated blocks leak information

✅ No randomization occurs

---

# 🚩 Task 3 — Automate Cryptographic Analysis

## 🔹 Step 1 — Create Automated Analyzer

Create:

```text
scripts/automated_analyzer.py
```

The analyzer should:

* 📦 Extract APK
* 🔍 Scan vulnerabilities
* 📈 Calculate Risk Score
* 📝 Generate Report
* 💾 Export JSON

Implement every TODO in the supplied template.

---

## 🔹 Step 2 — Execute Automated Analysis

```bash
cd ~/crypto-lab/scripts

chmod +x automated_analyzer.py

python3 automated_analyzer.py \
../apk-files/sample-vulnerable-app.apk
```

---

## 🔹 Step 3 — Review JSON Output

```bash
cat ~/crypto-lab/apk-files/sample-vulnerable-app.apk_analysis.json
```

---

## 🔹 Step 4 — Create Executive Summary

Include:

* 📌 Total vulnerabilities
* 📌 Risk score
* 📌 Recommendations
* 📌 Remediation timeline

---

# 📊 Expected Outcomes

After completing this lab you should have successfully:

## 🔍 Vulnerability Discovery

* ✅ AES ECB usage
* ✅ Hardcoded keys
* ✅ Weak algorithms
* ✅ Missing IVs

---

## 🔐 ECB Demonstration

* ✅ Pattern preservation
* ✅ Identical ciphertext blocks
* ✅ CBC comparison
* ✅ Security explanation

---

## 🤖 Automation

Created tools capable of:

* ✔ APK Extraction
* ✔ Static Crypto Analysis
* ✔ Risk Assessment
* ✔ JSON Reporting

---

## 📄 Documentation

Generated:

* 📝 Scan Report
* 📝 Pattern Analysis
* 📝 JSON Findings
* 📝 Security Recommendations

---

# 🛡 Security Best Practices

Instead of:

❌ AES ECB

Use:

✅ AES-GCM

---

Instead of:

❌ Hardcoded Keys

Use:

✅ Android Keystore

---

Instead of:

❌ Static IV

Use:

✅ Random IV

---

Instead of:

❌ MD5

Use:

✅ SHA-256

---

Instead of:

❌ DES / RC4

Use:

✅ AES-256

---

# 🐞 Troubleshooting

## ❌ APKTool Errors

```bash
sudo apt install apktool
```

Verify:

* APK exists
* Sufficient storage
* Correct permissions

---

## ❌ Python Crypto Errors

```bash
pip3 install pycryptodome
```

Requirements:

* Python ≥ 3.6
* Remove legacy pycrypto

---

## ❌ No Vulnerabilities Found

Verify:

* Correct extraction directory
* Supported extensions
* Regular expression accuracy
* Test APK actually contains insecure crypto

---

# 📈 Skills Gained

After this lab you can confidently:

* 🔐 Audit Android cryptography
* 📱 Reverse APK encryption logic
* 🔍 Detect insecure implementations
* 🤖 Automate vulnerability discovery
* 📊 Produce professional security reports
* 🛡 Recommend secure cryptographic designs

---

# 🎓 Key Takeaways

✔ AES-ECB leaks patterns and should never protect sensitive information.

✔ Hardcoded keys inside APKs are easily extracted through static analysis.

✔ Automated scanners significantly improve mobile application security assessments.

✔ Modern Android applications should use AES-GCM together with Android Keystore for secure encryption and key management.

✔ Secure cryptography requires strong algorithms, authenticated encryption, random IVs, and proper secret management.

---

<div align="center">

## 🎉 Congratulations!

You have successfully completed the

# 🔐 Evaluate Crypto Libraries (AES in ECB Mode)

### Android Mobile Security Lab

**Happy Learning & Secure Coding! 🚀**

</div>

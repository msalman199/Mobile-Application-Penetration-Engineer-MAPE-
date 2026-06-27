# 📱 Reverse Malicious APK to Extract C2 Address

<div align="center">

# 🔍 Android Malware Reverse Engineering 

## Extract Command & Control (C2) Infrastructure from Malicious APKs

**Learn Android Reverse Engineering, Malware Analysis, String Decoding, and Threat Intelligence**

![Platform](https://img.shields.io/badge/Platform-Android-success?style=for-the-badge)
![Decompiler](https://img.shields.io/badge/Decompiler-JADX-blue?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Reverse%20Engineering-red?style=for-the-badge)
![Threat](https://img.shields.io/badge/Threat-Malware-orange?style=for-the-badge)
![Level](https://img.shields.io/badge/Difficulty-Intermediate-purple?style=for-the-badge)

</div>

---

# 📖 Overview

This lab introduces practical techniques for **reverse engineering malicious Android applications (APKs)** to discover their **Command and Control (C2)** infrastructure. Students will use **JADX** to decompile APKs, inspect Java source code, analyze Android manifests, extract strings from DEX files, decode obfuscated data, automate malware investigation with Python, and produce professional threat intelligence reports.

The lab demonstrates methodologies commonly used by:

* Mobile Security Analysts
* Malware Researchers
* Threat Intelligence Teams
* DFIR Analysts
* SOC Analysts
* Reverse Engineers

---

# 🎯 Objectives

By the end of this lab, you will be able to:

* ✅ Reverse engineer Android APK files using JADX
* ✅ Extract strings from DEX files
* ✅ Identify Command & Control (C2) servers
* ✅ Decode Base64, Hex, and ROT13 obfuscated strings
* ✅ Automate APK investigations using Python
* ✅ Produce professional malware analysis reports
* ✅ Generate Indicators of Compromise (IOCs)

---

# 📚 Prerequisites

Before starting this lab, students should have:

* Basic Android application knowledge
* Java programming familiarity
* Linux command-line experience
* Python scripting fundamentals
* Networking and TCP/IP knowledge

---

# 🖥️ Lab Environment

The provided Ubuntu 20.04 environment contains:

| Component        | Description                |
| ---------------- | -------------------------- |
| Operating System | Ubuntu 20.04               |
| Decompiler       | JADX                       |
| Python           | 3.8+                       |
| Sample Malware   | Malicious Android APK      |
| Linux Utilities  | unzip, strings, grep, file |

---

# 📂 Repository Structure

```text
Reverse-Malicious-APK-to-Extract-C2/
│
├── README.md
├── malicious_sample.apk
├── apk_hash.txt
├── all_strings.txt
├── decoded_results.txt
├── final_c2_list.txt
├── analysis_report.md
├── ioc_list.txt
│
├── jadx_output/
│
├── dex_files/
│
├── automated_analysis/
│   ├── analysis_report.txt
│   └── analysis_report.json
│
├── string_decoder.py
└── apk_analyzer.py
```

---

# 🚀 Task 1 — Environment Setup & Initial Analysis

---

## ✅ Step 1.1 Verify Tools and Create Workspace

Verify JADX installation.

```bash
jadx --version
```

Create a working directory.

```bash
mkdir -p ~/apk_analysis/lab10

cd ~/apk_analysis/lab10
```

Copy the sample malware.

```bash
cp /home/student/samples/malicious_sample.apk ./
```

---

## ✅ Step 1.2 Inspect the APK

Determine file information.

```bash
file malicious_sample.apk
```

Generate SHA256 hash.

```bash
sha256sum malicious_sample.apk > apk_hash.txt
```

Inspect APK contents.

```bash
unzip -l malicious_sample.apk | head -20
```

---

## ✅ Step 1.3 Reverse Engineer the APK

Decompile using JADX.

```bash
jadx -d jadx_output malicious_sample.apk
```

View project structure.

```bash
tree jadx_output -L 2
```

Open AndroidManifest.xml.

```bash
cat jadx_output/resources/AndroidManifest.xml
```

---

# 🔍 Task 2 — String Extraction & Analysis

---

## 📝 Step 2.1 Extract DEX Strings

Extract DEX files.

```bash
unzip -j malicious_sample.apk "*.dex" -d dex_files/
```

Extract strings.

```bash
strings dex_files/classes.dex > all_strings.txt
```

Count extracted strings.

```bash
wc -l all_strings.txt
```

---

## 🌐 Step 2.2 Search for C2 Indicators

Search for URLs.

```bash
grep -E "https?://" all_strings.txt > potential_urls.txt
```

Search for IP addresses.

```bash
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" all_strings.txt > potential_ips.txt
```

Search for domain names.

```bash
grep -E "[a-zA-Z0-9-]+\.(com|net|org|tk|ml|cc)" all_strings.txt > potential_domains.txt
```

Display discovered indicators.

```bash
echo "=== Potential C2 Indicators ==="

cat potential_urls.txt potential_ips.txt potential_domains.txt | sort -u
```

---

## 🔐 Step 2.3 Analyze Android Manifest

Find network permissions.

```bash
grep -i "permission" jadx_output/resources/AndroidManifest.xml | \
grep -E "(INTERNET|NETWORK)"
```

Find services and receivers.

```bash
grep -E "(service|receiver)" \
jadx_output/resources/AndroidManifest.xml
```

---

# 🧠 Task 3 — Analyze Decompiled Code

---

## 🔎 Step 3.1 Locate Network Classes

Navigate into source files.

```bash
cd jadx_output/sources/
```

Search for networking APIs.

```bash
find . -name "*.java" \
-exec grep -l "HttpURLConnection\|Socket\|URL" {} \; \
> network_classes.txt
```

Preview results.

```bash
head -5 network_classes.txt
```

---

## 🌍 Step 3.2 Review Network Communication

Search for URL creation.

```bash
grep -r "new URL\|URL(" . --include="*.java" | head -10
```

Search socket communication.

```bash
grep -r "Socket\|connect(" . --include="*.java" | head -10
```

Find dynamically generated URLs.

```bash
grep -r "StringBuilder\|StringBuffer" . \
--include="*.java" | grep -i http
```

---

## ⚙️ Step 3.3 Identify Configuration Files

Locate configuration classes.

```bash
find . -name "*[Cc]onfig*.java" \
-o -name "*[Ss]etting*.java"
```

Search for hardcoded strings.

```bash
grep -r "final.*String.*=" . \
--include="*.java" \
| grep -E "(http|[0-9]{1,3}\.)"
```

---

# 🔓 Task 4 — Decode Obfuscated Strings

---

## 🐍 Step 4.1 Create String Decoder

Create the decoder script.

```bash
nano string_decoder.py
```

The decoder should support:

* Base64 decoding
* Hex decoding
* ROT13 decoding
* URL detection
* Domain detection
* IP detection
* Automated C2 identification

Core functions include:

* `decode_base64()`
* `decode_hex()`
* `rot13_decode()`
* `is_potential_c2()`
* `analyze_strings()`

---

## ▶️ Step 4.2 Execute Decoder

Make executable.

```bash
chmod +x string_decoder.py
```

Run the decoder.

```bash
python3 string_decoder.py > decoded_results.txt
```

Review findings.

```bash
cat decoded_results.txt
```

---

# 🤖 Task 5 — Automated APK Analysis

---

## 🛠️ Step 5.1 Build APK Analyzer

Create analyzer.

```bash
nano apk_analyzer.py
```

Implement methods for:

* Environment setup
* APK decompilation
* String extraction
* C2 detection
* Permission analysis
* Report generation
* Complete analysis workflow

---

## ▶️ Step 5.2 Execute Analyzer

Run analysis.

```bash
python3 apk_analyzer.py
```

Review generated reports.

```bash
cat automated_analysis/analysis_report.txt
```

```bash
cat automated_analysis/analysis_report.json
```

---

# 📄 Task 6 — Documentation & Reporting

---

## 📝 Step 6.1 Create Security Report

Generate a professional report containing:

* Executive Summary
* APK Information
* Methodology
* Key Findings
* Network Permissions
* Extracted C2 Infrastructure
* Communication Methods
* Obfuscation Techniques
* Risk Assessment
* Recommendations
* Technical Appendix

---

## 🚨 Step 6.2 Generate IOC List

Create an IOC document including:

* MD5
* SHA1
* SHA256
* C2 Domains
* IP Addresses
* URLs
* Suspicious Permissions
* Package Names

Append file hashes.

```bash
md5sum malicious_sample.apk >> ioc_list.txt

sha256sum malicious_sample.apk >> ioc_list.txt
```

---

## 📋 Step 6.3 Consolidate Findings

Merge all discovered C2 indicators.

```bash
cat potential_urls.txt \
potential_ips.txt \
potential_domains.txt \
decoded_results.txt \
| sort -u > final_c2_list.txt
```

Display results.

```bash
echo "=== Final C2 Address List ==="

cat final_c2_list.txt
```

---

# 📊 Expected Outcomes

Upon successful completion you should have:

* ✅ Decompiled a malicious Android APK
* ✅ Extracted strings from DEX files
* ✅ Identified multiple C2 indicators
* ✅ Decoded obfuscated strings
* ✅ Built automated malware analysis tools
* ✅ Generated professional malware reports
* ✅ Produced IOC documentation

Your `final_c2_list.txt` should contain approximately **5–10 unique C2 indicators** discovered through multiple analysis techniques.

---

# 🔍 Indicators of Compromise (IOCs)

Examples of artifacts collected include:

### 🌐 Network IOCs

* C2 Domains
* C2 IP Addresses
* URLs
* HTTP Endpoints

---

### 📱 Android Artifacts

* Package Names
* Services
* Broadcast Receivers
* Activities
* Permissions

---

### 🔐 Cryptographic Artifacts

* Base64 Strings
* Hex Strings
* ROT13 Data
* Obfuscated URLs

---

### 📄 File Artifacts

* SHA256
* SHA1
* MD5
* APK Metadata

---

# 🛠️ Troubleshooting

---

## ❌ JADX Decompilation Fails

Force decompilation.

```bash
jadx --show-bad-code \
-d output \
malicious_sample.apk
```

---

## ❌ No Strings Extracted

Verify DEX extraction.

```bash
file dex_files/*.dex
```

Ensure the `strings` utility exists.

---

## ❌ Python Import Errors

Install required packages.

```bash
pip3 install requests
```

---

## ❌ Unable to Locate C2

Check for:

* Dynamic URL generation
* Configuration classes
* String concatenation
* Reflection
* Encoded strings
* Network-related imports

---

# 🏆 Skills Acquired

After completing this lab you will understand:

* Android reverse engineering
* APK decompilation
* JADX usage
* Manifest analysis
* DEX string extraction
* Malware configuration analysis
* C2 infrastructure discovery
* Obfuscation techniques
* Threat hunting
* IOC generation
* Python malware automation
* Threat intelligence reporting

---

# 📖 Key Takeaways

* Static analysis often exposes hidden C2 infrastructure.
* Reverse engineering reveals malware communication logic without execution.
* Combining multiple extraction techniques improves detection accuracy.
* Obfuscated strings can frequently be decoded using common encoding schemes.
* Automation enables scalable malware triage and repeatable investigations.
* Proper IOC documentation supports incident response and threat intelligence.

---

# 🚀 Next Steps

Expand your malware analysis skills by exploring:

* Android dynamic analysis
* Frida instrumentation
* Smali reverse engineering
* APK unpacking techniques
* Malware sandboxing
* Threat intelligence integration
* YARA rule development
* Mobile threat hunting

---

# ⚠️ Security Note

> **Always analyze malware inside isolated virtual machines or dedicated malware analysis environments. Never execute suspicious APKs on personal or production Android devices. Follow responsible malware handling practices and ensure all extracted indicators are validated before operational use.**

---

<div align="center">

# 🎓 Lab Completed Successfully

**You have successfully learned how to reverse engineer Android malware, extract Command & Control (C2) infrastructure, decode obfuscated strings, automate APK investigations with Python, and produce professional threat intelligence reports.**

⭐ **Happy Reverse Engineering & Stay Secure!**

</div>

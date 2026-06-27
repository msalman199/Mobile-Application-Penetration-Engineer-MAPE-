# 📱 Root Android Emulator (Magisk + ADB Shell)

> **Hands-on Mobile Application Penetration Testing Lab**  
> Learn how to configure a rootable Android emulator, install **Magisk**, verify root access using **ADB Shell**, and automate security validation using **Python**.

---

## 🎯 Objectives

By the end of this lab, you will be able to:

- ✅ Configure and launch an Android emulator using rootable system images
- ✅ Install and configure **Magisk** for systemless root management
- ✅ Use **ADB Shell** to interact with a rooted Android device
- ✅ Verify root access manually and programmatically
- ✅ Automate root verification using Python
- ✅ Understand the security implications of rooted Android devices

---

# 🛠 Technology Stack

<p align="center">

![Android](https://img.shields.io/badge/Android-11-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Magisk](https://img.shields.io/badge/Magisk-v26.4-blue?style=for-the-badge)
![ADB](https://img.shields.io/badge/ADB-Platform--Tools-success?style=for-the-badge)
![Fastboot](https://img.shields.io/badge/Fastboot-Bootloader-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?style=for-the-badge&logo=ubuntu)

</p>

---

# 📚 Prerequisites

Before beginning this lab, you should have:

- Basic Linux command-line experience
- Understanding of Android operating system architecture
- Familiarity with Android SDK tools
- Basic Python programming knowledge
- Experience using terminal environments

---

# 🖥 Lab Environment

This lab uses a pre-configured Ubuntu cloud workstation containing:

- Ubuntu 22.04 LTS
- Android SDK
- Android Platform Tools
- Android Emulator
- Python 3.x
- Fastboot
- ADB
- Android Virtual Device Manager

Simply click **Start Lab** to access the environment.

---

# 📊 Lab Workflow

```text
        Android SDK
             │
             ▼
   Download System Image
             │
             ▼
      Create Android AVD
             │
             ▼
      Launch Emulator
             │
             ▼
      Install Magisk
             │
             ▼
     Patch Boot Image
             │
             ▼
      Flash Boot Image
             │
             ▼
      Verify Root Access
```

---

# 🚀 Task 1 — Prepare Android Emulator Environment

---

# 🎯 Goal

Before rooting an Android device, we must prepare a virtual Android environment capable of supporting root access.

During this task you will:

- Verify Android SDK
- Download a compatible Android image
- Create a new Android Virtual Device (AVD)

---

# 🛠 Step 1.1 — Verify Android SDK Installation

First verify that the Android SDK is correctly installed.

Display the Android SDK path.

```bash
echo $ANDROID_HOME
```

---

Check the installed ADB version.

```bash
adb --version
```

Example output:

```text
Android Debug Bridge version 1.0.41
```

---

List available Android Virtual Devices.

```bash
emulator -list-avds
```

Expected output:

```text
Pixel_API_30

RootableEmulator
```

---

# ✅ Verification Checklist

Confirm the following:

- Android SDK installed
- Platform Tools available
- Emulator installed
- Existing AVDs detected

---

# 🛠 Step 1.2 — Download a Rootable Android Image

Update the Android SDK Manager.

```bash
sdkmanager --update
```

---

Download the Android 11 Google APIs x86_64 image.

```bash
sdkmanager "system-images;android-30;google_apis;x86_64"
```

---

Verify the installed packages.

```bash
sdkmanager --list_installed
```

Expected output includes:

```text
system-images

android-30

google_apis

x86_64
```

---

# 📦 Installed Components

| Component | Purpose |
|------------|----------|
| Android 11 | Emulator OS |
| Google APIs | Emulator Services |
| x86_64 | Hardware Architecture |
| Platform Tools | ADB & Fastboot |

---

# 🛠 Step 1.3 — Create an Android Virtual Device

Create a new emulator.

```bash
avdmanager create avd \
--name RootableEmulator \
--package "system-images;android-30;google_apis;x86_64" \
--device "pixel_4"
```

---

Verify the AVD.

```bash
avdmanager list avd
```

Example output:

```text
Name: RootableEmulator

Device: Pixel 4

API Level: 30
```

---

# 📊 Task 1 Summary

At this point you have:

- ✅ Installed Android SDK
- ✅ Downloaded Android 11 image
- ✅ Created a Pixel 4 emulator
- ✅ Prepared a rootable Android device

---

# 🚀 Task 2 — Install & Configure Magisk

---

# 🎯 Goal

Magisk is the industry-standard tool for obtaining **systemless root** on Android devices.

Unlike traditional rooting methods, Magisk modifies the boot image instead of the system partition, making it safer and easier to manage.

During this task you will:

- Download Magisk
- Launch the emulator
- Enable writable system mode
- Patch the boot image
- Flash the patched boot image

---

# 📊 Rooting Workflow

```text
Download Magisk

↓

Launch Emulator

↓

ADB Root

↓

Writable System

↓

Extract boot.img

↓

Patch boot.img

↓

Flash Patched Image

↓

Root Access
```

---

# 🛠 Step 2.1 — Download Magisk

Create a working directory.

```bash
mkdir -p ~/android-root-lab

cd ~/android-root-lab
```

---

Download Magisk.

```bash
wget -O magisk.apk \
"https://github.com/topjohnwu/Magisk/releases/download/v26.4/Magisk-v26.4.apk"
```

---

Verify the download.

```bash
ls -lh magisk.apk
```

Example output:

```text
magisk.apk

12 MB
```

---

# 🛠 Step 2.2 — Launch the Emulator

Start the emulator with a writable system partition.

```bash
emulator \
-avd RootableEmulator \
-writable-system \
-no-snapshot-load &
```

---

Allow Android to boot.

```bash
sleep 120
```

---

Verify the emulator is online.

```bash
adb devices
```

Example:

```text
List of devices attached

emulator-5554 device
```

---

# 🛠 Step 2.3 — Prepare the System Partition

Restart ADB with elevated privileges.

```bash
adb root
```

---

Remount the system partition.

```bash
adb remount
```

---

Verify the mount status.

```bash
adb shell mount | grep system
```

---

Install Magisk.

```bash
adb install magisk.apk
```

Example output:

```text
Success
```

---

# 🛠 Step 2.4 — Extract the Boot Image

Dump the boot partition.

```bash
adb shell \
"dd if=/dev/block/by-name/boot of=/data/local/tmp/boot.img"
```

---

Copy the boot image to the host.

```bash
adb pull /data/local/tmp/boot.img ./
```

---

Verify extraction.

```bash
ls -lh boot.img
```

---

# 🛠 Step 2.5 — Patch & Flash the Boot Image

Push the boot image to the emulator.

```bash
adb push boot.img /sdcard/Download/
```

---

Inside the emulator:

1. Open **Magisk**
2. Tap **Install**
3. Select **Select and Patch a File**
4. Choose:

```text
boot.img
```

5. Wait for patching to finish.

---

Locate the patched image.

```bash
adb shell ls /sdcard/Download/magisk_patched*
```

---

Copy it back to the host.

```bash
adb pull \
/sdcard/Download/magisk_patched-*.img \
./magisk_patched.img
```

---

Reboot into the bootloader.

```bash
adb reboot bootloader
```

Wait a few seconds.

```bash
sleep 10
```

---

Flash the patched boot image.

```bash
fastboot flash boot magisk_patched.img
```

---

Reboot Android.

```bash
fastboot reboot
```

Allow Android to fully boot.

```bash
sleep 120
```

---

# 📊 Task 2 Summary

You have successfully:

- ✅ Downloaded Magisk
- ✅ Installed Magisk APK
- ✅ Extracted the boot image
- ✅ Patched the boot image
- ✅ Flashed the patched boot image
- ✅ Prepared the emulator for root access

---

# 🎉 Part 1 Complete

You have successfully:

- 📱 Configured a rootable Android emulator
- 🛠 Installed the Android SDK components
- 📦 Created a Pixel 4 Android Virtual Device
- 🔓 Installed Magisk
- 💾 Patched the Android boot image
- 🚀 Flashed the patched boot image

---

➡️ **Next:** **Part 2** covers:

- 🔍 Verifying Root Access with ADB Shell
- 🛠 Testing `su` and Magisk
- 📜 Creating an Automated Bash Root Verification Script
- ✅ Confirming Root Access Using Multiple Methods
# 🚀 Task 3 — Verify Root Access

---

# 🎯 Goal

After patching and flashing the boot image, it is essential to verify that the Android emulator has been successfully rooted.

In this task you will:

- Connect to the emulator using **ADB Shell**
- Verify root privileges
- Confirm Magisk installation
- Create an automated Bash verification script

---

# 📊 Root Verification Workflow

```text
        Android Emulator
               │
               ▼
         Connect via ADB
               │
               ▼
          Launch Shell
               │
               ▼
         Request Root (su)
               │
               ▼
        Verify User Identity
               │
               ▼
      Confirm Magisk Version
               │
               ▼
      Execute Verification Script
```

---

# 🛠 Step 3.1 — Verify Root Using ADB Shell

Connect to the Android shell.

```bash
adb shell
```

---

Request root access.

```bash
su
```

If Magisk prompts for permission, allow root access.

---

Verify the current user ID.

```bash
id
```

Expected output:

```text
uid=0(root)
gid=0(root)
groups=0(root)
```

---

Verify the active username.

```bash
whoami
```

Expected output:

```text
root
```

---

Verify the installed Magisk version.

```bash
magisk --version
```

Example output:

```text
26.4
```

---

Exit the root shell.

```bash
exit
```

Exit the ADB shell.

```bash
exit
```

---

# ✅ Successful Root Verification

A successful verification confirms:

| Test | Expected Result |
|------|-----------------|
| ADB Shell | Connected |
| `su` | Granted |
| `id` | uid=0 |
| `whoami` | root |
| `magisk --version` | Displays Version |

---

# 📊 Root Privilege Comparison

| Command | Non-Root Device | Rooted Device |
|----------|----------------|---------------|
| id | uid=2000(shell) | uid=0(root) |
| whoami | shell | root |
| su | Permission Denied | Root Granted |
| magisk --version | Not Found | Installed |

---

# 🔍 Understanding Root Privileges

Root access provides unrestricted control over the Android operating system.

Examples of privileged operations include:

- Reading protected application data
- Modifying system files
- Installing system applications
- Capturing application memory
- Changing SELinux policies
- Accessing protected partitions

---

# 🚀 Step 3.2 — Create an Automated Root Verification Script

Manual verification works well for individual tests, but automated validation is essential during security assessments.

Create the verification script.

```text
verify_root.sh
```

---

# 📦 Script Responsibilities

The script automatically verifies:

- Device connectivity
- Presence of the `su` binary
- Root privileges
- Magisk installation

---

# 🧩 Verification Workflow

```text
Device Connected

↓

Check su Binary

↓

Verify Root Access

↓

Check Magisk

↓

Display Report
```

---

# ▶ Create the Script

Create the file.

```bash
nano verify_root.sh
```

Paste the verification script provided in the lab manual.

---

# Make the Script Executable

```bash
chmod +x verify_root.sh
```

---

# Execute the Script

```bash
./verify_root.sh
```

---

# 📊 Example Output

```text
=== Root Verification Script ===

[PASS] Device connected

[PASS] su binary found

[PASS] Root access confirmed

[PASS] Magisk installed

=== Verification Complete ===
```

---

# 🔍 Script Logic

The script performs the following checks:

## Device Connectivity

```bash
adb get-state
```

Expected:

```text
device
```

---

## Verify `su` Binary

```bash
adb shell which su
```

Expected:

```text
/system/bin/su
```

or

```text
/system/xbin/su
```

---

## Test Root Access

```bash
adb shell "su -c id"
```

Expected:

```text
uid=0(root)
```

---

## Verify Magisk Installation

```bash
adb shell "magisk --version"
```

Expected:

```text
26.4
```

---

# 📈 Verification Results

| Verification | Expected Status |
|--------------|-----------------|
| Device Connected | ✅ PASS |
| su Binary Found | ✅ PASS |
| Root Privileges | ✅ PASS |
| Magisk Installed | ✅ PASS |

---

# 📄 Common Verification Commands

Check device status.

```bash
adb devices
```

---

Verify root.

```bash
adb shell su -c id
```

---

Check current user.

```bash
adb shell whoami
```

---

Display Magisk version.

```bash
adb shell magisk --version
```

---

Locate the `su` binary.

```bash
adb shell which su
```

---

# ⚠ Common Verification Issues

| Issue | Cause | Solution |
|--------|-------|----------|
| Device Offline | Emulator not fully booted | Wait and reconnect |
| `su` Not Found | Root not installed | Reflash patched boot image |
| Permission Denied | Magisk request rejected | Grant root permission in Magisk |
| Magisk Command Missing | Installation failed | Reinstall Magisk APK |

---

# 🔐 Security Considerations

A rooted Android device:

- Allows unrestricted system access
- Can bypass application sandboxing
- Increases attack surface
- Enables advanced penetration testing
- Should **never** be used as a production device without understanding the associated risks

---

# 📈 Skills Developed

By completing this section, you have learned how to:

- ✅ Connect to Android using ADB Shell
- ✅ Verify root privileges
- ✅ Test the `su` binary
- ✅ Confirm Magisk installation
- ✅ Automate root verification using Bash
- ✅ Validate a rooted Android environment

---

# 🎉 Part 2 Complete

You have successfully:

- 📱 Verified root access using ADB
- 🔓 Confirmed elevated privileges
- 🛠 Validated Magisk installation
- 📜 Created an automated Bash verification script
- ✅ Confirmed that the emulator is fully rooted

---

➡️ **Next:** **Part 3** covers:

- 🐍 Automating Root Analysis with Python
- 📊 Building the `AndroidRootChecker` class
- 🔄 Testing Root Persistence Across Reboots
- 🛡 Creating a Comprehensive Android Security Assessment Tool
# 🚀 Task 4 — Automate Root Analysis with Python

---

# 🎯 Goal

Manual verification is useful during initial setup, but automated validation is essential for repeatable penetration testing and mobile security assessments.

In this task, you will develop Python-based automation tools to:

- Detect Android root status
- Verify Magisk installation
- Test root persistence across reboots
- Perform automated Android security assessments
- Generate JSON security reports

These tools emulate the type of automation commonly used by mobile penetration testers and security researchers.

---

# 📊 Automation Workflow

```text
           Android Emulator
                   │
                   ▼
            Python Scripts
                   │
      ┌────────────┼────────────┐
      │            │            │
      ▼            ▼            ▼
 Root Checker  Persistence  Security Assessment
      │            │            │
      └────────────┼────────────┘
                   ▼
           JSON Security Reports
```

---

# 🐍 Step 4.1 — Build the Android Root Checker

Create the following file.

```text
android_root_checker.py
```

---

# 📦 Responsibilities

The script should automatically:

- Verify ADB connectivity
- Detect the `su` binary
- Test root privileges
- Detect Magisk
- Generate a report
- Export results to JSON

---

# 🧩 Class Structure

```text
AndroidRootChecker

│
├── __init__()
├── run_adb_command()
├── check_device_connection()
├── check_su_binary()
├── check_root_access()
├── check_magisk_installation()
├── generate_report()
├── save_results()
└── run_full_analysis()
```

---

# 📋 Device Connection Check

The first validation ensures the emulator is available through ADB.

Command executed:

```bash
adb devices
```

Expected output:

```text
emulator-5554 device
```

---

# 🔓 Verify the `su` Binary

The script checks whether the Superuser binary exists.

Command:

```bash
adb shell which su
```

Expected output:

```text
/system/bin/su
```

or

```text
/system/xbin/su
```

---

# 👑 Verify Root Access

Test elevated privileges.

Command:

```bash
adb shell su -c id
```

Expected:

```text
uid=0(root)
```

---

# 🧿 Detect Magisk

Verify Magisk installation.

```bash
adb shell magisk --version
```

Expected output:

```text
26.4
```

---

# 📄 JSON Report Example

```json
{
    "device_connected": true,
    "root_access": true,
    "su_binary_present": true,
    "magisk_installed": true
}
```

---

# ▶ Execute the Script

```bash
python3 android_root_checker.py
```

---

# 📊 Example Console Output

```text
Android Root Analysis

Device Connected

PASS

su Binary

PASS

Root Access

PASS

Magisk Installed

PASS

Results Saved
```

---

# 🚀 Step 4.2 — Test Root Persistence

Root access should remain available after rebooting the emulator.

Create:

```text
test_root_persistence.py
```

---

# 📦 Responsibilities

The persistence tester should:

- Verify root before reboot
- Reboot Android
- Wait for boot completion
- Verify root after reboot
- Confirm Magisk persistence
- Generate a JSON report

---

# 📊 Persistence Workflow

```text
Verify Root

↓

Reboot Device

↓

Wait for Boot

↓

Verify Root Again

↓

Confirm Magisk

↓

Generate Report
```

---

# 🔄 Verify Root Before Reboot

Command executed:

```bash
adb shell su -c id
```

Expected:

```text
uid=0(root)
```

---

# 🔁 Reboot the Emulator

```bash
adb reboot
```

Wait until Android becomes available again.

```bash
adb get-state
```

Expected:

```text
device
```

---

# 🔍 Verify Root After Reboot

Execute once again.

```bash
adb shell su -c id
```

Expected:

```text
uid=0(root)
```

---

# 🧿 Verify Magisk Persistence

Check whether Magisk remains installed.

```bash
adb shell magisk --version
```

---

# 📄 Persistence Report

Example:

```json
{
    "root_before": true,
    "root_after": true,
    "magisk_present": true,
    "persistence_verified": true
}
```

---

# ▶ Execute

```bash
python3 test_root_persistence.py
```

---

# 📊 Example Output

```text
Root Before Reboot

PASS

Device Rebooted

PASS

Root After Reboot

PASS

Magisk Present

PASS

Persistence Verified
```

---

# 🚀 Step 4.3 — Build the Android Security Assessment Tool

Create:

```text
security_assessment.py
```

---

# 🎯 Purpose

This script evaluates the security posture of the rooted Android emulator.

---

# 📦 Assessment Responsibilities

The tool should:

- Gather Android system information
- Verify Android version
- Check API level
- Retrieve security patch level
- Inspect SELinux status
- Detect root
- Assess device risk
- Generate a security report

---

# 🧩 Class Structure

```text
AndroidSecurityAssessment

│
├── gather_system_info()
├── check_selinux_status()
├── analyze_root_status()
├── check_security_patch_level()
├── assess_risk_level()
├── generate_security_report()
└── run_assessment()
```

---

# 📋 Collect System Information

Commands executed include:

```bash
adb shell getprop ro.build.version.release
```

```bash
adb shell getprop ro.build.version.sdk
```

```bash
adb shell getprop ro.build.version.security_patch
```

```bash
adb shell getenforce
```

---

# 🔒 Verify SELinux Status

Possible outputs:

```text
Enforcing
```

or

```text
Permissive
```

A permissive configuration should be reported as a security finding.

---

# 👑 Analyze Root Status

Determine whether root is enabled.

Command:

```bash
adb shell su -c id
```

If root is available:

- Risk Level increases
- Recommendations are generated

---

# 🛡 Evaluate Security Patch Level

Retrieve:

```bash
adb shell getprop ro.build.version.security_patch
```

Example:

```text
2024-06-05
```

Outdated patch levels should be highlighted during the assessment.

---

# 📊 Risk Levels

| Risk | Description |
|------|-------------|
| 🟢 Low | Secure configuration |
| 🟡 Medium | Minor weaknesses |
| 🟠 High | Root enabled or outdated patches |
| 🔴 Critical | Multiple high-risk findings |

---

# 📄 Example Security Report

```json
{
    "risk_level":"HIGH",
    "root_enabled":true,
    "selinux":"Permissive",
    "security_patch":"2024-06-05"
}
```

---

# ▶ Execute

```bash
python3 security_assessment.py
```

---

# 📊 Example Console Output

```text
Android Security Assessment

Android Version

11

API Level

30

SELinux

Enforcing

Root Status

Enabled

Overall Risk

HIGH

Security Report Saved
```

---

# 📈 Skills Developed

During this task you learned how to:

- ✅ Automate Android root detection
- ✅ Verify ADB connectivity
- ✅ Detect the `su` binary
- ✅ Confirm Magisk installation
- ✅ Test root persistence
- ✅ Gather Android system information
- ✅ Assess device security posture
- ✅ Export JSON security reports

---

# 🎉 Part 3 Complete

You have successfully:

- 🐍 Built an automated Android Root Checker
- 🔍 Verified root using Python
- 🔄 Tested root persistence across reboots
- 🛡 Created a comprehensive Android Security Assessment tool
- 📊 Generated machine-readable JSON reports
- 🚀 Automated repetitive mobile security validation tasks

---

➡️ **Next:** **Part 4** covers:

- 📋 Expected Outcomes
- 🛠 Troubleshooting Guide
- 🔐 Security Best Practices
- 📚 Key Takeaways
- 🎓 Learning Outcomes
- ⚠ Disclaimer
- 🤝 Contributing
- ⭐ Support
# 🚀 Lab Verification & Final Assessment

---

# ✅ Lab Verification Checklist

Use the following checklist to verify that all lab objectives have been completed successfully.

| Verification Item | Status |
|-------------------|--------|
| Android SDK Verified | ✅ |
| Android 11 System Image Installed | ✅ |
| Android Virtual Device Created | ✅ |
| Emulator Launched Successfully | ✅ |
| Writable System Enabled | ✅ |
| Magisk APK Installed | ✅ |
| Boot Image Extracted | ✅ |
| Boot Image Patched | ✅ |
| Patched Boot Image Flashed | ✅ |
| Root Access Verified | ✅ |
| Magisk Operational | ✅ |
| Bash Verification Script Executed | ✅ |
| Python Root Checker Completed | ✅ |
| Root Persistence Tested | ✅ |
| Security Assessment Completed | ✅ |
| JSON Reports Generated | ✅ |

---

# 📁 Expected Project Structure

```text
android-root-lab/

├── magisk.apk
├── boot.img
├── magisk_patched.img
│
├── verify_root.sh
├── android_root_checker.py
├── test_root_persistence.py
├── security_assessment.py
│
├── root_analysis.json
├── persistence_report.json
├── security_assessment.json
│
├── reports/
├── logs/
└── screenshots/
```

---

# 📊 Validate Generated Files

Verify all reports exist.

```bash
ls -lh *.json
```

---

Validate JSON formatting.

```bash
python3 -m json.tool root_analysis.json
```

```bash
python3 -m json.tool persistence_report.json
```

```bash
python3 -m json.tool security_assessment.json
```

---

# 📈 Expected Outcomes

After successfully completing this lab you should be able to:

- 📱 Configure Android emulators for penetration testing
- 🔓 Root Android using Magisk
- 🛠 Patch and flash Android boot images
- 💻 Use ADB Shell with elevated privileges
- 🐍 Automate root verification using Python
- 🔄 Test root persistence across device reboots
- 📊 Generate automated security reports
- 🛡 Assess the security posture of rooted Android devices

---

# 🔐 Security Implications of Root Access

Rooting an Android device introduces several important security considerations.

## Advantages

- Complete system visibility
- Access protected application data
- Dynamic application testing
- Memory analysis
- System modification
- Malware analysis
- Reverse engineering support
- Penetration testing capabilities

---

## Risks

- Reduced platform security
- Increased attack surface
- Application sandbox bypass
- Potential malware abuse
- Integrity verification failures
- Sensitive data exposure
- Incompatibility with secure applications

---

# 📊 Rooted vs Non-Rooted Devices

| Feature | Standard Device | Rooted Device |
|----------|----------------|---------------|
| System File Access | ❌ | ✅ |
| Install System Apps | ❌ | ✅ |
| Access Protected Directories | ❌ | ✅ |
| Modify SELinux | ❌ | ✅ |
| Application Sandboxing | Enabled | Can Be Bypassed |
| Full Filesystem Access | ❌ | ✅ |
| Advanced Security Testing | Limited | Full Capability |

---

# 🛠 Troubleshooting Guide

---

## ❌ Emulator Will Not Start

### Symptoms

```text
PANIC: Missing emulator engine program
```

### Solutions

Verify virtualization support.

```bash
egrep -c "(vmx|svm)" /proc/cpuinfo
```

Check available AVDs.

```bash
emulator -list-avds
```

Start emulator using software rendering.

```bash
emulator \
-avd RootableEmulator \
-no-boot-anim \
-gpu swiftshader_indirect
```

---

## ❌ ADB Cannot Detect Device

### Symptoms

```text
no devices found
```

### Restart the ADB server.

```bash
adb kill-server

adb start-server
```

Reconnect devices.

```bash
adb devices
```

---

## ❌ Root Access Denied

### Symptoms

```text
Permission denied
```

### Solutions

Verify the patched boot image was flashed.

```bash
fastboot flash boot magisk_patched.img
```

Reboot Android.

```bash
adb reboot
```

Ensure Magisk granted Superuser permissions.

---

## ❌ Magisk Application Crashes

### Solution

Clear application data.

```bash
adb shell pm clear com.topjohnwu.magisk
```

Reinstall Magisk.

```bash
adb install -r magisk.apk
```

Review logs.

```bash
adb logcat | grep Magisk
```

---

## ❌ Boot Loop After Flashing

### Possible Causes

- Incorrect boot image
- Corrupted patched image
- Unsupported Android image

### Recovery

Flash the original boot image.

```bash
fastboot flash boot boot.img
```

Reboot.

```bash
fastboot reboot
```

---

# 🛡 Security Best Practices

When working with rooted Android devices:

- Use rooted devices only for testing and research.
- Never root production or personal devices without understanding the risks.
- Keep Magisk updated to the latest stable release.
- Grant Superuser permissions only to trusted applications.
- Monitor changes to the system partition.
- Use snapshots before making significant modifications.
- Restrict ADB access to trusted environments.
- Regularly review installed Magisk modules.

---

# 📚 Key Takeaways

- Android emulators provide a safe environment for security testing.
- Magisk enables **systemless root**, preserving the system partition while providing administrative access.
- ADB is a powerful interface for interacting with Android devices.
- Python automation significantly improves efficiency and repeatability in mobile security assessments.
- Root persistence testing ensures that elevated privileges remain available after rebooting.
- Security assessments help identify configuration weaknesses and hardening opportunities.

---

# 🎓 Learning Outcomes

By completing this lab, you can now:

- Configure Android emulators for mobile penetration testing.
- Install and configure Magisk for root management.
- Extract, patch, and flash Android boot images.
- Verify root access using ADB Shell.
- Automate Android root validation with Python.
- Test root persistence across system reboots.
- Assess Android device security posture.
- Generate professional JSON-based assessment reports.

---

# 🚀 Next Labs

Continue your Mobile Application Penetration Testing journey with:

- 📱 Android Application Reverse Engineering
- 🔍 Static APK Analysis
- ⚡ Dynamic Analysis with Frida
- 🧠 Memory Dump Analysis
- 🔐 Android Keystore Security
- 🌐 Mobile API Security Testing
- 📦 APK Repackaging
- 🕵 Runtime Instrumentation
- 📡 HTTPS Traffic Interception
- 📱 Mobile Malware Analysis

---

# ⚠ Disclaimer

This lab is intended **solely for educational purposes, cybersecurity training, mobile security research, and authorized penetration testing**.

Only perform rooting, reverse engineering, and security assessments on devices and applications that you own or have explicit authorization to test. Unauthorized activities may violate organizational policies, contracts, or applicable laws.

---

# 🤝 Contributing

Contributions are welcome!

You can help improve this repository by:

- 📚 Adding new Android security labs
- 🐍 Enhancing Python automation tools
- 🔧 Improving Magisk and ADB workflows
- 📝 Expanding documentation
- 🐛 Reporting bugs
- 🚀 Optimizing scripts
- 📊 Adding additional security checks

---

# ⭐ Support

If you found this repository useful:

- ⭐ Star the repository
- 🍴 Fork the repository
- 📢 Share it with the cybersecurity community
- 🤝 Contribute new mobile security content

---

<div align="center">

# 📱 Master Android Rooting, Automation & Mobile Security Assessment

### 🚀 Happy Learning & Happy Hacking (Ethically)!

</div>
- 
- 
- 

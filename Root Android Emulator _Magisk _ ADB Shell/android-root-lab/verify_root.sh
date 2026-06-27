#!/bin/bash

echo "=== Root Verification Script ==="

# Check device connection
if adb get-state &>/dev/null; then
    echo "[PASS] Device connected"
else
    echo "[FAIL] Device not connected"
    exit 1
fi

# Check su binary
if adb shell "which su" &>/dev/null; then
    echo "[PASS] su binary found"
else
    echo "[FAIL] su binary not found"
fi

# Test root access
if adb shell "su -c 'id'" 2>/dev/null | grep -q "uid=0"; then
    echo "[PASS] Root access confirmed"
else
    echo "[FAIL] Root access denied"
fi

# Check Magisk
if adb shell "magisk --version" &>/dev/null; then
    echo "[PASS] Magisk installed"
else
    echo "[FAIL] Magisk not found"
fi

echo "=== Verification Complete ==="

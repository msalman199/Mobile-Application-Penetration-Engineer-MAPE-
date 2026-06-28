Java.perform(function() {
    console.log("[+] Starting Frida hook script");
    
    // Hook the LoginActivity class
    var LoginActivity = Java.use("com.example.vulnlogin.LoginActivity");
    
    // Hook the validateCredentials method
    LoginActivity.validateCredentials.implementation = function(username, password) {
        console.log("[+] validateCredentials called");
        console.log("[+] Username: " + username);
        console.log("[+] Password: " + password);
        
        // Call original method and capture result
        var result = this.validateCredentials(username, password);
        console.log("[+] Original result: " + result);
        
        return result;
    };
    
    console.log("[+] Hook installed successfully");
});

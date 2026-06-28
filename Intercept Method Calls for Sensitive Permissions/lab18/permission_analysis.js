// Permission Analysis Script
console.log("[*] Starting permission method analysis...");

Java.perform(function() {
    // TODO: Hook ContextWrapper.checkSelfPermission
    // Hint: Use Java.use("android.content.ContextWrapper")
    // Log the permission parameter and return value
    
    // TODO: Hook ActivityCompat.checkSelfPermission
    // Hint: Use Java.use("androidx.core.app.ActivityCompat")
    // This method takes context and permission as parameters
    
    // TODO: Hook PackageManager.checkPermission
    // Hint: Use Java.use("android.content.pm.PackageManager")
    // Log both permission name and package name
    
    console.log("[+] Permission analysis hooks installed");
});

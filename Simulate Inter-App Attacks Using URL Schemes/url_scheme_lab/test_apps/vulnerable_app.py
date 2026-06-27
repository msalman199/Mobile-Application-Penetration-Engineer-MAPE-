#!/usr/bin/env python3
import sys
import urllib.parse
from datetime import datetime

class VulnerableApp:
    def __init__(self):
        self.app_name = "VulnBank"
        self.log_file = "../logs/app_activity.log"
        
    def log_activity(self, action, data):
        """
        Log application activity to file.
        
        Args:
            action: Type of action performed
            data: Data associated with the action
        """
        # TODO: Implement timestamp generation
        # TODO: Format log entry with timestamp, app_name, action, and data
        # TODO: Write to log file and print to console
        pass
    
    def handle_url_scheme(self, url):
        """
        Process incoming URL scheme requests.
        
        Args:
            url: The URL scheme to process
            
        Returns:
            Boolean indicating success
        """
        # TODO: Parse the URL using urllib.parse.urlparse()
        # TODO: Extract scheme, path, and query parameters
        # TODO: Route to appropriate handler based on path
        # TODO: Return True if successful, False otherwise
        pass
    
    def handle_login(self, params):
        """
        Handle login requests (VULNERABLE - logs credentials).
        
        Args:
            params: Dictionary of query parameters
        """
        # TODO: Extract 'user' and 'pass' from params
        # TODO: Log the login attempt with credentials (vulnerability!)
        # TODO: Simulate authentication check
        pass
    
    def handle_transfer(self, params):
        """
        Handle money transfer requests (VULNERABLE - no auth check).
        
        Args:
            params: Dictionary with amount, to, from parameters
        """
        # TODO: Extract amount, to_account, from_account
        # TODO: Log transfer initiation
        # TODO: Process transfer without authentication (vulnerability!)
        pass
    
    def handle_admin(self, params):
        """
        Handle admin commands (EXTREMELY VULNERABLE).
        
        Args:
            params: Dictionary with cmd parameter
        """
        # TODO: Extract command from params
        # TODO: Log and execute command (vulnerability!)
        pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 vulnerable_app.py 'url_scheme'")
        sys.exit(1)
    
    # TODO: Create VulnerableApp instance
    # TODO: Process the URL scheme from sys.argv[1]
    # TODO: Handle any errors appropriately

if __name__ == "__main__":
    main()

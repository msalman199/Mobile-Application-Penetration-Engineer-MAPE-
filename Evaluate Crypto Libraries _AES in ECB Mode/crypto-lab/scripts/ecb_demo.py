#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class ECBVulnerabilityDemo:
    def __init__(self, key):
        """
        Initialize with encryption key.
        
        Args:
            key: 16-byte encryption key
        """
        self.key = key
    
    def encrypt_ecb(self, plaintext):
        """
        Encrypt plaintext using AES-ECB mode.
        
        Args:
            plaintext: String to encrypt
        
        Returns:
            Base64-encoded ciphertext
        """
        # TODO: Create AES cipher in ECB mode
        # TODO: Pad plaintext to block size (16 bytes)
        # TODO: Encrypt padded plaintext
        # TODO: Return base64-encoded result
        pass
    
    def decrypt_ecb(self, ciphertext):
        """
        Decrypt ciphertext using AES-ECB mode.
        
        Args:
            ciphertext: Base64-encoded encrypted data
        
        Returns:
            Decrypted plaintext string
        """
        # TODO: Decode base64 ciphertext
        # TODO: Create AES cipher in ECB mode
        # TODO: Decrypt and unpad
        # TODO: Return plaintext
        pass
    
    def demonstrate_pattern_weakness(self):
        """
        Show how ECB preserves patterns in plaintext.
        """
        test_cases = [
            "REPEATEDBLOCK___REPEATEDBLOCK___",  # Identical blocks
            "AAAAAAAAAAAAAAAA" * 2,              # Same characters
            "1234567890123456" * 2,              # Repeated numbers
        ]
        
        print("ECB MODE PATTERN VULNERABILITY")
        print("=" * 50)
        
        for plaintext in test_cases:
            # TODO: Encrypt the plaintext
            # TODO: Split ciphertext into 16-byte blocks
            # TODO: Display each block in hexadecimal
            # TODO: Identify and highlight identical blocks
            # TODO: Explain the security implication
            pass
    
    def compare_with_cbc(self, plaintext):
        """
        Compare ECB with CBC mode encryption.
        
        Args:
            plaintext: Test data to encrypt
        """
        # TODO: Encrypt same plaintext with ECB
        # TODO: Encrypt same plaintext with CBC (use random IV)
        # TODO: Display both ciphertexts
        # TODO: Show that CBC produces different output each time
        # TODO: Explain why CBC is more secure
        pass

def main():
    key = b'MySecretKey12345'  # 16 bytes
    demo = ECBVulnerabilityDemo(key)
    
    # TODO: Run pattern weakness demonstration
    # TODO: Run ECB vs CBC comparison
    # TODO: Print security recommendations
    pass

if __name__ == "__main__":
    main()

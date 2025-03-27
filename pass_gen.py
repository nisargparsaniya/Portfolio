import random  

def generate_password(length, use_digits=True, use_special_chars=True):    
 
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    digits = "0123456789" if use_digits else ""  
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/" if use_special_chars else ""  
  
    all_chars = letters + digits + special_chars  

    if not all_chars:  
        return "Error: No character set selected!"  

    return "".join(random.choices(all_chars, k=length))  

length = int(input("Enter password length: "))  
use_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"  
use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"  

print(f"Generated Password: {generate_password(length, use_digits, use_special_chars)}")  

#!/usr/bin/env python3
"""
Password Strength Checker
Checks password complexity
"""

import re

def check_password_strength(password):
    """Evaluate password strength"""
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters")
    
    if len(password) >= 12:
        score += 1
    
    # Complexity checks
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")
    
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add numbers")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add special characters")
    
    # Determine strength
    if score <= 2:
        strength = "WEAK 🔴"
    elif score <= 4:
        strength = "MODERATE 🟡"
    else:
        strength = "STRONG 🟢"
    
    return strength, feedback

def main():
    print("=== Password Strength Checker ===\n")
    password = input("Enter password to check: ")
    
    strength, feedback = check_password_strength(password)
    
    print(f"\nPassword Strength: {strength}")
    print(f"Score: {len(feedback)}/6\n")
    
    if feedback:
        print("Recommendations:")
        for item in feedback:
            print(f"  {item}")
    else:
        print(":) Excellent password!")

if __name__ == "__main__":
    main()

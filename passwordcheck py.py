

def check_password_strength(password):
    """
    Checks the strength of a password based on multiple criteria.
    Returns a score and feedback.
    """
    score = 0
    feedback = []
    
    # Check length
    length = len(password)
    if length >= 12:
        score += 3
        feedback.append("✓ Good length (12+ characters)")
    elif length >= 8:
        score += 2
        feedback.append("✓ Acceptable length (8+ characters)")
    else:
        score += 0
        feedback.append("✗ Too short (minimum 8 characters recommended)")
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters")
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters")
    
    # Check for numbers
    if re.search(r"\d", password):
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters")
    
    # Check for common patterns (security check)
    common_passwords = ["password", "123456", "qwerty", "abc123", "letmein"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("✗ This is a commonly used password - VERY WEAK!")
    
    # Determine strength level
    if score >= 7:
        strength = "STRONG"
        color = "🟢"
    elif score >= 5:
        strength = "MODERATE"
        color = "🟡"
    else:
        strength = "WEAK"
        color = "🔴"
    
    return score, strength, color, feedback


def main():
    print("=" * 50)
    print("     PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    print("\nThis tool helps you check if your password is strong.")
    print("A strong password should:")
    print("  - Be at least 12 characters long")
    print("  - Include uppercase and lowercase letters")
    print("  - Include numbers")
    print("  - Include special characters (!@#$%^&*)")
    print("\n" + "=" * 50)
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\nThank you for using Password Strength Checker!")
            break
        
        if not password:
            print("Please enter a password.")
            continue
        
        # Check the password
        score, strength, color, feedback = check_password_strength(password)
        
        # Display results
        print("\n" + "-" * 50)
        print(f"Password Strength: {color} {strength}")
        print(f"Score: {score}/8")
        print("-" * 50)
        print("\nFeedback:")
        for item in feedback:
            print(f"  {item}")
        print("-" * 50)
        
        # Give recommendations
        if strength == "WEAK":
            print("\n⚠️  WARNING: This password is weak and easy to crack!")
            print("Recommendation: Create a longer password with mixed characters.")
        elif strength == "MODERATE":
            print("\n💡 Your password is okay, but could be stronger.")
            print("Recommendation: Add more length and special characters.")
        else:
            print("\n✅ Excellent! This is a strong password.")


if __name__ == "__main__":
    main()

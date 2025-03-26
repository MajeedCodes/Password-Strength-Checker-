def check_password_strength(password):

    score = 0
    feedback = []
    

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
   
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number")
    

    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*)")
    

    if score == 5:
        strength = "Strong"
        message = "Excellent! Your password meets all security requirements."
    elif score >= 3:
        strength = "Moderate"
        message = "Good password, but it could be stronger."
    else:
        strength = "Weak"
        message = "Password needs improvement."
    
    return score, strength, message, feedback

def main():
    print("🔐 Password Strength Meter")
    print("Enter a password to check its strength")
    print("Requirements: 8+ chars, upper/lowercase, numbers, special chars (!@#$%^&*)")
    print("-" * 50)
    
    while True:
        password = input("\nEnter password (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
            
        score, strength, message, feedback = check_password_strength(password)
        
       
        print(f"\nPassword Strength: {strength}")
        print(f"Score: {score}/5")
        print(f"Message: {message}")
        
      
        if strength != "Strong" and feedback:
            print("Suggestions for improvement:")
            for suggestion in feedback:
                print(f"- {suggestion}")

if __name__ == "__main__":
    main()
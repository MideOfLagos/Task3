def password_strength(password):
    score = 0

    if len(password) >= 8:  # Removed the quotes around 'if'
        score += 1
        
    if any(char.isupper() for char in password):
        score += 1
        
    if any(char.islower() for char in password):  # Fixed indentation
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    feedback = ""

    if score == 0:
        feedback = "Very Weak"
    elif score == 1:
        feedback = "Weak"
    elif score == 2:
        feedback = "Medium"
    elif score == 3:
        feedback = "Strong"
    elif score == 4:
        feedback = "Very Strong"

    return feedback

# Test the function with a password
password = "Iamsamuel404."
strength = password_strength(password)
print("Password Strength:", strength)

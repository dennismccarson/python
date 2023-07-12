import re
import getpass

# Simulate a database of known compromised passwords
compromised_passwords = ["password123", "12345678", "qwerty123"]

def test_password_strength(password):
    feedback = []

    # Check the password length
    if len(password) < 12:
        feedback.append("Password too short. It should be at least 12 characters long.")

    # Check for presence of both upper and lower case letters
    if not (any(char.islower() for char in password) and any(char.isupper() for char in password)):
        feedback.append("Password should have both upper and lower case characters.")

    # Check for digits
    if not any(char.isdigit() for char in password):
        feedback.append("Password should have at least one numeral.")
    
    # Check for non-consecutive numbers
    numbers = [char for char in password if char.isdigit()]
    if numbers:
        if all(abs(int(numbers[i]) - int(numbers[i+1])) == 1 for i in range(len(numbers) - 1)):
            feedback.append("Password should not have consecutive numbers.")

    # Check for non-repetitive characters
    if any(password.count(char) > 2 for char in set(password)):
        feedback.append("Password should not have the same character repeated more than twice consecutively.")

    # Check for special characters
    if not re.findall('[^A-Za-z0-9]', password):
        feedback.append("Password should have at least one special character.")

    # Check against known compromised passwords
    if password in compromised_passwords:
        feedback.append("This password has been compromised before, please choose a different one.")

    return feedback if feedback else "Password is strong."

# Test the function
password = getpass.getpass("Enter a password: ")
feedback = test_password_strength(password)

if type(feedback) is list:
    for item in feedback:
        print(item)
else:
    print(feedback)

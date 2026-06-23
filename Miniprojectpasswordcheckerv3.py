def length(password):
    return len(password)
def contains_number(password):
    for char in password:
        if char.isdigit():
            return "Yes"
    return "No"
def contains_uppercase(password):
    for char in password:
        if char.isupper():
            return "Yes"
    return "No"
def starts_with_uppercase(password):
        if password[0].isupper():
            return "Yes"
        else:
            return "No"
def contains_lowercase(password):
    for char in password:
        if char.islower():
            return "Yes"
    return "No"
def ends_with_number(password):
    if password[-1].isdigit():
            return "Yes"
    return "No"
def password_strength(password):
    if length(password) >= 8 and contains_number(password) == "Yes" and contains_uppercase(password) == "Yes" and contains_lowercase(password) == "Yes":
        return "Strong" 
    return "Weak"
password = input("Enter your password: ")
print("Password: ", password)
print("Length: ", length(password))
print("Contains number: ", contains_number(password))
print("Contains uppercase: ", contains_uppercase(password))
print("Contains lowercase: ", contains_lowercase(password))
print("Starts with uppercase: ", starts_with_uppercase(password))
print("Ends with number: ", ends_with_number(password))
print("Strength: ", password_strength(password))
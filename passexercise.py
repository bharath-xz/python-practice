def contains_uppercase(password):
    for char in password:
        if char.isupper():
            return "Yes"
        
    return "No"
password = " "
print(contains_uppercase(password))
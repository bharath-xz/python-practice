def password_length(password):
        return len(password)
def starts_with_uppercase(password):
        if password[0].isupper():
            return "Yes"
        else:
              return"No"
def ends_with_number(password):
        if password[-1].isdigit():
            return "Yes"
        else:
              return"No"
def contains_number(password):
    for char in password:
        if char.isdigit():
            return "Yes"
    return "No"
password ="Cyber13tt"
print("Password:", password)
print("Length:", password_length(password))
print("Contains number:", contains_number(password))
print("Starts with uppercase:", starts_with_uppercase(password))
print("Ends with number:", ends_with_number(password))
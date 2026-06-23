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
def count_numbers(password):
    count = 0
    for char in password:
            if char.isdigit():
                  count +=1
    return count
password = input("Enter a password: ")
print("Password:", password)
print("Length:", password_length(password))
print("Contains number:", contains_number(password))
print("Starts with uppercase:", starts_with_uppercase(password))
print("Ends with number:", ends_with_number(password))
print("Number of digits: ", count_numbers(password))
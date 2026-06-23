def get_numbers_in_password(password):
    result = []
    for char in password:
        if char.isdigit():
            result.append(char)
    return result
password = "Cyber123"
result = get_numbers_in_password(password)
print(result)
def get_count_numbers(password):
    count = 0
    for char in password:
        if char.isdigit():
            count += 1
    return count
password = "Cyber123"
print(get_count_numbers(password))

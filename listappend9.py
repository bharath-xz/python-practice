def get_name_first_letters(names):
    result = []
    for name in names:
        result.append(name[0])
    return result
result = get_name_first_letters(["Bharath", "John", "Sara"])
print(result)
def get_first_and_last_letters_of_long_names(names):
    result = []
    for name in names:
        if len(name) > 5:
            result.append(name[0] + name[-1])
    return result
result = get_first_and_last_letters_of_long_names(["John", "Bharath", "Ben", "Alexander", "Sam"])
print(result)
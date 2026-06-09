def get_names_starting_with_s(names):
    result = []
    for name in names:
        if name[0] == "S":
            result.append(name)
    return result
result = get_names_starting_with_s(["Sarah", "Bharath", "Sam", "John", "Steve"])
print(result)
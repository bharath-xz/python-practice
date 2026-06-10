def get_name_lengths(names):
    result = []
    for name in names:
        result.append(len(name))
    return result
result = get_name_lengths(["John", "Bharath", "Sam"])
print(result)
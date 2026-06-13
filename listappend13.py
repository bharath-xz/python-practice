def get_name_lengths_plus_one(names):
    result = []
    for name in names:
        result.append(len(name) + 1)
    return result
result = get_name_lengths_plus_one(["John", "Bharath", "Sam"])
print(result)
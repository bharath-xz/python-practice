def get_lenghts_of_long_names(names):
    result = []
    for name in names:
        if len(name) > 5:
            result.append(len(name))
    return result
result = get_lenghts_of_long_names(["john", "Bharath", "Ben", "Alexander", "Sam"])
print(result)
def get_names_longer_than_5(names):
    result = []
    for name in names:
        if len(name) > 5:
            result.append(name)
    return result
result = get_names_longer_than_5(["John", "Bharath", "Ben", "Alexander", "Sam"])
print(result)
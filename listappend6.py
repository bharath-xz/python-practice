def get_long_names_containing_a(names):
    result = []
    for name in names:
        if "a" in name and len(name) > 5:
            result.append(name)
    return result
result = get_long_names_containing_a(["John", "Sarah", "Benjamin", "Bharath", "Sam"])
print(result)
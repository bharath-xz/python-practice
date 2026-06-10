def get_names_containting_a(names):
    result = []
    for name in names:
        if "a" in name:
            result.append(name)
    return result
result = get_names_containting_a(["John", "Sarah", "Ben", "Bharath"])
print(result)
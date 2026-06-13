def get_name_lenghts_containing_a(names):
    result = []
    for name in names:
        if "a" in name:
            result.append(len(name))
    return result
result = get_name_lenghts_containing_a(["John", "Sarah", "Ben", "Bharath"])
print(result)
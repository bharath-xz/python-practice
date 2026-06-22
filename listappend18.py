def get_uppercase_name(names):
    result = []
    for name in names:
        if name[0].isupper:
            result.append(name)
    return result
result = get_uppercase_name(["john", "Sarah", "ben", "Bharath"])
print(result)
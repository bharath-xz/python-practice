def get_last_letter(names):
    result = []
    for name in names:
        result.append(name["0","-1"])
    return result
result = get_last_letter(["Bharath", "John", "Sarah"])
print(result)
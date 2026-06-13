def get_fist_and_last_letter(names):
    result = []
    for name in names:
       result.append(name[0] + name[-1])
    return result
result = get_fist_and_last_letter(["Bharath", "John", "Sarah"])
print(result)
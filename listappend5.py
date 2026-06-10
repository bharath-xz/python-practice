def get_names_ending_with_h(names):
    result = []
    for name in names:
        if name[-1] == "h":
            result.append(name)
    return result
result = get_names_ending_with_h(["Sarah", "John", "Bharath", "Ben", "Hannah"])
print(result)
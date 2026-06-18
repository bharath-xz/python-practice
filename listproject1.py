def get_longest_name_length(names):
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longest = name
    return len(longest)
result = get_longest_name_length(["John", "Bharath", "Ben", "Alexander", "Sam"])
print(result)
def find_longest_name(names):
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longest = name
    return longest         
result = find_longest_name(["John", "Bharath", "Ben", "Alexander"])
print(result)

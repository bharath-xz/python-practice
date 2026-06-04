def count_names_starting_with_a(names):
    count = 0
    for name in names:
        if name[0] == "A":
            count = count + 1
    return count
result = count_names_starting_with_a(["Arjun", "Bharath", "Alice", "Sarah", "Andrew"])
print(result)    


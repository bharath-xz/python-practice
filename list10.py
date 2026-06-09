def count_names_starting_with_s(names):
    count = 0
    for name in names:
        if name[0] == "S":
            count = count + 1
    return count
result = count_names_starting_with_s(["Sarah", "Bharath", "Sam", "John", "Steve"])
print(result)

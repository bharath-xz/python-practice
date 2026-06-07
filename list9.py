def count_names_ending_with_h(names):
    count = 0
    for name in names:
        if name[len(name) - 1] == "h":
            count = count + 1 
    return count
result = count_names_ending_with_h(["Sarah", "John", "Bharath", "Ben", "Hannah", "mh"])
print(result)
def count_long_names(names):
    count = 0
    for name in names:
        if len(name) > 5:
            count +=1
    return count
result = count_long_names(["John", "Bharath", "Ben", "Alexander", "Sam"])
print(result)
def count_names_containing_a(names):
    count = 0
    for name in names:
        if "a" in name:
            count = count + 1
    return count
result = count_names_containing_a(["John","aaron", "Sarah", "Ben", "Bharath"])
print(result)    
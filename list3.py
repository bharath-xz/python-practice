def count_names_starting_with_b(names):
    count=0
    for name in names:
        if name[0] == "B":
           count = count + 1
    return count
result = count_names_starting_with_b(["Bharath", "John","Ben", "Sarah", "Bob"])    
print(result)   
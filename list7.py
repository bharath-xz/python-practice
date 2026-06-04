def find_shortest_name(names):
    shortest = names[0]
    for name in names:
        if len(shortest) > len(name):
            shortest = name
    return shortest
result = find_shortest_name(["Bharath", "John", "Ben", "Alexander"])
print(result)        

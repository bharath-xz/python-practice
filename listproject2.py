def get_shortest_name_length(names):
    shortest = names[0]
    for name in names:
        if len(shortest) > len(name):
            shortest = name
    return len(shortest)
result = get_shortest_name_length(["John", "Bharath", "Ben", "Alexander", "Sam"])
print(result)
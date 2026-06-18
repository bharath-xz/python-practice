def count_names(names):
    count = 0
    for name in names:
        count += 1
    return count
def find_longest_name(names):
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longest = name
    return longest
def find_shortest_names(names):
    shortest = names[0]
    for name in names:
        if len(name) < len(shortest):
            shortest = name
    return shortest
def get_long_names(names):
    result = []
    for name in names:
        if len(name) > 5:
            result.append(name)
    return result
names = ["John", "Bharath", "Ben", "Alexander", "Sam"]
longest = find_longest_name(names)
shortest = find_shortest_names(names)
print("Total names:", count_names(names))
print("Longest name:", longest)
print("Shortest name:", shortest)
print("Longest name length:", len(longest))
print("Shortest name length:", len(shortest))
print("Long names:", get_long_names(names))

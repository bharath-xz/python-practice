def count_names_longer_than_5(names):
    count = 0
    for name in names:
      if len(name) > 5:
        count = count + 1
    return count
result = count_names_longer_than_5(["Bharath", "John", "Benjamin", "Sarah"])
print(result)
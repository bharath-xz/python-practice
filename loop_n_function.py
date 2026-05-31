def even_or_odd(n):
    return "Even" if n % 2 == 0 else "odd"
print(even_or_odd(25))
for i in range(1,11):
    print(i, even_or_odd(i))

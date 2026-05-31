def sum_to_n(n):
    total = 0
    for i in range(1,n+1):
        total =total + i
        print("i: ", i , "total: ", total)
    return total
print(sum_to_n(5))


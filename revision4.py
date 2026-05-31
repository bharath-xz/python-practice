def count_divisible_by_3_numbers(n):
    count = 0
    for i in range(1,n +1):
        if i % 3 == 0 and i % 5 ==0:
            count = count + 1
    return count        
result = count_divisible_by_3_numbers(50)
print(result)   
def find_Smallest(numbers):
    Smallest = numbers[0]
    for num in numbers:
        if num < Smallest:
           Smallest = num
    return Smallest    
result = find_Smallest([5, 2, 9, 1, 7])
print(result)
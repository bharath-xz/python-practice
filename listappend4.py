def get_odd_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 1:
            result.append(num)
    return result
result = get_odd_numbers([3, 8, 10, 7, 12, 5])
print(result)
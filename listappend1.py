def get_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 ==0:
            result.append(num)
    return result
result = get_even_numbers([3, 8, 10, 7, 12])
print(result)
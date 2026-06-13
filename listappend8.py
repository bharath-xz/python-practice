def get_even_numbers_greater_than_10(numbers):
    result = []
    for num in numbers:
        if num > 10 and num % 2 == 0:
            result.append(num)
    return result
result = get_even_numbers_greater_than_10([3, 8, 12, 15, 20, 7])
print(result)
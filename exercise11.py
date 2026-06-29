def is_even(numbers):
    return numbers % 2 == 0
def get_even_numbers(numbers):
    result = []
    for num in numbers:
        if is_even(num):
            result.append(num)
    return result
result = get_even_numbers([3, 8, 10, 7, 12])
print(result)
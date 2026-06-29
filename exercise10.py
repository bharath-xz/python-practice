def is_even(numbers):
    return numbers % 2 == 0
def count_even_numbers(numbers):
    count = 0
    for num in numbers:
     if is_even(num):
            count += 1
    return count
numbers = [3, 8, 10, 7, 12]
print(count_even_numbers(numbers))
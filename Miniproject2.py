def count_numbers(numbers):
    count = 0
    for num in numbers:
        count += 1
    return count
def largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
def smallest_number(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
def get_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
def get_odd_numbers(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 1:
            answer.append(num)
    return answer
def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [3, 8, 10, 7, 12]
largest = largest_number(numbers)
smallest = smallest_number(numbers)
result = get_even_numbers(numbers)
answer = get_odd_numbers(numbers)
print("Total numbers:",count_numbers(numbers))
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Even numbers:", result)
print("Odd numbers:", answer)
print("Sum:", sum_of_numbers(numbers))
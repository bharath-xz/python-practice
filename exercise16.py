def square(number):
    return number*number
def is_even(number):
    return number % 2 == 0
def get_even_squares(numbers):
    result = []
    for num in numbers:
        if is_even(num):
            result.append(square(num))
    return result
print(get_even_squares([2,3,4,5]))
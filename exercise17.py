def cube(number):
    return number*number*number
def is_even(number):
    return number % 2 == 0
def get_even_cubes(numbers):
    result = []
    for num in numbers:
        if is_even(num):
            result.append(cube(num))
    return result
print(get_even_cubes([2, 3, 4, 5]))
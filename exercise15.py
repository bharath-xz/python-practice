def is_positive(number):
    return number > 0
def get_positive_number(numbers):
    result = []
    for num in numbers:
        if is_positive(num):
            result.append(num)
    return result
print(get_positive_number([-3,5,0,7,-1,10]))
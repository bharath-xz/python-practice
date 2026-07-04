def is_positive(number):
   return number > 0
def count_positive_numbers(number):
    count = 0
    for num in number:
     if is_positive(num):
        count += 1
    return count
print(count_positive_numbers([-3, 5, 0, 7, -1, 10]))
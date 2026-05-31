def describe_number(number):
    #parity
    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    # divisibility
    if number % 3 == 0 and number % 5 ==0:
        return f"{parity} divisible by 3 and 5"
    elif number %3 == 0:
        return f"{parity} and divisible by 3"
    elif number % 5 == 0:
        return f"{parity} and divisible by 5"
    else:
        return f"{parity}"
    
result=describe_number(1)
print(result)

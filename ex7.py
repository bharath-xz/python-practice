max_number =int(input("Hello, enter your number ").strip())
for number in range(1,max_number +1):
    if number %2 == 0 and number %3 ==0:
        print(f"{number} - EvenTriple")
    elif number %2 ==0:
        print(f"{number} - Even")   
    elif number %3 ==0:
        print(f"{number} - Triple")
    else:
        print(f"{number} - odd")            
name = input("What is your name? ").strip()
print("Hello", name)
answer =int(input("Enter the number ").strip())
if answer ==0:
    print(f"{name}, your number is just zero which is neither odd or even")
else:
    if answer >0:
        sign = "Positive"
    else:
        sign= "negative"

    if answer % 2 == 0:
        parity = "even"
    else:
        parity = "odd" 
    print(f"{name}, your number is {sign} and {parity}")

    if answer %3==0 and answer %5==0:
        print("your number is also divisible by 3 and 5")             
     
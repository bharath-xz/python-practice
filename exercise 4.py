name = input("What is your name? ").strip() 
print("Hi", name)
answer = int(input("Enter the number: ").strip())
if answer ==0:
    print(f"{name}, it is just zero, which is neither odd nor even!")
elif answer >0:
    if answer % 2 ==0 :
        print(f"{name}, your number is positive and even")
        if answer %3 ==0:
            print(f"{name}, your number is positive, even and divisible by 3")
    else :
        print(f"{name}, your number is positive, odd")
        if answer %3 ==0:
            print(f"{name}, your number is positive, odd and divisible by 3")

else:
    if answer %2 ==0 :
       print(f"{name}, your number is negative and even")
       if answer %3 ==0:
           print(f"{name}your number is negative, even and divisible by 3")
    else:
       print(f"{name}, your number is negative and odd")
       if answer %3 ==0:
           print(f"{name}, your number is negative, odd and divisible by 3")
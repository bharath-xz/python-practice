name =input("what is your name? ")
print("Hi", name)
answer = int(input("enter the number: ").strip())
if answer == 0:
    print(f"{name}, 0 is neither even nor odd") #put =0 before %2
elif answer %2 == 0:
    print(f"{name}, your number is even")
else :
    print(f"{name}, your number is odd")
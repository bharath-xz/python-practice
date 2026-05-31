answer = int(input("Enter your marks").strip())
if answer < 0 or answer > 100:
    print("invalid, please enter number between 0 and 100")
elif answer >=90 :
    print("HD")
elif answer >=80 :
    print("D")
elif answer >=70  :
    print("credit")
elif answer >=60:
    print("Pass")    
else:
    print("fail")
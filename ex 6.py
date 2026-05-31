answer = int(input("Hello, enter the number ").strip())
if answer %3 ==0 and answer %5 ==0:
   print("FizzuBzz")   
elif answer %3 ==0 :
   print("Fizz")
elif answer %5 ==0:
   print("Buzz")   
else:
   print(answer)   

print("Welcome to the Quiz")
answer = 0
while answer != 8:
    answer = int(input("What is 5 + 3?"))
    if answer == 8:
       print("Correct!")
    else:
       print("Incorrect!")
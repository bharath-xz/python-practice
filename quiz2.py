print("Welcome to the Quiz!")
answer1 = int(input("What is 5 + 3?"))
score = 0
if answer1 == 8:
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
answer2 = int(input("What is 10 - 4?"))
if answer2 == 6:
    score +=1
    print("Correct!")
else:
    print("Incorrect!")
print("Final score : ", score, "/2")

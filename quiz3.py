def ask_question(question, correct_answer):
    answer = int(input(question))
    if answer == correct_answer:
         print("Correct")
         return 1
    else:
        print("Incorrect")
        return 0
score = 0
score += ask_question("What is 5 + 3?", 8)
score += ask_question("What is 10-4?", 6)
print("Final score: ",score,  "/2")
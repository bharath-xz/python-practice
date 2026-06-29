print("Welcome to number guessing game")
secret_number = 7
guess = 0
count = 0
while guess != secret_number:
    count += 1
    guess = int(input("Guess the number: "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
print("Correct! You guessed it")
print("You guessed it in", count, "attempts")
import random

isRunning = True


while isRunning:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = None

    if difficulty == "easy":
        attempts = 10
        
    elif difficulty == "hard":
        attempts = 5

    print("\n\n")
    print(f"You have {attempts} attempts remaining to guess the number.")
    
    ChosenNumber = random.randint(1,100)

    while attempts != 0:

        guess = int(input("Make a guess: "))
        attempts = attempts - 1
    
        if guess == ChosenNumber:
            print("Congratulations you win!")
            break
        
        elif guess < ChosenNumber:
            print("Too low.")
        
        elif guess > ChosenNumber:
            print("Too high.")

            
        print(f"Guess again.\n\nYou have {attempts} remaining to guess the number.")

    replay = input("Would you like to play again? Type either 'Y' or 'N': ").lower()
    
    if replay != "y":
        isRunning = False
    else:
        for i in range(1,100):
            print("\n")

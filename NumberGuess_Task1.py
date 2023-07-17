import random

name = input("Please enter your name: ")

play_again = True

while play_again:
    number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        print("Attempts left:", attempts)

    if attempts == 0:
        print("Game over! You ran out of attempts. The number was:", number)

    play_again_input = input("Do you want to play again? (yes/no): ")
    if play_again_input.lower() != "yes":
        play_again = False

print("Thank you for playing the Number Guessing Game!")
import random

play_again = True

while play_again:
    number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        print("Attempts left:", attempts)

    if attempts == 0:
        print("Game over! You ran out of attempts. The number was:", number)

    play_again_input = input("Do you want to play again? (yes/no): ")
    if play_again_input.lower() != "yes":
        play_again = False

print("Thank you for playing the Number Guessing Game!")

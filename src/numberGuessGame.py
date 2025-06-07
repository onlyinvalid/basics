import random

while True:
    number = random.randrange(0,100)
    guess = float(input("Guess a number: "))

    while guess != number:

        if guess > number:
            print("\nGo lower")
        else:
            print("\ngo higher")

        guess = float(input("\nGuess again: "))

    again = input("want to play again? (y/n)")
    if again != "y":
        break

      



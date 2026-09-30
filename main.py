import random

secret = random.randint(1, 100)
guesses = 0

while True:

    guess = int(input("Guess the Number: "))
    guesses += 1

    if guess < secret:
        print("guess is too low... guess higher!")

    elif guess > secret:
        print("guess is too high...guess lower!")

    else:
        print("Correct!")
        print(f"You took {guesses} guesses.")
        break

       

    


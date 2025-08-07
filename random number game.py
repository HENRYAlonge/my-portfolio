#Random number game
import random
secret_number = random.randint(1,100)
guess_count = 0
max_guess_count = 10
is_correct = False
while not is_correct:
    if guess_count >= max_guess_count:
        print("Game over")
        print("Would you like to play again")
        break

    guess = int(input("input a random number between 1 and 100:"))
    guess_count += 1
    if guess == secret_number:
        is_correct = True
        print("Congratulations you guessed correctly")

    elif guess < secret_number:
        print("Too low try again")

    elif guess > secret_number:
        print("Too high try again")


import random

def guessing_game():
    rand_num = random.randint(0, 100)
    while True:
        guess = int(input("Guess the number between 0-100: "))
        if guess > rand_num:
            print("Too high")
        elif guess < rand_num:
            print("Too low")
        else:
            print("Congrats you did it!")
            break

guessing_game()
import random

def guessing_game():
    rand_num = random.randint(0, 100)
    won = False
    for _ in range(3):
        guess = int(input("Guess the number between 0-100: "))
        if guess > rand_num:
            print("Too high")
        elif guess < rand_num:
            print("Too low")
        else:
            print("Congrats you did it!")
            won = True
            break
        
    if not won:
        print(f"The number was {rand_num}, Game Over")

guessing_game()
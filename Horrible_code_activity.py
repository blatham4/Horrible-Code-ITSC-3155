import random

def give_hint(number, guess):
    if guess > number:
        print("too high")
        # guess was high
    else:
        print("too low")
        # guess was low

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    # ask user for guess
    guess = int(input("Enter a number between 1 and 100: "))
    attempts = attempts + 1

    if guess == number:
        print("You win in", attempts, "attempts")
    else:
        give_hint(number, guess)
        guess = int(input("Enter a number between 1 and 100: "))
        attempts = attempts + 1
        if guess == number:
            print("You win in", attempts, "attempts")
        else:
            give_hint(number, guess)
            guess = int(input("Enter a number between 1 and 100: "))
            attempts = attempts + 1
            if guess == number:
                print("You win in", attempts, "attempts")
            else:
                give_hint(number, guess)
                guess = int(input("Enter a number between 1 and 100: "))
                attempts = attempts + 1
                if guess == number:
                    print("You win in", attempts, "attempts")
                else:
                    give_hint(number, guess)
                    print("You lose")

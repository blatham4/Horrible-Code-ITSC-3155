import random

#Gets the number that the user guesses
def get_guess():
   return int(input("Enter your guess (1-100)"))

#gives the player a hint so they can make a guess
def give_hint(guess, secret_number):
   if guess<secret_number:
       print("Your guess is too low")
   else:
       print("Your guess is too high")



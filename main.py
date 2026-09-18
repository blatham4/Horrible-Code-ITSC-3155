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

#Runs the game and keeps up with attempts and if they get it right
def play_game():
   secret_number = random.randint(1,100)
   attempts= 0

   print("Guess the number between 1 and 100")

   while True:
       guess=get_guess()
       attempts+=1

       if guess==secret_number:
           print(f"You win, you guessed in {attempts} attempts")
           break
       give_hint(guess, secret_number)

#calls the play game method
play_game()

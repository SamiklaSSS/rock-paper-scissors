#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#


ROCK = "1"
SCISSOR = "2"
PAPER = "3"

print("Game")

print("Welcome to Rock, Paper, Scissors!")

print("So, ROCK = 1, Scissor = 2 and Paper = 3, let's play?")
print("Choose and write only one number!")

user_action = input("You choose...")


import random

print("Your oponent has choosed:")

print(random.randint(1, 3))

computer_action = str(random.randint(1, 3))


print(f"\nYou have choosed {user_action}, your oponent has choosed {computer_action}.\n")


if user_action == computer_action:
    print("Draw")


elif user_action == "1":
   if computer_action == "2":
       print("You have won!")
   else:
       print("Your oponent has won")



elif user_action == "2":
   if computer_action == "3":
       print("You have won!")
   else:
       print("Your oponent has won")



elif user_action == "3":
   if computer_action == "1":
       print("You have won!")
   else:
       print("Your oponent has won")

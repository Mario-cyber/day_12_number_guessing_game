import random

# generate global variables 

NUMBERS  = []
COMPUTER_GUESS = 0


#generat numbers: 
for i in range(1,101,1):
    NUMBERS.append(i)

# computer selects a random card 
COMPUTER_GUESS = NUMBERS[random.randint(0,99)]

print(COMPUTER_GUESS)

COMPUTER_GUESS = 60

#welcome interphase 

print(f"Welcome to the number gessing game! \nI'm thinking of a number between 1 and 100")
difficulty = input("Chose a difficulty, type 'e' or 'h: ").lower()

print(difficulty)

#define functions here:

def hard_mode(guess):
    attemps = 5 
    while attemps > 0 :
        user_guess = int(input("enter your guess: "))
        if user_guess == COMPUTER_GUESS:
            print("you win!")
            attemps = 0
        else: 
            attemps = attemps - 1 
            print(f"nope try again \n {attemps} remiaing")


if difficulty == "h": 
   hard_mode(COMPUTER_GUESS)
elif difficulty == "e":
    print("goodbye")

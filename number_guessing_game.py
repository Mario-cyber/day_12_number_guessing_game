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

#welcome interphase 

print(f"Welcome to the number gessing game! \nI'm thinking of a number between 1 and 100")
difficulty = input("Chose a difficulty, type 'e' or 'h: ").lower()

print(difficulty)

if difficulty == "h": 
    print("h")
elif difficulty == "e":
    print("goodbye")
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
difficulty = input("Chose a difficulty, type 'easy' or 'hard: ").lower()

print(difficulty)

#define functions here:

def guess_game():
    if difficulty == "hard":
        attemps = 5
    elif difficulty == "easy":
        attemps = 10 
    while attemps > 0 :
        user_guess = int(input("enter your guess: "))
        if user_guess == COMPUTER_GUESS:
            print("you win!")
            attemps = 0
        else: 
            attemps = attemps - 1 
            if user_guess > COMPUTER_GUESS:
                print("too high")
            else:
                print("too low")
            print(f"you have {attemps} attempts remiaing")


guess_game()


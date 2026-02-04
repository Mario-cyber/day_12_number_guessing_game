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

#set difficulty 
difficulty = input("Chose a difficulty, type 'easy' or 'hard: ").lower()

#define functions here:

def guess_game():

    if difficulty == "hard":
        attemps = 5
    elif difficulty == "easy":
        attemps = 10 
    while attemps > 0 :
        user_guess = int(input("make a guess: "))
        if user_guess == COMPUTER_GUESS:
            print("you win!")
            #this is a little cheeky, but it will do 
            attemps = - 1
        else: 
            attemps = attemps - 1 
            if user_guess > COMPUTER_GUESS:
                print("too high")
            else:
                print("too low")
            print(f"Guess again! \nyou have {attemps} attempts remiaing")
    if attemps == 0:
        print("you lose")

guess_game()


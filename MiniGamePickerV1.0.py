from random import randint
from random import randint
running = True

def RockPaperScissors():
    mode = input("Do you wish to play on Baby or Normal?")
    if mode == "Normal":
        move = input("Rock, Paper, Scissors, SHOOT")
        enemymove = randint(1,3)
        if enemymove == 1:
            print("Enemies move is: Rock")
            if move == "Rock":
                print("It's a tie!")
            elif move == "Paper":
                print("You won!")
            elif move == "Scissors":
                print("You lost!")
        elif enemymove == 2:
            print("Enemies move is: Paper")
            if move == "Rock":
                print("You lost!")
            elif move == "Paper":
                print("It's a tie!")
            elif move == "Scissors":
                print("You won!")
        elif enemymove == 3:
            print("Enemies move is: Scissors")
            if move == "Rock":
                print("You won!")
            elif move == "Paper":
                print("You lost!")
            elif move == "Scissors":
                print("It's a tie!")
    if mode == "Baby":
        move = input("Rock, Paper, Scissors, SHOOT")
        if move == "Rock":
            print("Enemies move is: Scissors")
            print("You won!")
        if move == "Paper":
            print("Enemies move is: Rock")
            print("You won!")
        if move == "Scissors":
            print("Enemies move is: Paper")
            print("You won!")
    
def OneToTen():
    mode = input("Shall I pick the number or shall you?")
    if mode == 'IP':
        number = int(input("Pick a number between 1 and 10"))
        if 1 <= number <= 10:
            enemymove = randint(1,10)
            print("I pick " + str(enemymove))
            if enemymove == number:
                print("I won!")
            else:
                print("You won!")
        else:
            print("You can't pick that number, I win!")
    elif mode == 'EP':
        number = randint(1,10)
        print("I have my number, what do you think it is?")
        move = int(input("Pick the number"))
        if 1 <= move <= 10:
            if move == number:
                print("You won!")
                print("My number was: " + str(number))
            else:
                print("I won!")
                print("My number was: " + str(number))
        else:
            print("You can't pick that number, I win!")
    else:
        print("That is not a gamemode!")

while running:
    gamepick = input("What game do you wish to play?")
    
    if gamepick == "RPS":
        RockPaperScissors()
    elif gamepick == "1to10":
        OneToTen()
    exit()

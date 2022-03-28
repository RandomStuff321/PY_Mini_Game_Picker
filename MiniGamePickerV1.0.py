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

while running:
    gamepick = input("What game do you wish to play?")
    
    if gamepick == "RPS":
        RockPaperScissors()
    exit()
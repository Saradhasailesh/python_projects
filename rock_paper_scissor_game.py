import random

mylist = ["rock", "paper", "scissors"]
#randomly choose any element from the list

def game():

    while True:

        a = random.choice(mylist)

        winning_move = {
            "rock":"scissors",
            "scissors":"paper",
            "paper":"rock"
        }
        #get input from user
        while True:
            b = input("Please enter your move from rock, paper or scissors\n").lower().strip()
            if b not in mylist:
                print("Invalid input. Please enter a move from the options provided.")

            else:
                break
        print("Computer's move:",a)
        print("User's move:",b)

        if a == b:
            print("It is a tie")
        elif winning_move[a] == b:
            print("Computer Won!!!")
        else:
            print("User Won!!!")

        while True:
            #check if user wants to play again
            print("Do you want to play again?(yes/no):\n")
            c = str(input()).lower().strip()
            if c == "yes":
                break#the game if the user says 'yes'
            elif c == "no":
                print("Ok, Bye!")
                return# game if the user says 'no'
            else:
                print("Invalid input. Please enter yes or no.")

# Start the game
game()
                



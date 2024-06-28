import random


user_wins=0
computer_wins=0

options = ["rock","paper","scissors"]

while True:
    useroption = input("Type Rock/Paper/Scissor/Q for quit ")
    if useroption == 'q':
        print("you have won " + str(user_wins))
        print("computer has won " + str(computer_wins))
        quit()
    elif useroption not in options:
        print("Invalid options try again")
        continue
    else:
        number = random.randint(0,2)
        computeroption = options[number]

        if useroption =='rock' and computeroption =='scissors':
            print("You won!!")
            user_wins+=1
        elif useroption == 'scissors' and computeroption == 'paper':
            print("You won!!")
            user_wins+=1
        elif useroption == 'paper' and computeroption =='rock':
            print("You won!!")
            user_wins+=1
        elif useroption =='rock' and computeroption =='rock':
            print("Draw")
            
        elif useroption == 'scissors' and computeroption == 'scissors':
            print("Draw")
            
        elif useroption == 'paper' and computeroption =='paper':
            print("Draw")
        else:
            print("Computer won!!")
            computer_wins+=1



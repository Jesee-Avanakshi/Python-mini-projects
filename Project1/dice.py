import random


def rolldice():
    dice = random.randint(1,6)
    print(dice)
    return dice

def maximumscore(players_num):
    max_scores =[0 for _ in range(players_num)]
    while max(max_scores) <=20:
        for player in range(players_num):
            diceroll = input("Shall we roll dice for player ?(y)")
            if (diceroll.lower() =='y'):
                dicevalue = rolldice()
                max_scores[player] +=dicevalue
            else:
                print("your turn is skipped")
        print(max_scores,"player ")
    
    print("Maximum score is ", max(max_scores), "by player",max_scores.index(max(max_scores))+1)
    

while True:
    players_num = input("Enter how many people want to play? < 2 to 4> and q to quit \n")

    if players_num.lower() == 'q':
        break

    if players_num.isdigit():
        players_num = int(players_num)
        if(2<= players_num <=4):
            maximumscore(players_num)
            
        else:
            print("No.of players should be in between 2 to 4 ")
    else:
        print("Invalid input")
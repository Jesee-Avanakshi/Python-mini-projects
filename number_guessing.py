import random

maximumlimit = input("Enter top range number ")
if maximumlimit.isdigit():
    maximumlimit = int(maximumlimit)
    if maximumlimit<=0:
        print("Enter number greater than 0 next time")
        quit()
else:
    print("Enter number next time")
    quit()


randomnumber = random.randint(0,maximumlimit)
# print(randomnumber)

count =0
while(True):
    count +=1
    guessnumber = input("Enter your guess ")
    if guessnumber.isdigit():
        guessnumber = int(guessnumber)
    else:
        print("Enter number next time")
        quit()

    if guessnumber == randomnumber:
        print("You guessed it in "+ str(count) + " times")
        quit()
    else:
        if guessnumber > randomnumber:
            print("Try again - your guess is above the number ")
        else:
            print("Try again - your guess is lower the number ")


print('Welcome to my Quiz!!')

playing = input("Do you want to play ? YES/NO ")

if playing!='yes':
    quit()

print("Let's play")

score = 0
answer = input("How do you access the first element of a list named myList? ")

if answer == 'myList[0]':
    print('Correct')
    score +=1
else:
    print('Incorrect')

answer = input("Lists are mutable or immutable ")

if answer.lower() == 'mutable':
    print('Correct')
    score +=1
else:
    print('Incorrect')

answer = input("Tuples are mutable or immutable ")

if answer.lower() == 'immutable':
    print('Correct')
    score +=1
else:
    print('Incorrect')

print("your quiz has ended and your score is " + str(score))

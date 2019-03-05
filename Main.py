import random

RandNumList = []

print ("Welcome to MasterMind")

RandNumList.append(random.randint(1,8))

for q in RandNumList:
    print (q)

Guess = input("Pick a number between 1 & 8: ")

if int(Guess) == RandNumList[0]:               #fix later, none int values cause ValueError
    print ("Correct!")
else:
    print ("Sorry that's not correct.")

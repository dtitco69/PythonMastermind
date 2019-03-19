import random

RandNumList = []
GuessList = []

print ("Welcome to MasterMind")

for r in range(2):
    RandNumList.append(random.randint(1,8))

for q in RandNumList:
    print (q)

while GuessList != RandNumList:
    GuessList = []

    for r in range(2):
        TempGuessInput = input("Pick a number between 1 & 8: ")  #fix later, none int values cause ValueError
        GuessList.append(int(TempGuessInput))

    for x in GuessList:
        print (x)
    
    #change output from guesses
    if GuessList[0] == RandNumList[0]:
        print ("Guess 0 is correct!")
    elif GuessList[0] == RandNumList[1]:
        print ("Guess 0 is correct, but not in the right place")
    else:
        print ("Sorry, guess 0 is not correct.")

    if GuessList[1] == RandNumList[0]:
        print ("Guess 1 is correct, but not in the right place")
    elif GuessList[1] == RandNumList[1]:
        print ("Guess 1 is correct!")
    else:
        print ("Sorry, guess 1 is not correct.")
    
print ("thanks for playing")

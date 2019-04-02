import random

RandNumList = []
GuessList = []
GymList = [0,1,2,3]

print ("Welcome to MasterMind")

for r in range(4):
    RandNumList.append(random.randint(1,8))

for q in RandNumList:
    print (q)

while GuessList != RandNumList:
    GuessList = []

    while len(GuessList) != len(RandNumList):
        TempGuessInput = input("Pick a number between 1 & 8: ")
        try:
            GuessList.append(int(TempGuessInput))
        except ValueError:
            print ("Guess not valid")
            continue

##    for x in GuessList:
##        print (x)

#INIT CHECK#
    #change output from guesses
    for x in range(4):
        if GuessList[x] == RandNumList[x]:
            GymList[x] = 'X'
        else:
            GymList[x] = 'O'

#debug
    print (GymList)
#debug end

    for x in range(4):
        if GymList[x] == 'O':
            if GuessList[x] == RandNumList[0] and GymList[0] != 'X':
                print ("Guess "+str(x)+" is correct, but not in the right place")
            elif GuessList[x] == RandNumList[1] and GymList[1] != 'X':
                print ("Guess "+str(x)+" is correct, but not in the right place")
            elif GuessList[x] == RandNumList[2] and GymList[2] != 'X':
                print ("Guess "+str(x)+" is correct, but not in the right place")
            elif GuessList[x] == RandNumList[3] and GymList[3] != 'X':
                print ("Guess "+str(x)+" is correct, but not in the right place")
            else:
                print ("Sorry, guess "+str(x)+" is not correct.")
    
print ("thanks for playing")

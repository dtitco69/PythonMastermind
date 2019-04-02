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

    for x in GuessList:
        print (x)
    
    #change output from guesses
    for x in range(4):
        if GuessList[x] == RandNumList[x]:
            GymList[x] = 'X'
        else:
            GymList[x] = 'O'

#debug
    print (GymList)
#debug end
    
#    if GuessList[0] == RandNumList[0]:
#        print ("Guess 0 is correct!")
    if GymList[0] == 'O':
        if GuessList[0] == RandNumList[1] and GymList[1] != 'X':
            print ("Guess 0 is correct, but not in the right place")
        elif GuessList[0] == RandNumList[2] and GymList[2] != 'X':
            print ("Guess 0 is correct, but not in the right place")
        elif GuessList[0] == RandNumList[3] and GymList[3] != 'X':
            print ("Guess 0 is correct, but not in the right place")
        else:
            print ("Sorry, guess 0 is not correct.")


#    if GuessList[1] == RandNumList[1]:
#        print ("Guess 1 is correct!")
    if GymList[1] == 'O':
        if GuessList[1] == RandNumList[0] and GymList[0] != 'X':
            print ("Guess 1 is correct, but not in the right place")
        elif GuessList[1] == RandNumList[2] and GymList[2] != 'X':
            print ("Guess 1 is correct, but not in the right place")
        elif GuessList[1] == RandNumList[3] and GymList[3] != 'X':
            print ("Guess 1 is correct, but not in the right place")
        else:
            print ("Sorry, guess 1 is not correct.")

#    if GuessList[2] == RandNumList[2]:
#        print ("Guess 2 is correct!")
    if GymList[2] == 'O':
        if GuessList[2] == RandNumList[0] and GymList[0] != 'X':
            print ("Guess 2 is correct, but not in the right place")
        elif GuessList[2] == RandNumList[1] and GymList[1] != 'X':
            print ("Guess 2 is correct, but not in the right place")
        elif GuessList[2] == RandNumList[3] and GymList[3] != 'X':
            print ("Guess 2 is correct, but not in the right place")
        else:
            print ("Sorry, guess 2 is not correct.")    


#    if GuessList[3] == RandNumList[3]:
#        print ("Guess 3 is correct!")
    if GymList[3] == 'O':
        if GuessList[3] == RandNumList[0] and GymList[0] != 'X':
            print ("Guess 3 is correct, but not in the right place")
        elif GuessList[3] == RandNumList[1] and GymList[1] != 'X':
            print ("Guess 3 is correct, but not in the right place")
        elif GuessList[3] == RandNumList[2] and GymList[2] != 'X':
            print ("Guess 3 is correct, but not in the right place")
        else:
            print ("Sorry, guess 3 is not correct.")
    
print ("thanks for playing")

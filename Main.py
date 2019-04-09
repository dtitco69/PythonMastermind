import random

RandNumList = []
GuessList = []
GymList = [0,1,2,3]

print ("Welcome to MasterMind")

for r in range(4):
    RandNumList.append(random.randint(1,8))

##for q in RandNumList:
##    print (q)

while GuessList != RandNumList:
    GuessList = []

    while len(GuessList) != len(RandNumList):
        TempGuessInput = input("Pick four numbers between 1 & 8: ")
        GuessList = list(TempGuessInput)
        try:
           for i in range(4):
               GuessList[i] = int(GuessList[i])
        except ValueError:
            print ("Please enter 4 numbers between 1 & 8 without spaces or punctuation")
            continue
        except IndexError:
            print ("Please enter FOUR numbers between 1 & 8 without spaces or punctuation")
            continue
        
##    for x in GuessList:
##        print (x)

#INIT CHECK#
    #change output from guesses
    for x in range(4):
        if GuessList[x] == RandNumList[x]:
            GymList[x] = 'X'
        else:
            GymList[x] = '-'

    for x in range(4):
        if GymList[x] == '-':
            if GuessList[x] == RandNumList[0] and GymList[0] != 'X':
                GymList[x] = 'O'
#                print ("Guess "+str(x)+" is correct, but not in the right place")
            elif GuessList[x] == RandNumList[1] and GymList[1] != 'X':
                GymList[x] = 'O'
#                print ("Guess "+str(x)+" is correct, but not in the right place")
            elif GuessList[x] == RandNumList[2] and GymList[2] != 'X':
                GymList[x] = 'O'
#                print ("Guess "+str(x)+" is correct, but not in the right place")
            elif GuessList[x] == RandNumList[3] and GymList[3] != 'X':
                GymList[x] = 'O'
#                print ("Guess "+str(x)+" is correct, but not in the right place")
            else:
#                print ("Sorry, guess "+str(x)+" is not correct.")
                pass
            
#debug
    GymList.sort(reverse=True)
    print (GymList)
#debug end

print ("thanks for playing")

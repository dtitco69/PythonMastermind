import random

RandNumList = []
GuessList = []
GymList = [0,1,2,3]
AllowedNums = [1,2,3,4,5,6,7,8]
AnswerCheck = 0

print ("Welcome to MasterMind")

for r in range(4):
    RandNumList.append(random.randint(1,8))

##for q in RandNumList:
##    print (q)

while GuessList != RandNumList:
    GuessList = []
    AnswerCheck = 0
    
    while len(GuessList) != len(RandNumList) or AnswerCheck != 4:
        TempGuessInput = input("Pick four numbers between 1 & 8: ")
        GuessList = list(TempGuessInput)
        try:
           for i in range(4):
               GuessList[i] = int(GuessList[i])
        except ValueError:
            print ("Your answer must not contain letters or punctuation")
            continue
        except IndexError:
            print ("Your answer is less than four numbers")
            continue
        if len(GuessList) > 4:
            print ("Your answer is more than four numbers")
        for i in range(4):
            for j in range(8):
                if GuessList[i] == AllowedNums[j]:
                    AnswerCheck = AnswerCheck+1
                    
#INIT CHECK#
    for x in range(4):
        if GuessList[x] == RandNumList[x]:
            GymList[x] = 'X'
        else:
            GymList[x] = '-'

    for x in range(4):
        if GymList[x] == '-':
            if GuessList[x] == RandNumList[0] and GymList[0] != 'X':
                GymList[x] = 'O'
            elif GuessList[x] == RandNumList[1] and GymList[1] != 'X':
                GymList[x] = 'O'
            elif GuessList[x] == RandNumList[2] and GymList[2] != 'X':
                GymList[x] = 'O'
            elif GuessList[x] == RandNumList[3] and GymList[3] != 'X':
                GymList[x] = 'O'
            else:
                pass
        
    GymList.sort(reverse=True)
    print (GymList)

print ("Thanks for playing!")

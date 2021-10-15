class TreasureChest:
    #Private question : STRING
    #Private answer : INTEGER
    #Private points : INTEGER
    def __init__(self,questionpriv,anspriv,pointspriv):
        self.__question = questionpriv
        self.__answer = anspriv
        self.__points = pointspriv
    def getQuestion(self):
        return self.__question
    def checkAnswer(self,anspriv):
        if int(self.__answer) == anspriv:
            return True
        else:
            return False
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points) // 2
        elif attempts == 3 or attempts == 4:
            return int(self.__points) // 4
        else:
            return 0

arrayTreasure = []
def readData():
    filename = "TreasureChestData.txt"
    try:
        with open('TreasureChestData.txt') as f:
            for i in range(int(5)):
                temp = []
                for y in range(3):
                    temp.append(f.readline().strip())
                arrayTreasure.append(TreasureChest(*temp))

    except OSError:
        print('File not found')


readData()
pick = int(input("Choose a treasure chest from 1-5."))
if pick > 0 and pick < 6:
    result = False
    attempts = 0
    while result == False:
        answer = int(input(arrayTreasure[pick-1].getQuestion()))
        result = arrayTreasure[pick-1].checkAnswer(answer)
        attempts +=1
    print(int(arrayTreasure[pick-1].getPoints(attempts)))
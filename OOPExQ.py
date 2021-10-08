class TreasureChest:
    #Private question : STRING
    #Private answer : INTEGER
    #Private points : INTEGER
    def __init__(self,questionpriv,anspriv,pointspriv):
        self.__question = questionpriv
        self.__answer = anspriv
        self.__points = pointspriv
def readData():
    filename = "TreasureChestData.txt"
    try:
        with open('TreasureChestData.txt') as f:
            for i in range(int(5)):
                temp = []
                for y in range(3):
                    temp.append(f.readline().strip())
                print(temp)
    except OSError:
        print('File not found')


    
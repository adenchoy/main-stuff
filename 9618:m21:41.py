class node:
    def __init__(self,datainp,nextnodepoint):
        self.Data = datainp
        self.nextNode = nextnodepoint
linkedlist = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5

def outputNodes(linkedList,Pointer):
    while Pointer != -1:
        print(linkedList[Pointer].Data)
        Pointer = linkedList[Pointer].nextNode
def addNode(linkedList, Pointer, emptyList):
    dataInput = input("Enter data to be added")
    if emptyList <0 or emptyList >9:
        return False
    else:
        newNode = node(int(dataInput),-1)
        linkedList[emptyList] = newNode
        previousPointer = 0
        while Pointer != -1:
            previousPointer = Pointer
            Pointer = linkedList[Pointer].nextNode
        linkedList[previousPointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode
        return True
outputNodes(linkedlist,startPointer)

value = addNode(linkedlist,startPointer,emptyList)
if value == True:
    print("Node was added successfully")
else:
    print("list is full.")

outputNodes(linkedlist,startPointer)
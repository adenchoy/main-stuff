class Node:
    def __init__(self,datainp,leftpointer=None,rightpointer=None):
        self.Data = datainp
        self.leftPoint = leftpointer
        self.rightPoint = rightpointer
    def __repr__(self):
        return self.Data
    
tree = [0,0,0,0,0,0,0,0,0,0,0,0]
NextNode = 0
def CreateTree(NodeData):
    global NextNode 
    NextNode=0
    tree[NextNode]= Node(NodeData)
    NextNode+=1
def AttachLeft(NodeData,ParentNode):
    global NextNode
    tree[NextNode]= Node(NodeData)
    tree[ParentNode].leftPoint = NextNode
    NextNode+=1
def AttachRight(NodeData,ParentNode):
    global NextNode
    tree[NextNode]= Node(NodeData)
    tree[ParentNode].rightPoint = NextNode
    NextNode+=1

startPointer = 0
def printTreeLeft(treeArr,Pointer):
    while Pointer!= None:
        print(treeArr[Pointer].Data)
        Pointer = treeArr[Pointer].leftPoint
CreateTree("Red")
AttachLeft("Blue", 0)
AttachRight("Green", 0)
AttachRight("Black", 2)
AttachLeft("Brown", 2)
AttachLeft("Peach", 3)
AttachLeft("Yellow", 1)
AttachRight("Purple", 1)
AttachLeft("White", 6)
AttachLeft("Pink", 7)
AttachLeft("Grey", 9)
AttachRight("Orange", 9)
printTreeLeft(tree,startPointer)

def counter(tree,Pointer):
    if tree:
        if tree[Pointer].leftPoint == None and tree[Pointer].rightPoint == None:
            print(tree[Pointer].Data)     
        if tree[Pointer].leftPoint:
            counter(tree,tree[Pointer].leftPoint)
        if tree[Pointer].rightPoint:
            counter(tree,tree[Pointer].rightPoint)
print(counter(tree,startPointer))


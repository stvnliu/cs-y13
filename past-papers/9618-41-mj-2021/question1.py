#1a
class node:
    def __init__(self):
        self.data = None # integer type, none for empty value
        self.nextNode = None # integer type, none for empty value
#1b
linkedList = [node() for i in range(10)]
startPointer = 0
emptyList = 5
newData = [1, 5, 6, 7, 2, 0, 0, 56, 0, 0]
newNextNode = [1, 4, 7, -1, 2, 6, 8, 3, 9, -1]
for i in range(len(linkedList)):
    linkedList[i].data = newData[i]
    linkedList[i].nextNode = newNextNode[i]
#1ci
def outputNodes(array: list[node], startPointer: int):
    print(array[startPointer].data)
    nextItemIndex = array[startPointer].nextNode
    while nextItemIndex != -1:
        print(array[nextItemIndex].data)
        nextItemIndex = array[nextItemIndex].nextNode
#1cii
outputNodes(linkedList, startPointer)
#1di
def addNode():
    global linkedList
    global startPointer
    global emptyList
    inputData = int(input("New data: "))
    if emptyList == -1:
        return False
    linkedList[emptyList].data = inputData
    nextEmptyList = linkedList[emptyList].nextNode
    linkedList[emptyList].nextNode = startPointer
    startPointer = emptyList
    emptyList = nextEmptyList
    return True
#1dii
success = addNode()
if success == True: 
    print("Successfully added a new node.") 
else:
    print("Failed to add the node, array is full.")
outputNodes(linkedList, startPointer)
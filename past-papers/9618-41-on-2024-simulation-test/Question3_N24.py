# initialise linked list structure 
global LinkedList
# creating empty data and joining pointers
LinkedList = [[-1, i + 1] for i in range(0, 20)]
# set last element to be null pointer
LinkedList[-1][1] = -1
global FirstEmpty
global FirstNode
FirstEmpty = 0
FirstNode = -1

def InsertData():
    global FirstEmpty, FirstNode, LinkedList
    for i in range(5):
        number = int(input("your positive integer number: "))
        while number < 0:
            print("invalid, must be positive!")
            number = int(input("your positive integer number: "))
        if FirstEmpty != -1:
            # the linked list is not full
            NextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = number
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = NextEmpty
        else:
            return

def OutputLinkedList():
    global FirstNode, LinkedList
    # assign initial node location
    next_node = FirstNode
    while next_node != -1:
        # outputs the data at the given position
        print(LinkedList[next_node][0])
        # updates the next following pointer
        next_node = LinkedList[next_node][1]

InsertData()
OutputLinkedList()

def RemoveData(target_data):
    global FirstNode, FirstEmpty, LinkedList
    current_node = FirstNode
    next_node = LinkedList[FirstNode][1]
    if LinkedList[current_node][0] == target_data:
        # the first node needs to be removed
        new_first_node = LinkedList[current_node][1]
        LinkedList[current_node][1] = FirstEmpty
        FirstEmpty = current_node
        FirstNode = new_first_node
        return
    while current_node != -1:
        # checks if the immediately succeeding element is target
        if LinkedList[next_node][0] == target_data:
            if LinkedList[next_node][1] == -1:
                # the target is at the end of the list
                # terminating linked list with null pointer
                LinkedList[current_node][1] = -1
            # put element in empty list
            else:
                # the target is in the middle of the list 
                # skip the removed element
                LinkedList[current_node][1] = LinkedList[next_node][1]
                LinkedList[next_node][1] = FirstEmpty
            FirstEmpty = next_node
            return # returning here because only matching for one occurrence
        current_node = next_node
        next_node = LinkedList[next_node][1]
RemoveData(5)
print("After")
OutputLinkedList()
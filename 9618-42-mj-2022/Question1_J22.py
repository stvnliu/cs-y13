#1a
global StackData
global StackPointer
StackData = [None for i in range(10)] # global variable
StackPointer = 0 # global variable 

#1b
def OutputAllElements():
    for dataItem in StackData:
        print(dataItem)
    print(f"Stack pointer: {StackPointer}")

#1c
def Push(push_item: int):
    if StackPointer == len(StackData):
        return False
    StackData[StackPointer] = push_item
    StackPointer += 1
    return True
# 1 e i
def Pop():
    if StackPointer == 0:
        return -1
    StackPointer -= 1
    item = StackData[StackPointer]
    StackData[StackPointer] = None
    return item

#1d
for i in range(11):
    num = int(input(f"Number {i}: "))
    successful = Push(num)
    if successful:
        print("Successfully pushed the item to the stack.")
    else:
        print("The stack is full.")
print(StackData)

# 1 e ii
Pop()
Pop()
print(StackData)
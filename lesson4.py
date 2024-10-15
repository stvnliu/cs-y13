stack = [None for index in range(0,10)]
basePointer = 0
topPointer = -1
stackFull = 10

def push(item):
    global stack, topPointer
    topPointer += 1
    if topPointer >= stackFull: 
        print("ERROR Cannot insert more.")
        return
    stack[topPointer] = item
    print(stack)
def pop():
    global stack, topPointer
    if topPointer < basePointer:
        print("ERROR List is empty, cannot pop.")
        return
    itemPopped = stack[topPointer]
    print(f"I popped this {itemPopped}")
    stack[topPointer] = None
    topPointer -= 1
    print(stack)
def test():
    push(1)
    push(2)
    push(69)

    pop()
    pop()

    print(stack)

    pop()
    pop()

test()

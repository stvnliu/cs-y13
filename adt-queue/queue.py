queue = [None for index in range(0, 10)]
frontPointer = 0
rearPointer = -1
queueLength = 0
queueFull = 10
def dequeue():
    global queue, queueLength, queueFull, rearPointer
    
def enqueue(item):
    global queue, queueLength, queueFull, rearPointer
    if queueLength < queueFull:
        if rearPointer < len(queue) - 1:
            rearPointer += 1
        else:
            rearPointer = 0
        queueLength += 1
        queue[rearPointer] = item
        print(queue)
        return
    print("ERROR queue length exceeded!")
    return
for i in range(13):
    enqueue(10 * i)

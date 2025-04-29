Queue = [None for i in range(50)]
HeadPointer = -1
TailPointer = 0
def Enqueue(Value: str):
    global TailPointer, HeadPointer, Queue
    if HeadPointer == 49:
        print("Queue is full")
        return
    HeadPointer += 1
    Queue[HeadPointer] = Value
    print(Queue)
def Dequeue() -> str:
    global TailPointer, HeadPointer, Queue
    if TailPointer >= HeadPointer:
        print("The queue is empty")
        return "Empty"
    returnValue = Queue[TailPointer]
    Queue[TailPointer] = None
    TailPointer += 1
    return returnValue

def ReadData(): 
    with open("QueueData.txt", 'r') as queueData: 
        [Enqueue(line.strip()) for line in queueData.readlines()]

class RecordData:
    def __init__(self):
        self.ID = None
        self.Total = None
global Records
Records = [RecordData() for i in range(50)]
global NumberRecords
NumberRecords = 0
def TotalData():
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1
    else:
        for x in range(NumberRecords):
            if Records[X].ID == DataAccessed:
                Records[X].Total = Records[X].Total + 1
                Flag = True
    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1

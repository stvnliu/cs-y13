#2a
class SaleData:
    def __init__(self, sale_quantity, sale_id):
        self.Quantity = sale_quantity
        self.ID = sale_id
#2b
global CircularQueue
CircularQueue = [SaleData(-1, "") for i in range(5)]
global Head, Tail
global NumberOfItems
Head = 0
Tail = 0
NumberOfItems = 0

#2c
def Enqueue(NewRecord):
    global NumberOfItems, Head, Tail, CircularQueue
    if NumberOfItems >= 5:
        return -1
    CircularQueue[Tail] = NewRecord
    NumberOfItems += 1
    if Tail < len(CircularQueue) - 1:
        Tail += 1
    else:
        Tail = 0
    print(f"DEBUG Num={NumberOfItems}, Head={Head}, Tail={Tail}")
    return 1
#2d
def Dequeue():
    global NumberOfItems, Head, Tail, CircularQueue
    if NumberOfItems <= 0:
        return SaleData(-1, "")
    item = CircularQueue[Head]
    NumberOfItems -= 1
    if Head >= len(CircularQueue) - 1:
        Head = 0
    else:
        Head += 1
    print(f"DEBUG Num={NumberOfItems}, Head={Head}, Tail={Tail}")
    return item
#2e
def EnterRecord(sale_id: str, quantity: int):
    successfulness = Enqueue(SaleData(quantity, sale_id))
    if successfulness == 1:
        print("Stored")
    elif successfulness == -1:
        print("Full")
#2fi
IDs = ["ADF", "OOP", "BXW", "XXZ", "HQR", "LLP"]
Quantities = [10, 1, 5, 22, 6, 3]
for i in range(6):
    EnterRecord(IDs[i], Quantities[i])
item = Dequeue()
if item.Quantity == -1: # null item
    print("Error: Circular queue is empty")
else:
    print(f"ID={item.ID}, Quantity={item.Quantity}")
EnterRecord("LLP", 3)
for item in CircularQueue:
    print(f"{item.ID} {item.Quantity}")
# while True:
#     Enqueue(SaleData(int(input("qty: ")), input("id: ")))
#     if not input("c: "):
#         break
# [print(obj) for obj in CircularQueue]

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
    return 1
# while True:
#     Enqueue(SaleData(int(input("qty: ")), input("id: ")))
#     if not input("c: "):
#         break
# [print(obj) for obj in CircularQueue]

#1a
global Animals
Animals = [None for i in range(10)] # String array, initialise to None to imply emptiness
#1b
Animals = [
    "horse",
    "lion",
    "rabbit",
    "mouse",
    "bird",
    "deer",
    "whale",
    "elephant",
    "kangaroo",
    "tiger"
]
#1c
def SortDescending():
    ArrayLength = len(Animals)
    for x in range(0, ArrayLength):
        for y in range(0, ArrayLength - x - 1):
            if Animals[y][0] < Animals[y+1][0]:
                Temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = Temp
#1di
SortDescending()
for i in range(len(Animals)):
    print(Animals[i])
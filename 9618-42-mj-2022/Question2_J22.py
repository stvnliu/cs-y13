# 2 a
import random
ArrayData = []
for i in range(10):
    Row = []
    for j in range(10):
        Row.append(random.randint(1, 100))
    ArrayData.append(Row)

# 2 b i
ArrayLength = 10
for x in range(0, ArrayLength): # range() function excludes ArrayLength, so equiv to 0 -> ArrayLength - 1
    for y in range(0, ArrayLength - 1): # range() function excludes ArrayLength, so equiv to 0 -> ArrayLength - 2
        for z in range(0, ArrayLength - y - 1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                # swapping
                tempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = tempValue

# 2 b ii
def OutputAllElements():
    global ArrayData
    global ArrayLength
    for i in range(0, ArrayLength):
        for j in range(0, ArrayLength):
            print(ArrayData[i][j], end=" ")
        print()
# 2 b iii
OutputAllElements()

# 2 c i

# Bugfix included
# Originally, was "if Upper >= Lower"
# Does not work due to max recursion depth exceeding

def BinarySearch(SearchArray: list, Lower: int, Upper: int, SearchValue: int) -> int:
    if Upper > Lower:
        Mid = (Lower + (Upper - 1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                print(f"Searching: {SearchArray[0][Lower:Mid-1]}")
                input()
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                print(f"Searching: {SearchArray[0][Mid+1:Upper]}")
                input()
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    elif Upper == Lower:
        return -1 if SearchArray[0][Upper] != SearchValue else Upper 
    return -1

# a value dynamically input by user, since ArrayData is randomly generated
# target = int(input("Search for a value in first line of array: ")) 
not_exists = -50 # a value that definitely does not exist in ArrayData

find1 = BinarySearch(ArrayData, 0, 10, ArrayData[0][6])
find2 = BinarySearch(ArrayData, 0, 10, not_exists)
print(find1)
print(find2)
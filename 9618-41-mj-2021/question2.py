#2a
global arrayData
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
#2bi
def linearSearch(searchValue: int):
    for item in arrayData:
        if item == searchValue: 
            return True
    return False
#2bii
valueToSearch = int(input("Your value to search for: "))
found = linearSearch(valueToSearch)
if found:
    print("Value has been found")
else:
    print("Value can't be found")
#2c
def bubbleSort():
    for x in range(0, len(arrayData)):
        for y in range(0, len(arrayData) - x - 1):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1] 
                arrayData[y + 1] = temp
print(arrayData)
bubbleSort()
print(arrayData)
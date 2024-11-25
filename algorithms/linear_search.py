import random
def generate_test_data(length: int, _range: tuple):
    arr = []
    for i in range(length):
        arr.append(random.randint(_range[0], _range[1]))
    return arr
def linsearch(myList: list, valueToFind: int):
    mindex: int = len(myList) - 1
    index: int = 0
    found = False
    while not found and index <= mindex:
        if myList[index] == valueToFind:
            found = True
        index += 1
    if found: print("VALUE FOUND!!!")
    else: print("OH NO ITEM NOT FOUND IN LIST!!")
def main():
    inputFind = int(input("Value to find: "))
    linsearch(generate_test_data(10, (0, 1000)), inputFind)
if __name__ == "__main__":
    main()

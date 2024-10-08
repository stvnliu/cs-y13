import random
def generate_test_data(length: int, _range: tuple):
    arr = []
    for i in range(length):
        arr.append(random.randint(_range[0], _range[1]))
    return arr
def linear_search_while(arr: list, item):
    found: bool = False
    index = 0
    while not found and index < len(arr):
        if (arr[index] == item): 
            found = True
            break
        index += 1
    return (found, index)
def linear_search(arr: list, item):
    index = 0
    for _item in arr:
        if _item == item:
            return (True, index) 
        index += 1
    return False
def main():
    print("Hello world")
    array = generate_test_data(10, (0, 100))
    print(array)
    query = int(input("Your query for item: "))
    found1 = linear_search(array, query)
    found2 = linear_search_while(array, query)
    if found1[0]:
        print("Found by for loop method ", found1[1]) 
    else: print("Not found.")
    if found2[0]:
        print("Found by while loop method ", found2[1])
    else: 
        print("Not found.")
if __name__ == "__main__":
    main()
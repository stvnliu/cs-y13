import random
def generate_test_data(length: int, _range: tuple):
    arr = []
    for i in range(length):
        arr.append(random.randint(_range[0], _range[1]))
    return arr
def binsearch(arr: list, item):
    arr = sorted(arr)
    print(arr)
    ubound, lbound = len(arr) - 1, 0
    found = False
    while not found and lbound <= ubound:
        index = (lbound + ubound) // 2
        if arr[index] == item: 
            found = True
            print("Found here")
            return found
        if arr[index] > item:
            ubound = index - 1
        if arr[index] < item:
            lbound = index + 1
    print("not found")
    return found


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
def test_existsness(samples: int):
    yes = 0
    no = 0
    for i in range(samples):
        query = random.randint(0, 100)
        array = generate_test_data(100, (0, 100))
        found = linear_search(array, query)
        if found:
            yes += 1    
        else:
            no += 1
    print(f"In {samples} samples, {yes} match, {no} don't")
def main():
    narr = sorted(["A", "B", "C", "D", "E"])
    print("Hello world")
    array = generate_test_data(10, (0, 100))
    print(array)
    query = int(input("Your query for item: "))
    qstring = input("String item: ")
    binsearch(narr, query)
    found1 = linear_search(array, query)
    found2 = linear_search_while(array, query)
    if found1[0]:
        print("Found by for loop method ", found1[1]) 
    else: print("Not found.")
    if found2[0]:
        print("Found by while loop method ", found2[1])
    else: 
        print("Not found.")
    test_existsness(100)
if __name__ == "__main__":
    main()
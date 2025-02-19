import random
import string
CHARS = list(string.ascii_lowercase)
print(CHARS)
def generate_test_data(length: int, _range: tuple):
    arr = []
    for i in range(length):
        arr.append(random.randint(_range[0], _range[1]))
    return arr
def bubsort(arr: list):
    for i in range(len(arr)):
        # print(arr)
        changed = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                swp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = swp
                changed = True
        if not changed: return arr 
def testarr_string(length: int):
    arr = []
    for i in range(length):
        string = ""
        for i in range(10):
            string += CHARS[random.randint(0,len(CHARS) - 1)]
        arr.append(string)
    print(arr)
    return arr
def bubsort_reliability(samples: int):
    y = 0
    n = 0
    for _ in range(samples):
        test  = generate_test_data(100, (0, 100))
        if bubsort(test) == sorted(test): y += 1
        else: n += 1
    if y == samples: print(f"{samples} checks passed!")
bubsort_reliability(100)
print(bubsort(testarr_string(10)))
# includes return type definition returning a list of strings
def ReadData() -> list[str]:
    with open("Data.txt", 'r') as file:
        # Uses a Python list syntax to collect all lines, 
        # trim newline character, and assign to new lines variable
        lines = [line.strip('\n') for line in file.readlines()]
        return lines
def FormatArray(string_array: list[str]) -> str:
    # uses the str.join(iterator) built-in function for the str type
    return " ".join(string_array)

data = ReadData()
print(FormatArray(data))

def CompareStrings(first: str, second: str) -> int:
    smallest = len(first) if len(first) < len(second) else len(second)
    for i in range(smallest):
        if first[i] < second[i]:
            return 1
        elif first[i] > second[i]:
            return 2
# type definitions for parameter and return value
# takes a list of strings, returns a list of strings
def Bubble(string_array: list[str]) -> list[str]:
    for i in range(len(string_array)):
        # have moved largest value to the end, shrink sort range by 1 each time
        for j in range(len(string_array) - i - 1):
            result = CompareStrings(string_array[j], string_array[j+1])
            # if the two strings are in the wrong order
            if result == 2:
                swap = string_array[j+1]
                string_array[j+1] = string_array[j]
                string_array[j] = swap
    return string_array
sorted_array = Bubble(data)
print(FormatArray(sorted_array))
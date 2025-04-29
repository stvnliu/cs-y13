global WordArray
global NumberWords
WordArray = []
NumberWords = 0
def ReadWords(filename: str):
    with open(filename, 'r') as file:
        WordArray = [line.strip('\n') for line in file.readlines()]
        NumberWords = len(WordArray) - 1

choice = input("Difficulty: easy; medium; hard? : ")
if choice == "easy":
    ReadWords("Easy.txt")
elif choice == "medium":
    ReadWords("Medium.txt")
elif choice == "hard":
    ReadWords("Hard.txt")

def Play():
    print(f"{WordArray[0]}; number of answers: {NumberWords}")
    while
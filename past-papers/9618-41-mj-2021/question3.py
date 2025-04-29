#3a
class TreasureChest:
    def __init__(self, question: str, answer: int, points: int):
        self.__question = question # String
        self.__answer = answer # Integer
        self.__points = points # Integer
    #3ci
    def getQuestion(self):
        return self.__question
    #3cii
    def checkAnswer(self, user_answer: int):
        if self.__answer == user_answer: 
            return True
        else:
            return False
    #3ciii
    def getPoints(self, numberOfAttempts: int):
        if numberOfAttempts == 1: return self.__points
        if numberOfAttempts == 2: return self.__points // 2
        if numberOfAttempts == 3 or numberOfAttempts == 4: return self.__points // 4
        return 0
#3b
def readData():
    TREASURE_CHEST_DATA_FILENAME = "TreasureChestData.txt"
    try:
        with open(TREASURE_CHEST_DATA_FILENAME, 'r') as file:
            global arrayTreasure
            arrayTreasure = [None for i in range(5)] # array of TreasureChest
            for i in range(5):
                question = file.readline().strip()
                answer = int(file.readline().strip())
                points = int(file.readline().strip())
                arrayTreasure[i] = TreasureChest(question, answer, points)
            file.close()
    except IOError:
        print("Error: the file cannot be found")

#3civ
readData()
questionNumber = int(input("Input a question number (1 to 5): "))
while questionNumber < 1 or questionNumber > 5:
    questionNumber = int(input("Input a question number (1 to 5): "))
print(arrayTreasure[questionNumber - 1].getQuestion())
nAttempts = 1
answerInput = int(input(f"[Attempt {nAttempts}] Your answer: "))
while not arrayTreasure[questionNumber - 1].checkAnswer(answerInput):
    answerInput = int(input(f"[Attempt {nAttempts}] Your answer: "))
    nAttempts += 1
points = arrayTreasure[questionNumber - 1].getPoints(nAttempts)
print(f"You are awarded {points} points")
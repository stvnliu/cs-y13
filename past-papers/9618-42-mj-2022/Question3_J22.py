# 3 a
class Card:
    def __init__(self, number: int, colour: str):
        self.__Number = number # Integer
        self.__Colour = colour # String
    
    # 3 b
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

# 3 c
TEXT_FILE_NAME = "CardValues.txt"
cards = [None for i in range(30)] # type is Card, use NoneType to indicate empty
try:
    with open(TEXT_FILE_NAME, "r") as file:
        i = 0
        j = 0
        text_lines = file.readlines()
        #print(text_lines)
        while i < 30:
            number = int(text_lines[j])
            colour = text_lines[j+1]
            cards[i] = Card(number, colour.strip())
            i += 1
            j += 2
except IOError:
    print("Cannot find file.")
#print(cards)
# 3 d
selected_cards = [False for i in range(30)]
def ChooseCard(array_index: int):
    global cards
    global selected_cards
    if array_index < 1 or array_index > 30:
        print("The card array index is out of range")
        return
    normalized_index = array_index - 1
    if selected_cards[normalized_index] == True: # already selected
        for i in range(len(selected_cards)):
            if not selected_cards[i]: return i + 1
    else:
        return array_index

# 3 e i 
Player1 = [None for i in range(4)] # type in array is Card
for i in range(4):
    selected = int(input("Your selected card index: "))
    Player1[i] = cards[ChooseCard(selected) - 1]
for card in Player1:
    print(f"{card.GetNumber()} {card.GetColour()}")
# .......

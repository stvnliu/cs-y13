def IterativeVowels(Value: str) -> int:
    Total = 0 
    LengthString = len(Value)
    for X in range(LengthString):
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total += 1
        Value = Value[1:]
    return Total
returnValue = IterativeVowels("house")
print(returnValue)
def RecursiveVowels(Value: str) -> int:
    if len(Value) == 0:
        return 0
    current = Value[0]
    if current == 'a' or current == 'e' or current == 'i' or current == 'o' or current == 'u':
        return 1 + RecursiveVowels(Value[1:])
    else:
        return 0 + RecursiveVowels(Value[1:])
print(RecursiveVowels("imagine"))

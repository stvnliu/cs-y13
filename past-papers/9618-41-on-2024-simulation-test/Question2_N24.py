class Horse:
    def __init__(self, Name: str, MaxFenceHeight: int, PercentageSuccess: int):
        self.__Name: str = Name # String type
        self.__MaxFenceHeight: int = MaxFenceHeight # Integer type
        self.__PercentageSuccess: int = PercentageSuccess # Integer type
    def GetName(self):
        return self.__Name
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    def Success(self, fence_height: int, fence_risk: int):
        if fence_height > self.__MaxFenceHeight:
            return 0.2 * self.__PercentageSuccess
        modifier = 0.6 + 0.1 * (5 - fence_risk)
        return modifier * self.__PercentageSuccess
# Python has dynamic sized arrays, here simulates static sizes by assigning None 2 times
Horses = [None for i in range(2)]
Horses[0] = Horse("Beauty", 150, 72)
Horses[1] = Horse("Jet", 160, 65)
for horse in Horses:
    print(horse.GetName())

class Fence:
    def __init__(self, Height: int, Risk: int):
        self.__Height: int = Height # Integer type
        self.__Risk: int = Risk # Integer type
    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk
    

# creates array local to main program scope
# with maximum 4 elements, initialised to None
Course = [None for i in range(4)]

for i in range(4):
    fence_height = int(input(f"Fence {i + 1} height (70 to 180): "))
    while fence_height > 180 or fence_height < 70:
        # invalid height
        print("Height invalid! 70 <= Height <= 180!")
        fence_height = int(input(f"Fence {i + 1} height (70 to 180): "))
    fence_risk = int(input(f"Fence {i + 1} risk (1-5): "))
    while fence_risk > 5 or fence_risk < 1:
        # invalid height
        print("Risk invalid! 1 <= Risk <= 5!")
        fence_height = int(input(f"Fence {i + 1} risk (1 to 5): "))
    new_fence = Fence(fence_height, fence_risk)
    Course[i] = new_fence

# initialising averages tracker array
Averages = [0 for i in range(len(Horses))]
for i in range(len(Horses)):
    total_chance = 0
    for j in range(len(Course)):
        success_chance = Horses[i].Success(Course[j].GetHeight(), Course[j].GetRisk())
        total_chance += success_chance
        display_percentage = round(success_chance)
        message = f"Horse {Horses[i].GetName()} has a {display_percentage}% chance of jumping over fence {j + 1}!"
        print(message)
    average_chance = total_chance / len(Course)
    Averages[i] = average_chance # store raw average chance in tracker array at corresponding index
    display_average = round(average_chance) # pretty-print display average
    print(f"The horse {Horses[i].GetName()} has a {display_average}% chance of successfully jumping over all fences!")

# finding the horse with largest chance of winning
largest_at = 0
for i in range(len(Averages)):
    # if there exists a new largest, replace index with new
    if Averages[i] > Averages[largest_at]:
        largest_at = i
# print output, refer to horse at the largest_at index in Horses array
print(f"The horse {Horses[largest_at].GetName()} has the highest average chance of success!")
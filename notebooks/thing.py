import datetime
import pickle
import random # data generator
class Car:
    def __init__(self, car_id):
        self.VehicleID = car_id
        self.__Registration = ""
        self.__Date = datetime.datetime.now()
        self.__EngineSize = -1
        self.__PurchasePrice = 5900_00
def data_generator():
    cars = []
    for i in range(40):
        s = "ID"
        for i in range(10):
            s += str(random.randint(0, 9))
        cars.append(Car(s))
    return cars
with open("cars.dat", 'wb+') as carfile:
    for car in data_generator():
        print(car.VehicleID)
        pickle.dump(car, carfile)
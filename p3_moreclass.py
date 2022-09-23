import random
import math


class Human:
    def __init__(self, name="Human"):
        self.name = name

class Maniac:
    def __init__(self, maniac="Maniac"):
        self.maniac = maniac
        self.ManiacHere = 0
        self.inCar = False





class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passanger = []
        self.inCar = []
        randommaniac = random.randint(1, 100)
        self.ManiacHere = randommaniac


    def add_passanger(self, human):
        self.passanger.append(human)


    def add_maniac(self, maniac):
        if self.ManiacHere >= 50:
            self.inCar.append(Maniac)
        else:
            self.inCar == []


    def print_maniac(self):
        if self.inCar != []:
            print("sry u unlucky man ;) \nTaxi maniac kill u :)")
        for maniac in self.inCar:
            print(maniac.maniac)
        else:
            print(f"No maniac in {self.brand}")





    def print_passanger(self):
        if self.passanger!=[]:
            print(f"Names of {self.brand} passangers")
        for passanger in self.passanger:
            print(passanger.name)
        else:
             print(f"Oh shit, no passangers in {self.brand} - no money")



Judi = Human("Judi")
person2 = Human("Jackson")
car1 = Auto("Zaporozhets")
car2 = Auto("Porsche")
maniac = Maniac("Maniac")

car1.print_passanger()
car2.print_passanger()

print("Go into car")
car1.add_passanger(Judi)
car1.add_passanger(person2)
car1.add_maniac(maniac)

car1.print_maniac()
car2.print_maniac()


car1.print_passanger()
car2.print_passanger()



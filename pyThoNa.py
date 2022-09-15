import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.alive = True

    def to_chill(self):
        print("Chiiiil")
        self.gladness += random.randint(1, 20)

    def end_of_day(self):
        print(f"gladness = {self.gladness}")

    def life(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = 1
        if live_cube == 1:
            self.to_chill()
        self.end_of_day()

vasya = Student(name="Vasya")
for day in range(365):
    if vasya.alive == False:
        break
    vasya.life(day)

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_work(self):
        print("I wanna work")
        self.money += random.randint(5,50)
        self.gladness -= random.randint(1,5)

    def to_study(self):
        print("Time to study")
        self.progress += 0.17
        self.gladness -= random.randint(1, 5)

    def to_sleep(self):
        print("I will sleep")
        self.gladness += random.randint(1, 7)

    def to_chill(self):
        print("Chiiiil")
        self.money -= random.randint(1,10)
        self.gladness += random.randint(1, 7)
        self.progress -= 0.1


    def problems(self):
        if self.progress <= 0.70:          #study harder
            print("Time to study")
            self.progress += 0.20
            self.gladness -= random.randint(1, 5)

        elif self.money <= 10:
            self.to_work()
        elif self.gladness <= 10:
            random_chill = random.randint(1, 2)
            if random_chill == 1:
                self.to_chill()
            elif random_chill == 2:
                self.to_sleep()

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("depression")
            self.alive = False
        elif self.money <= 0:
            print("have no money")
            self.alive = False
        elif self.progress > 5:
            print("Done")
            self.alive


    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def life(self, day):
        day = "Day" +str(day)+"of"+self.name+"life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()

vasya = Student(name="Vasya")
for day in range(365):
    if vasya.alive == False:
        break
    vasya.life(day)

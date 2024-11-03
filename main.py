import random

class House:
    def __init__(self):
        self.mess_level = 0
        self.food = 0

class Auto:
    brands_of_car = ["Toyota", "Ford", "BMW", "Audi", "Mercedes"]

    def __init__(self, brand=None):
        self.brand = brand if brand else random.choice(Auto.brands_of_car)
        self.fuel = 100
        self.durability = 100

    def drive(self):
        return self.fuel > 0 and self.durability > 0

    def to_repair(self):
        self.durability += 100

class Human:
    def __init__(self):
        self.home = None
        self.car = None
        self.job = None
        self.money = 100
        self.satiety = 50
        self.happiness = 50
        self.salary = 0

    def get_home(self):
        if not self.home:
            self.home = House()

    def get_car(self):
        if not self.car:
            self.car = Auto()

    def get_job(self):
        if self.car and self.car.drive():
            self.job = "Engineer"
            self.salary = 100
        else:
            if self.car:
                self.to_repair()

    def eat(self):
        if self.home.food > 0:
            self.satiety = min(self.satiety + 5, 100)
            self.home.food -= 1
        else:
            self.shopping("food")

    def work(self):
        if self.car and not self.car.drive():
            if self.car.fuel <= 0:
                self.shopping("fuel")
            else:
                self.to_repair()
            return

        self.money += self.salary
        self.satiety -= 5
        self.happiness -= 5

    def shopping(self, manage):
        if self.car and not self.car.drive():
            if self.car.fuel <= 0:
                self.shopping("fuel")
            else:
                self.to_repair()
            return

        if manage == "food":
            self.home.food += 10
            self.money -= 20
        elif manage == "fuel":
            self.car.fuel += 20
            self.money -= 10
        elif manage == "delicacies":
            self.happiness += 10
            self.money -= 15

    def chill(self):
        self.happiness += 10
        if self.home:
            self.home.mess_level += 5

    def clean_home(self):
        self.happiness -= 5
        if self.home:
            self.home.mess_level = 0

    def to_repair(self):
        if self.car:
            self.car.durability = min(self.car.durability + 100, 100)
            self.money -= 50
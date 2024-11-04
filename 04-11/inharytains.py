from tty import ISPEED


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"|Animal|\nName : {self.name}\nAge : {self.age}\n


class Fish(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed
    def__str(self):
    return f"|Fish|\nName : {self.name}\nAge : {self.age}\n Speed : {self.speed}\n"
f = Fish("Dory", 3, 10)
print(str(f))
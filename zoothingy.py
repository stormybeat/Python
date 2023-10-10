import time
class Animal:
    def __init__(self,name):
        self.name = name
    def run(self):
        print(self.name)
class Dog(Animal):
    def run(self):
        print(self.name + " runs")
class Cat(Animal):
          def run(self):
            print(self.name + " sneaks")
class Frog(Animal):
     def run(self):
          print(self.name + " hops")
class Hawk(Animal):
     def run(self):
          print(self.name + " dives")
class Mouse(Animal):
     def run(self):
          print(self.name + " scrambles")
T = Frog("Tam")
I = Dog("Iz")
L = Cat("Liz")
H = Hawk("Eye")
M = Mouse("Mouseatouille")
animalList = T,I,L,H,M
while True:
    for a in animalList:
        a.run()
        time.sleep(.5)
import time
import random 

class Animal:
    def __init__(self,name):
        self.name = name
    def run(self):
        print(self.name)

class Dog(Animal):
    def run(self):
        print(self.name + " barks")
class Cat(Animal):
    def run(self):
        print(self.name + " meows")
        

d = Dog("Fido")
c = Cat("Juny")

animal_list = [d,c]
while True:
    for a in animal_list:
        a.run()

    time.sleep(random.randrange(3))
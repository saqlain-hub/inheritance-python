# 06-07-2023
# Python - Object Oriented Programming
# attributes =  what an object is/has (ex. name, age, height)
# methods = an action of the object (ex. eat, sleep, make YouTube videos)
# names for object should be capital

class Animal:

    alive = True

    def eat(self):
        print("Tis animal is eating")

    def sleep(self):
        print("this animal is sleeping")


class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
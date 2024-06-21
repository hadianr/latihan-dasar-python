class Animal:
    def sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

class Cat(Animal):
    def sound(self):
        print("The cat meows")

animals = [Animal(), Dog(), Cat()]
for animal in animals:
    animal.sound()
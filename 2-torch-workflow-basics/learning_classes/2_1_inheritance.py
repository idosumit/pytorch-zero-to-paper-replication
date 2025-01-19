class Parent:
    hair_color = ['brown']

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.hair_color.append('purple')
    pass


# a = Parent()
# print(a.hair_color)

# b = Child()
# print(b.hair_color)

# improving on 1.1 code -->

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    def speak(self, sound="Bow"):
        return super().speak(sound)

class Bulldog(Dog):
    def speak(self, sound="Woof"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

"""
try these in interactive python: python3 -i 2_1_inheritance.py

jack.speak()
miles.speak()
miles.speak("Meow")
"""
# Exercise from: https://realpython.com/python3-object-oriented-programming/

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
    


miles = Dog("miles", 4)
print(miles) # or print(miles.__str__()) works the same way
print(miles.speak("Bark!"))
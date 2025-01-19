"""
Create a GoldenRetriever class that inherits from the Dog class.
Give the sound argument of GoldenRetriever.speak() a default value of "Bark".
"""

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)
    
golden_dog = GoldenRetriever("Fuzzy", 4)
print(golden_dog.speak())
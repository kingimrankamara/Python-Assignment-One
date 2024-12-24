# Base class (Animal)
class Animal:
    def move(self):
        pass

# Derived class (Bird)
class Bird(Animal):
    def move(self):
        return "Flying 🦅"

# Derived class (Fish)
class Fish(Animal):
    def move(self):
        return "Swimming 🐟"

# Derived class (Mammal)
class Mammal(Animal):
    def move(self):
        return "Walking 🦒"

# Polymorphism in action
def describe_movement(animal):
    print(animal.move())

# Creating instances of different animals
bird = Bird()
fish = Fish()
mammal = Mammal()

# Describing movements
describe_movement(bird)
describe_movement(fish)
describe_movement(mammal)

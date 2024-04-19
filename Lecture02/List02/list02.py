class Animal:
    number_of_animals = 0
    colors = []
    names = []
    nol = []
    animals = [names, colors, nol]
    
    def __init__(self, name, color, number_of_legs):
        self.name = name
        self.color = color
        self.number_of_legs = number_of_legs
        Animal.number_of_animals +=1
        Animal.colors.append(color)
        Animal.names.append(name)
        Animal.nol.append(self.number_of_legs)
        
    @classmethod
    def how_many_animals(self):
        return  f"There is {self.number_of_animals} animals"
    def description(self):
        description =""
        length = len(Animal.colors)
        for i in range(length):
                description += f"This is {Animal.animals[0][i]} it is {Animal.animals[1][i]} and has {Animal.animals[2][i]} legs\n"
        return description
        
class Bird(Animal):
    number_of_birds = 0
    def __init__(self, name, color):
        super().__init__(name, color, 2)
        Bird.number_of_birds += 1

class Fish(Animal):
    number_of_fish = 0
    def __init__(self, name, color):
        super().__init__(name, color, 0)
        Fish.number_of_fish += 1

class Mammal(Animal):
    number_of_mammals = 0
    def __init__(self, name, color, number_of_legs = -1):
        super().__init__(name, color, number_of_legs)
        Mammal.number_of_mammals += 1

class Dog(Mammal):
    number_of_dogs = 0
    def __init__(self, name, color):
        super().__init__(name, color, 4)
        Dog.number_of_dogs += 1
        
    @classmethod
    def info(self):
        return  f"There is {self.number_of_dogs} dogs. There are {self.number_of_animals} animals."

class Cat(Mammal):
    number_of_cats = 0
    def __init__(self, name, color):
        super().__init__(name, color, 4)
        Cat.number_of_cats +=1

        
dog = Dog("Zaki", "Brown")
cat = Cat("Harry", "Beige")
print(dog.description())

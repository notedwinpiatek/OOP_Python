class Car:
    carCounter = 0
    def __init__(self, brand, model, yearOfProduction, maxSpeed, platenumber):
        self.brand = brand
        self.model = model
        self.yearOfProduction = yearOfProduction
        self.maxSpeed = maxSpeed
        self.velocity = 0
        self.color = "not defined"
        Car.carCounter += 1
        if len(str(platenumber)) != 6:
            raise ValueError("Your plate number has to be 6digit number")
        else:
            self.platenumber = platenumber    
            
    
    def colorChange(self, color):
        self.color = color
    def run(self):
        self.velocity = self.maxSpeed*0.75
        print(f"You fast guy {self.velocity}")
    def stop(self):
        self.velocity = 0
        print("You just got stopped")
    
    def __str__(self):
        return f"This car is {self.brand} {self.model} produced in {self.yearOfProduction} in beautiful {self.color} color"
    @classmethod
    def description(self):
        return f"This is car class. Currently there is {self.carCounter} cars defined"

def carObj(brand, model, year, speed, plates):
    try:
        car = Car(brand, model, year, speed, plates)
        return car
    except ValueError as error:
        print(error)

def carCounter(car):
    if car.carCounter == 1:
        print(f"You have {car.carCounter} car right now!")
    else:
        print(f"You have {car.carCounter} cars right now!")
car1 = carObj('Peugeot', '206', 2010, 160, 123456)
car2 = carObj('Mercedes', 'G', 2020, 250, 212345)
car3 = carObj('Audi', 'RS6', 1997, 120, 212345)
car4 = carObj('Toyota', 'Supra', 2024, 120, 122345)
car5 = carObj('Nissan', 'GTR', 1997, 120, 122345)
car6 = carObj('BMW', 'E3śmieć', 1997, 0, 123245)
car7 = carObj('BMW', 'E46', 1997, 9999, 123425)
car8 = carObj('FSO', 'Polonez', 1997, 120, 123452)
car9 = carObj('Mazda', 'MX5', 1997, 120, 123453)
car10 = carObj('Toyota', 'A86', 1987, 120, 123345)
if car1:
    car1.colorChange('black')
    print(car1.color)
    car1.run()
    car1.stop()
    carCounter(car1)
if car2:
    car2.colorChange('dark green')


list_atributes = []
list_atributes.append(car8.brand)
list_atributes.append(car8.model)
list_atributes.append(car8.yearOfProduction)
list_atributes.append(car8.maxSpeed)
list_atributes.append(car8.platenumber)
list_atributes.append(car8.velocity)
list_atributes.append(car8.color)
print(list_atributes)
print(car1)
print(car1.description())

class Dealers:
    def __init__(self, name, car_brand):
        self.name = name
        self.car_brand = car_brand
        self.list_of_cars = []
    def new_car(self, car):
        self.list_of_cars.append(car)
    def __str__(self):
        str1 = f"The car dealer {self.name} have following cars:\n\n"
        for car in self.list_of_cars:
            str1 += f"{car.__str__()}\n\n"
        return str1
        
        
dealer = Dealers("jan", "kowalski cars")


for num in range(1,11):
    dealer.new_car(eval(f"car{num}"))

print(dealer)

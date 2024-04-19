class Employee:
    def __init__(self, name, age, number_of_hours, salary_per_hour, employeeID):
        self.name = name
        self.age = age
        self.salary = (number_of_hours, salary_per_hour)
        self.__employeeID = employeeID
        
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, salary):
        noh, sph = salary
        if (noh < 1):
            raise ValueError("You should've worked more!")
        if (sph < 27.7):
            raise ValueError("You probably earn a bit more :)")
        self._salary = noh * sph
    
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        self.email = f"{self._name}@company.com"
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if (18 > age > 99):
            raise ValueError("Your age has to be between 18 and 99")
        self._age = age
        
    def get_employeeID(self):
        return f"ID number of {self._name} is {self.__employeeID}"

class Manager(Employee):
    def __init__(self, name, age, number_of_hours, salary_per_hour, gender, phone_number):
        super().__init__(self, name, age, number_of_hours, salary_per_hour)
        self.gender = gender
        self.phone_number = phone_number
        
    @property
    def phone_number(self):
        return self.phone_number
    @phone_number.setter
    def phone_number(self, phone_number):
        if (len(phone_number) > 9):
            raise ValueError("Your phone number should contain 9 digits")
        return f"+48 {self.phone_number}"
        
try:
    John = Employee("John", 21, 109, 27.7, 2137)
    Rebeca = Manager("Rebeca", 9, 180, 21.5, 2115)
    print(f"Name: {John.name}\nAge: {John.age}\n")
    print(John.get_employeeID())
    print(John.salary)
    print(Rebeca.email)
    
except ValueError as e:
    print(e)
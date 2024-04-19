class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades
        
class Professor(Person):
    pass

new_student = Student("John", 21)
print(new_student.age)
print(type(new_student))
print(isinstance(new_student, Student))
print(isinstance(new_student, Person))
print(issubclass(Student, Person))
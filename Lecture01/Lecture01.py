class Student:
    student_count = 0
    def init(self, given_name="Henry", given_age=20):
        self.name = given_name
        self.age = given_age
        Student.student_count = Student.student_count + 1
    def hello(self):
        print(f'hello {self.name}')
    def str(self):
        return self.name
    
    @classmethod
    def description(self):
        return(f"This is class about students, there are {self.student_count} students")
    @staticmethod
    def description2():
        return(f"This is class about students")

student1 = Student()
print(student1.name)
student1.hello()

student2 = Student()
student2.name = 'Mark'
print(student2.name)


print(dir(Student))
# lists all methods and attributes

student3 = Student("Edwin", 20)
print(student3.age)
print(student3.name)
print(student3.student_count)
print(student3.description())
print(student3.description2())
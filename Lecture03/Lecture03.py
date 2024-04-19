class Person:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"name: {self.name}; age: {self.age};")
person = Person('John', 23)
person2 = Person('William')
# accessing using class methid
person.info()
person2.info()
# accessing directly from outside
print(person.name)
print(person.age)

# _variable -> _ is just for the human and it doesn't block access from another class

class Person:
    def __init__(self, name, age=20):
        self._name = name
        self._age = age
    
    def info(self):
        print(f"name: {self._name}; age: {self._age};")
person = Person('John', 23)
person2 = Person('William')
# accessing using class methid
person.info()
person2.info()
# accessing directly from outside
print(person._name)
print(person._age)

# __variable -> __ is blocking the access from another class
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23
t = Test()
print(dir(t))
print(t._Test__baz)

# https://www.youtube.com/watch?v=jCzT9XFZ5bw
import math

class Calculator:
    def average(self, my_list):
        if (not isinstance(my_list, list)):
            raise ValueError
        return sum(my_list) / len(my_list)

    def add(self, x, y):
        if (not isinstance(x, (int, float)) or not isinstance(y, (int, float))):
            raise ValueError
        return x + y

    def divide(self, x, y):
        if (y == 0):
            raise ZeroDivisionError
        return x / y


    def calc_c(self, a, b):
        if (not isinstance(a, (int, float)) or not isinstance(b, (int, float))):
            raise ValueError
        sum = a**2 + b**2
        return math.sqrt(sum)

    def calc_zero(self, a, b, c):
        if (not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float))):
            raise ValueError       
        if ((a == 0 and b == 0 and c != 0) or (b == 0 and c == 0 and a != 0) or (a == 0 and c == 0 and b !=0 )):
            raise ValueError   
                        
        if (a == 0):
            if (b == 0 and c == 0):
                return 0
            return -c/b
        else:
            discriminant = b**2 - 4*a*c
            if discriminant > 0:
                x1 = (-b - math.sqrt(discriminant))/2*a
                x2 = (-b + math.sqrt(discriminant))/2*a
                return (x1, x2)
            if discriminant == 0:
                x = -b/2*a
                return x
            else:
                raise ValueError("negative discriminant")
        

        
        
        
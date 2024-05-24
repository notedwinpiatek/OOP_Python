import unittest
import math
from calculator import Calculator

calculator = Calculator()

class TestCalculator(unittest.TestCase) :
    # adition
    def test_add_positive(self):
        self.assertEqual(3, calculator.add(1, 2))
        
    def test_add_floats(self):
        self.assertEqual(2.5, calculator.add(1.2, 1.3))
        
    def test_add_negative(self):
        self.assertEqual(-4, calculator.add(-2, -2))
        self.assertEqual(-2, calculator.add(0, -2))
        
    def test_add_zero(self):
        self.assertEqual(0, calculator.add(0, 0))
        
    def test_add_not_number(self):
        with self.assertRaises(ValueError):
            calculator.add("2", "3")
        with self.assertRaises(ValueError):
            calculator.add("2", 3)
        with self.assertRaises(ValueError):
            calculator.add("a", "b")
    
    # division 
    def test_divide_positive(self):
        self.assertEqual(5, calculator.divide(10, 2)) 
        
    def test_divide_negative(self):
        self.assertEqual(2, calculator.divide(-2, -1))    
    
    def test_divide_floats(self):
        self.assertEqual(5, calculator.divide(5.5, 1.1)) 
          
    def test_divide_edge(self):
        self.assertEqual(0, calculator.divide(0, 2))
        
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(2, 0)
            
    def test_devide_not_number(self):
        with self.assertRaises(TypeError):
            calculator.divide("2", "3")
        with self.assertRaises(TypeError):
            calculator.divide("2", 3)
        with self.assertRaises(TypeError):
            calculator.divide("a", "b")
            
    # average
    def test_average_positive(self):
        self.assertEqual(3, calculator.average([3, 2, 4]))
        
    def test_average_floats(self):
        self.assertAlmostEqual(1.67, calculator.average([2, 2, 1]), places=2)
        self.assertAlmostEqual(-0.67, calculator.average([-1, -3, 2]), places=2)
        
    def test_average_negative(self):
        self.assertEqual(-3, calculator.average([-3, -2, -4]))
        
    def test_average_edge(self):
        self.assertEqual(0, calculator.average([0]))
        
    def test_average_not_list(self):
        with self.assertRaises(ValueError):
            calculator.average('')
            
    def test_average_not_numbers_in_list(self):      
        with self.assertRaises(TypeError):
            calculator.average([1, "2"])      
        with self.assertRaises(TypeError):
            calculator.average(["a", "b", "c"])       
            
    # c in triangle
    def test_c_positive(self):
        self.assertEqual(5, calculator.calc_c(4, 3))
        
    def test_c_negative(self):
        self.assertEqual(5, calculator.calc_c(-4, -3))
        
    def test_c_floats(self):
        self.assertAlmostEqual(5.28, calculator.calc_c(3.2, 4.2), places=2)
        
    def test_c_edge(self):
        self.assertEqual(0, calculator.calc_c(0, 0))
        
    def test_c_not_numbers(self):
        with self.assertRaises(ValueError):
            calculator.calc_c('2', '3')
        with self.assertRaises(ValueError):
            calculator.calc_c('2', 3)
        with self.assertRaises(ValueError):
            calculator.calc_c('a', 'b')
            
    # calculate zeros
    def test_zeros_positive(self):
        self.assertEqual((-3, -1), calculator.calc_zero(1, 4, 3))
        
    def test_zeros_negative(self):
        self.assertEqual((-3, 1), calculator.calc_zero(1, 2, -3))
        
    def test_zeros_floats(self):
        self.assertEqual((-3.2, -1), calculator.calc_zero(1, 4.2, 3.2))
        
    def test_zeros_edge(self):
        self.assertEqual(0, calculator.calc_zero(0, 0, 0))
        
    def test_zeros_two_zeros(self):
        with self.assertRaises(ValueError):
            calculator.calc_zero(0, 0, 1)
        with self.assertRaises(ValueError):
            calculator.calc_zero(1, 0, 0)
        with self.assertRaises(ValueError):
            calculator.calc_zero(0, 1, 0)
        
    def test_zeros_not_number(self):
        with self.assertRaises(ValueError):
            calculator.calc_zero('1', 2, '3')
        with self.assertRaises(ValueError):
            calculator.calc_zero('1', '2', '3')
        with self.assertRaises(ValueError):
            calculator.calc_zero('a', 'b', 'c')
            
    def test_zeros_a_is_zero(self):
        self.assertEqual(-2, calculator.calc_zero(0, 3, 6))
        
    def test_zeros_b_is_zero(self):
        self.assertEqual((-3, 3), calculator.calc_zero(1, 0, -9))
        
    def test_zeros_c_is_zero(self):
        self.assertEqual((-3, 0), calculator.calc_zero(1, 3, 0))
        
    
if __name__ == "__main__":
 unittest.main()

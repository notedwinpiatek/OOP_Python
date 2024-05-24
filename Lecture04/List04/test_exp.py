import unittest
from exp import M_Math

class Test_M_Math(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, M_Math.add(1, 2))
        
    def test_add_strings(self):
        with self.assertRaises(ValueError):
            M_Math.add("1", "2")  
                  
    def test_add_bools(self):
        with self.assertRaises(TypeError):
            M_Math.add(True, "2")   
                 
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            M_Math.divide(1, 0)        
if __name__ == "__main__":
    unittest.main()

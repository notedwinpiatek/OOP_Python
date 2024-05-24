import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee("Nick", "Nelson", 20)
        self.employee2 = Employee("Mick", "Melson", 30)
        self.employee3 = Employee("Rick", "Relson", 25)
    
    def test_init(self):
        self.assertEqual(self.employee1.first, "Nick")
        self.assertEqual(self.employee1.last, "Nelson")
        self.assertEqual(self.employee1.pay, 20)
    
    def test_invalid_first(self):
        with self.assertRaises(ValueError):
            Employee(1, "Nelson", 20)
            
    def test_invalid_last(self):
        with self.assertRaises(ValueError):
            Employee("Nick", True, 20)
            
    def test_invalid_pay(self):
        with self.assertRaises(ValueError):
            Employee("Nick", "Nelson", "20")
            
    def test_email(self):
        self.assertEqual(self.employee1.email, "Nick.Nelson@email.com")
               
    def test_email_change(self):
        self.employee3.first = "Tick"
        self.assertEqual(self.employee3.email, "Tick.Relson@email.com")
        
    def test_fullname_change(self):
        self.employee2.last = "Telson"
        self.assertEqual(self.employee2.fullname, "Mick Telson")
        
    def test_raise(self):
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.pay, 21)
        
    def test_cut(self):
        self.employee2.apply_cut()
        self.assertEqual(self.employee2.pay, 28.5)
    
    def test_edge_raise_min(self):
        self.employee1.pay = 0
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.pay, 0)
        
    def test_edge_raise_max(self):
        self.employee2.pay = 99999999
        self.employee2.apply_raise()
        self.assertEqual(self.employee2.pay, 99999999 / 100 * 5 + 99999999)
        
    def test_edge_cut_min(self):
        self.employee1.pay = 0
        self.employee1.apply_cut()
        self.assertEqual(self.employee1.pay, 0)
        
    def test_negative_pay(self):
        with self.assertRaises(ValueError):
            Employee("Jick", "Jelson", -20)
        
    def test_pay_change(self):
        self.employee1.pay = 30
        self.assertEqual(30, self.employee1.pay)
        self.employee1.apply_raise()
        self.assertEqual(31.5, self.employee1.pay)
               
    def test_full_name(self):
        self.assertEqual(self.employee1.fullname, "Nick Nelson")
        
if __name__ == "__main__":
 unittest.main()
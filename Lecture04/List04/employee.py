class Employee:

    def __init__(self, first, last, pay):
        if (not isinstance(first, str) or not isinstance(last, str) or not isinstance(pay, (int, float))):
            raise ValueError("invalid input")
        self.first = first
        self.last = last
        self.pay = pay
    
    @property 
    def pay(self):
        return self._pay
    
    @pay.setter
    def pay(self, pay):
        if (not isinstance(pay, (int, float)) or pay < 0):
            raise ValueError
        self._pay = pay
        
    @property 
    def first(self):
        return self._first
    
    @first.setter
    def first(self, first): 
        if not isinstance(first, str):
            raise ValueError
        self._first = first
     
    @property
    def last(self):
        return self._last
    
    @last.setter
    def last(self, last):
        if not isinstance(last, str):
            raise ValueError
        self._last = last
        
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
 
    def apply_raise(self):
        raise_amt = self.pay * 5 / 100
        self.pay = round(self.pay + raise_amt, 2)

    def apply_cut(self):
        cut_amt = self.pay * 5 / 100
        self.pay = round(self.pay - cut_amt, 2)
        
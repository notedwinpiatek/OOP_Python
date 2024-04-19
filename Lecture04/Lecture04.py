# test_port1.py

# import unittest
# from portfolio1 import Portfolio

# class PortfolioTest(unittest.TestCase):
#     def test_buy_one_stock(self):
#         p = Portfolio()
#         p.buy("IBM", 100, 176.48)
#         assert p.cost() == 17648.0
        



# $ python - m unittest test_port1


# class Test(unittest.TestCase):
#     @unittest.skip("Not done yet")
#         def test():
#             pass
#     @unittest.fail("Write this test!")

lst = [1, 2, 3, 4, 5, 6]

def avgTest(lst):
    avg = sum(lst)/len(lst)
    return avg
print(avgTest(lst))
import unittest
def div(x,y):
    # assert y != 0,"Cannot divide by zero"
    return x/y

class TestDiv(unittest.TestCase):
    def test_div_pass(self):
        self.assertEqual(div(10,2),5)
        
        
    def test_div_fail(self):
        self.assertEqual(div(10,2),4.9)


if __name__=="__main__":
    unittest.main()




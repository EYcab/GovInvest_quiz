__author__ = 'Chenxi'
from financial_cal import *
import unittest
# below is a set of test to perform a testing on our financial_cal.py code
# Here,I check if all the data types are converted or correct
# It also checks if our program's running results matches with the actual results

# All tests are passed

#initiate value to check if our check_numbers() runs as expected
a,b,c,d,e = check_numbers(1,1.0,1,1,1)
# initiate value to check if our financial_calc() runs as expected

sample1 = financial_calc(13,5,0,5000,0)
future_value = sample1.future_value_cal()
future_value2 = sample1.continuous_cal(4,5,-12000)

class test_equality(unittest.TestCase):
    def test_type_N(self):
        self.assertIs(type(a),int)
    def test_type_i(self):
        self.assertIs(type(b),float)
    def test_type_pv(self):
        self.assertIs(type(c),float)
    def test_type_pmt(self):
        self.assertIs(type(d),float)
    def test_type_fv(self):
        self.assertIs(type(e),float)
    def test_result_equal_on_future_value_cal(self):
        self.assertEqual(future_value,88564.9142)
    def test_result_equal_on_continuous_cal(self):
        self.assertEqual(future_value2,55929.7068)

if __name__ == "__main__":
    unittest.main()

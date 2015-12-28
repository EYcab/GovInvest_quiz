__author__ = 'Chenxi'

import math
from types import *
# the below check_numbers is to check if all the key value except for N is converted to a float type
# if they are not in the correct type,we will convert them back to the right value
def check_numbers(N,i,PV,PMT,FV):
    if N is not int:
        N = int(N)
    if i is not FloatType:
        i = float(i) / 100
    if PV is not FloatType:
        PV = float(PV)
    if PMT is not FloatType:
        PMT = float(PMT)
    if FV is not FloatType:
        FV = float(FV)
    if N!=0 and (i<1 and i>0):
        #print N, i, PV, PMT, FV
        return N, i, PV, PMT, FV
    else:
        raise PyInputErrorException("InputError")

# Error is thrown when the above function returns nothing and raise a input error
class PyInputErrorException(Exception):
    pass

#Below is the financial_calc class including 2 methods:
#  future_value_cal is to calculate a future value when a set of inputs is initiated
#  continue_cal is to calculate a future value after we get the 1st future value result
class financial_calc:
    def __init__(self, N=0, i=0.0, PV=0.0, PMT=0.0, FV=0.0):
        """
        :rtype : object
        """
        self.num_yr = N
        self.interest = i
        self.present_value = PV
        self.payment = PMT
        self.future_value = FV

    def future_value_cal(self):
        self.num_yr,self.interest,self.present_value,self.payment,self.future_value=\
            check_numbers(self.num_yr,self.interest,self.present_value,self.payment,self.future_value)
        self.interest_factor = 1.0 + self.interest
        if self.payment != 0 or self.present_value != 0:
            self.future_value = self.present_value * math.pow(self.interest_factor, self.num_yr) \
                                + self.payment * (math.pow(self.interest_factor, self.num_yr) - 1) / self.interest
            # a temp is to hold a value in case of a future assignment
            self.temp = self.future_value
            # print "future_value: ", self.future_value
            return round(self.future_value,4)
        else:
            self.future_value = 0
    def continuous_cal(self,Num,Interest,PMT):
        self.future_value = 0.0
        self.present_value = self.temp
        self.num_yr = Num
        self.interest = Interest
        self.payment = PMT
        return self.future_value_cal()


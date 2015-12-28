__author__ = 'Chenxi'
from financial_cal import *
# This code is to show you the result for our question 2

if __name__ == '__main__':
    Fin = financial_calc(13,5,0,5000,0)
    future_value = Fin.future_value_cal()
    print "our first result: ", future_value
    future_value = Fin.continuous_cal(4,5,-12000)
    print "our final result: ", future_value


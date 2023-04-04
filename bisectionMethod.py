import math as m
from pylab import *

import ekor as g

temp = []
valone = []
myx = []

def f(x):
    return x**3+4*x**2-10


def Startbisection(x0,x1):

    I=10
    global val
    x0 = float(x0)
    x1 = float(x1)
    if x0 > x1:
        val = x0
    else:
        val = x1
    I = float(I)
    if f(x0) * f(x1) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    else:
        step = 1
        print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
        temp.append('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
        condition = True
        while condition:
            x2 = (x0 + x1) / 2
            print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
            temp.append('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2

            step = step + 1
            if I < step:
                condition = False

        print('\nRequired Root is : %0.8f' % x2)
        temp.append('\nRequired Root is : %0.8f' % x2)
        myx.append(x2)
        valone.append(val)
        #g.plot_my_graph(x2,val)


        return temp,myx,valone


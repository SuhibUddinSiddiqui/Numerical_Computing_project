def f(x):
    return x**3+4*x**2-10

temp = []
valone = []
myx = []

def startfalsePosition(x0,x1):
    x0 = float(x0)
    x1 = float(x1)
    global val
    if x0 > x1:
        val = x0
    else:
        val = x1

    I = 10
    # Checking Correctness of initial guess values and false positioning
    if f(x0) * f(x1) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    else:
        step = 1
        print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
        temp.append('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')

        condition = True
        while condition:
            x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
            print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
            temp.append('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2

            step = step + 1
            if I < step:
                condition = False

        print('\nRequired root is: %0.8f' % x2)
        temp.append('\nRequired Root is : %0.8f' % x2)
        myx.append(x2)
        valone.append(val)
        return temp, myx, valone



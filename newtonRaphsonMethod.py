
def f(x):
    return x**3+4*x**2-10

def g(x):
    return 3*x**2+8*x

temp = []
valone = []
myx = []



def startnewtonRaphson(x0):
    val = x0
    x0 = float(x0)
    N = 5
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    temp.append('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        temp.append('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if abs(f(x1)) < 0.00001:
            flag = 0
            break

        # condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
        temp.append('\nRequired root is: %0.8f' % x1)
        myx.append(x1)
        valone.append(val)
        return temp, myx, valone

    else:
        print('\nNot Convergent.')
        temp.append('\nRequired root is: %0.8f' % x1)
        myx.append(x1)
        valone.append(val)
        return temp, myx, valone


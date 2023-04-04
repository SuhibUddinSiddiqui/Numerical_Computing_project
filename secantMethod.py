def f(x):
    return x**3+4*x**2-10

temp = []
valone = []
myx = []


def startsecant(x0, x1):
    x0 = float(x0)
    x1 = float(x1)
    global val
    if x0 > x1:
        val = x0
    else:
        val = x1

    I = 10
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    temp.append('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        temp.append('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > I:
            condition = False
    print('\n Required root is: %0.8f' % x2)
    temp.append('\n Required root is: %0.8f' % x2)
    myx.append(x1)
    valone.append(val)
    return temp, myx, valone




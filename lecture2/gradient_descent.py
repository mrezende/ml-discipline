# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 3*x + 2

def df(x):
    return 2*x -3


x = 3
n = 100
step = 0.1

lx = [x]
lf = [f(x)]
ldf = [df(x)]


for i in range(n):
    x = x - step * df(x)
    lx.append(x)
    lf.append(f(x))
    ldf.append(df(x))

print('O x que minimiza f é %f' % x)

plt.plot(lx, lf, 'bo')
plt.plot(lx, ldf, 'r+')
plt.show()




# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:27:58 2018

@author: Marcelo de Rezende Martins
"""

import matplotlib.pyplot as plt
import numpy as np
import random as r
import math

def custo(ye, y):
    c = 0
    for i in range(len(y)):
        c += (ye[i] - y[i])**2
    return c/len(y)





potencias = [50, 100, 150, 230, 75, 90, 120, 200, 80, 140]

consumos = [12, 9, 7, 3, 11, 10, 6, 4, 11, 7]
m = len(consumos) # número de amostras



for potencia in potencias:
    print('potência =', potencia)

r.seed(1)
custox = 100
t0 = 30
t1 = 1



lt0 = [i for i in range(20, 31)]
lt1 = [-i*0.1 for i in range(11)]

print(lt0)
print(lt1)

for th0 in lt0:
    for th1 in lt1:
        ye = []
        for j in range(m):
            ye.append(th0 + th1*potencias[j])
        cc = custo(ye, consumos)
        if(cc < custox):
            t0, t1 = th0, th1
            plt.plot([0, 225], [t0,t0 + t1*255], color='grey')
            custox = cc
            

print(custox, t0, t1)

plt.plot([0, 225], [t0,t0 + t1*255], color='red')
plt.plot(potencias, consumos, 'bo')
plt.show()

print('-------------------------')
print('pot | y | ye | erro')
for i in range(m):
    yec = (t0 + t1*potencias[i])
    print(i + 1, potencias[i], consumos[i], yec, math.fabs(consumos[i] - yec))
    




#print(potencia)


#m1 = np.array([[1,2], [3,4]])

#print(m1)

#print(m1*m1)
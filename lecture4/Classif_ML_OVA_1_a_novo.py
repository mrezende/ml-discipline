# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math
import numpy as np

def sigmoid(x):
    return (1/(1+math.exp(-x)))

m1 = float(input('medida 1 '))
m2 = float(input('medida 2 '))
m3 = float(input('medida 3 '))
m4 = float(input('medida 4 '))

medias = [5.84, 3.05, 3.75, 1.98]
desv = [0.825, 0.432, 1.76, 0.76]

mod1 = [-4.5128560873541845, -1.8977108150376218, 3.0680515723848103, -4.3141179217623291, -3.9491028126885279]
mod2 = [-1.0000531298916975, -0.2085894972691261, -1.2011035271389141, 2.2848674271932574, -2.0569025485283308]
mod3 = [-11.735630293206775, -1.3936067254172166, -1.6811448678365926, 9.6809357864896768, 8.6435586041283301]

mod1 = np.array(mod1)
mod2 = np.array(mod2)
mod3 = np.array(mod3)

medidas = [m1, m2, m3, m4]

for i in range(len(medidas)):
    medidas[i] = (medidas[i] - medias[i])/desv[i]

medidas = [1] + medidas

pred1 = sigmoid(np.dot(mod1.transpose(), medidas))
pred2 = sigmoid(np.dot(mod2.transpose(), medidas))
pred3 = sigmoid(np.dot(mod3.transpose(), medidas))

print(pred1, 'setosa')
print(pred2, 'versicolor')
print(pred3, 'virginica')
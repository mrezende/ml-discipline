#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
IPT - Aprendizado de Máquina 2018
Analisar código classificação

Tarefa 1 : Obter índice de acertos

"""


import numpy as np
from sklearn import linear_model
import math

def med(fe):
    tam=len(fe)
    med=sum(fe)/tam
    return med

def sdev(fe):
    tam=len(fe)
    soma=0
    media=med(fe)
    for e in fe:
        soma+=(e-media)**2
    return math.sqrt(soma/tam) 

def standard(fe):
    media=med(fe)
    dp=sdev(fe)
    fes=[]
    for e in fe:
        fes.append((e-media)/dp)
    return fes
    
 

# import some data to play with
arq = open('../data/banknotes.txt', 'r')
texto = arq.readlines()
arq.close()


lx1=[]
lx2=[]
lx3=[]
lx4=[]
X=[]
ly=[]

for l in texto:
   l1=l.split(",")
   lx1.append(float(l1[0]))
   lx2.append(float(l1[1]))
   lx3.append(float(l1[2]))
   lx4.append(float(l1[3]))
   ly.append(float(l1[4]))
'''   
lx1=standard(lx1)
lx2=standard(lx2)
lx3=standard(lx3)
lx4=standard(lx4)
'''
   
X = list(zip(lx1,lx2,lx3,lx4))


X=np.array(X)

Y = ly
Y=np.array(Y)


logreg = linear_model.LogisticRegression()

# todos os parâmetros estão default

model=logreg.fit(X, Y)


Z=logreg.predict(X)

certos=0
#
#  Tarefa 1 : obter índice de acertos
#
#
for i in range(len(Z)):
    if(int(Z[i]) == int(Y[i])):
        certos += 1

 
print('taxa=',certos/len(Z)) 


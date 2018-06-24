# -*- coding: utf-8 -*-
"""
IPT - Aprendizagem de Máquina 2018
Tarefas : 
    

    1)Observe que agora há apenas uma função grad (antes eram gradt0 e gradt1)
    2)Observe que o X agora tem mais uma coluna de 1s para generalizar a soma
    3)A função custo J é agora dividida por 2


"""
    
import matplotlib.pyplot as plt
import math
import numpy as np

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
    
 
def grad(x,y,theta):
    m=len(x)
    n=len(theta)
    s=[0 for i in range(n)]
    p=[0 for i in range(m)]
    for i in range(m):
        for j in range(n):
            
#aqui é feito o produto X*theta            
            
             p[i]=p[i]+x[i][j]*theta[j] 
             
#aqui é feito  X*theta - y              
             
        p[i]=p[i]-y[i]  
        
# finalmente é feito 1/m *X(transposta) *(x*theta-y)
        
    for i in range(n):
        for j in range(m):
            s[i]=s[i]+x[j][i]*p[j]
        s[i]=s[i]/m
    return s         
           
    

def novotheta(th,x,y,alfa):
     s=grad(x,y,th)
     for i in range(len(x[0])):
         th[i]=th[i]-alfa*s[i]
     return (th)


#
#Ye é a lista de y estimado e y é o a lista de y real
#
def custo(ye,y):
    m=len(ye)
    c=0
    for i in range(m):
        c=c+(ye[i]-y[i])**2
    return (0.5/m)*c
    
   
arq = open('../data/cars-mpg.txt', 'r')
texto = arq.readlines()
arq.close()
#
#lx é uma lista dos valores de x(potência) em float
#ly é uma lista dos valores de y(MPG) em float
#

lx=[]
ly=[]

for l in texto:
    if 'NA' not in l:
        l1=l.split()
        lx.append(float(l1[3]))
        ly.append(float(l1[0]))
        
   
laux=standard(lx)
lauy=ly
theta=[0.5,0.5]
lcusto=[]

#
#   o algoritmo abaixo termina se i atinge n ou se o custo varia menos que var
#    percentual de uma iteração para outra
#
m=len(laux)
n1=len(theta)
var = 0.0001
n=100
k=n
alpha=0.1
x1=[1.0 for i in range(m)]
#
#  nx é o novo x (contém mais uma coluna de 1's)
#
nx=list(zip(x1,laux))
for i in range(n):
    theta=novotheta(theta,nx,lauy,alpha)
    ye=[]
    for o in range(m):
        s=0
        for j in range(n1):
            s+=theta[j]*nx[o][j]
        ye.append(s)
    lcusto.append(custo(ye,lauy))
    print('custo=',lcusto[i])
    print(i,' ',theta)  
    if (i>0)and np.abs((lcusto[i]-lcusto[i-1])/lcusto[i-1]) < var:
        k=i
        break
        
print(k)
print(theta)
plt.plot([i for i in range(k)],[lcusto[m] for m in range(k)],'yo')

plt.show()



        
        
        
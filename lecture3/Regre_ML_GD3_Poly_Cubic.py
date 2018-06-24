# -*- coding: utf-8 -*-
"""
IPT - Aprendizagem de Máquina 2018
Tarefas : 
    
    Apenas montar a matriz X (nx)

    1)Observe que agora há apenas uma função grad
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
    m = len(y)
    aux = np.dot(x, theta) - y
    xt = x.transpose()
    return 1/m * np.dot(xt, aux)
       
          
    

def novotheta(th,x,y,alfa):
     s=grad(x,y,th)
     #print('s=',s)
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

lx1=[]
lx2=[]
lx3=[]
ly=[]

for l in texto:
    if 'NA' not in l:
        l1=l.split()
        lx1.append(float(l1[3]))
        lx2.append(float(l1[3])**2)
        lx3.append(float(l1[3])**3)
        ly.append(float(l1[0]))
        
for learning_rate in [0.1]:
    laux1=standard(lx1)
    laux2=standard(lx2)
    laux3=standard(lx3)
    lauy=ly
    theta=[0.5,0.5,0.5, 0.5]
    lcusto=[]
    
    #
    #   o algoritmo abaixo termina se i atinge n ou se o custo varia menos que var
    #    percentual de uma iteração para outra
    #
    m=len(laux1)
    n1=len(theta)
    var = 0.0001
    n=10000
    k=n
    
    #*********************************
    #
    #  Monte a matriz nx aqui...a X das fórmulas matriciais
    #  Primeira coluna só de 1´s e as outras com as features
    #  elementar...só para aquecimento
    #
    #********************************
    
    x1=[1.0 for i in range(m)]
    nx=list(zip(x1,laux1, laux2, laux3))
    
    nx = np.array(nx)
    lauy = np.array(lauy)
    theta = np.array(theta)


    for i in range(n):
        theta=novotheta(theta,nx,lauy,learning_rate)
        ye=[]
        for o in range(m):
            s=0
            for j in range(n1):
                s+=theta[j]*nx[o][j]
            ye.append(s)
        lcusto.append(custo(ye,lauy))
        #print('custo=',lcusto[i])
        #print(i,' ',theta)  
        if (i>0)and np.abs((lcusto[i]-lcusto[i-1])/lcusto[i-1]) < var:
            k=i
            break
            
    print(k)
    print(theta)
    
    plt.plot([i for i in range(k)],[lcusto[m] for m in range(k)],'yo')
    plt.title('Custo ao longo das iterações')
    plt.show()
    
    ye = np.dot(nx, theta)
    plt.plot(laux1, ye, 'bo')
    plt.show()
    
    ye = np.dot(nx, theta)
    plt.plot(lx1, ye, 'bo')
    plt.show()
    
    
    



        
        
        
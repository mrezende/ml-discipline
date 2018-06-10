# -*- coding: utf-8 -*-
"""
IPT - Aprendizagem de Máquina 2017
Tarefas : 
    1)crie a função standard que retorna a lista fes da feature padronizada,
    use as funções med e sdev
    
    2)Otimize theta0 e theta 1  (começando com 0.5 e 0.5) com Gradient Descent:
    use as funções gradt0, gradt1 e novotheta
    
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
    print(media,dp)
    fes=[]
    for e in fe:
        fes.append((e-media)/dp)
    return fes
    
    
def gradt0(x,y,theta):
    m=len(x)
    s=0
    for i in range(m):
        s+=(theta[1]*x[i]+theta[0])-y[i]

    return 2*s/m 

def gradt1(x,y,theta):
    m=len(x)
    s=0
    for i in range(m):
        s+=((theta[1]*x[i]+theta[0])-y[i])*x[i]
    return 2*s/m   
    

def novotheta(th,x,y,alfa):
     s1=gradt0(x,y,th)
     s2=gradt1(x,y,th)
     th[0]=th[0]-alfa*s1
     th[1]=th[1]-alfa*s2
     return (th)


#
#Ye é a lista de y estimado e y é o a lista de y real
#
def custo(ye,y):
    m=len(ye)
    c=0
    for i in range(m):
        c=c+(ye[i]-y[i])**2
    return (1.0/m)*c



    
   
arq = open('c:\dados\cars-mpg.txt', 'r')
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
        
#
#  laux é lx após feature scaling
#  O primeiros elemento de laux é 0.6641327329009109   
#      
laux=standard(lx)


print('\n\nFeature Scaling')

print('A primeira potência padronizada é ',laux[0],' ..valor esperado 0.6641')


theta=[0.5,0.5]
#
#  lcusto é uma lista dos custos ao longo das iterações
#
lcusto=[]

#
#   o algoritmo abaixo termina se i atinge n ou se o custo varia menos que var
#    percentual de uma iteração para outra


# Para gerar o gráfico os valores de theta 0 e theta 1 vão sendo colocados
# nas listas t1 e t2 durante as iterações

t0=[]
t1=[]
t0.append(theta[0])
t1.append(theta[1])


var = 0.00001
n=30  
k=n
alpha=0.1
#
#
#

for i in range(n):
    theta=novotheta(theta,laux,ly,alpha)
    t0.append(theta[0])
    t1.append(theta[1])
    ye=[theta[0]+theta[1]*laux[i] for i in range(len(laux))]
    lcusto.append(custo(ye,ly))
    if (i>0) and np.abs((lcusto[i]-lcusto[i-1])/lcusto[i-1]) < var:
        k=i
        break
   
    
    
   
print('\nIterações e custo final : ',i,lcusto[i]) 
print('Valores esperados  29 23.944535927933213')   


print('\nTheta0 e theta1 após Gradient Descent ',theta[0],theta[1])
print('Valores esperados :23.417512696261827 -6.0597417711599375')
plt.title('\n custo ao longo das iterações')
plt.plot([i for i in range(k)],[lcusto[m] for m in range(k)],'yo')

plt.show()


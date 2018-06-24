# -*- coding: utf-8 -*-
"""
IPT - Aprendizado de Máquina 2018
Analisar código classificação

Tarefa 1 : Escrever a função sig 

Tarefa 2 : Escrever a função custo matricialmente

Tarefa 3 : Escrever a função grad matricialmente

Tarefa 4 : Obter o índice de acertos

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
    xt = x.transpose()
    g = sig(np.dot(x, theta))
    
    return (1/m) * (np.dot(xt, (g - y)))
   

#
# Tarefa 3: Escrever a função grad Matricialmente
#  
            
           
    

def novotheta(th,x,y,alpha):
     s=grad(x,y,th)
#    print('s=',s)
     for i in range(len(x[0])):
         th[i]=th[i]-alpha*s[i]
     return (th)



def sigmoid(x):
    return (1/(1+math.exp(-x)))

def sig(v):
    l = []
    for x in v:
        l.append(sigmoid(x))
    l = np.array(l)
    return l   
   
#
#  Tarefa 1 Escrever a função sig, que recebe um vetor e
#  cria um novo vetor, pela aplicação da função sigmoid 
#  em todos os elementos do vetor
   


def custo(theta,y,x):
    m = len(y)
    hx = sig(np.dot(x, theta))
    yt = y.transpose()
    one_minus_y_t = (np.ones(m) - y).transpose()
    lh = np.log(hx)
    
    l1h = np.log(np.ones(m) - hx)
    
    p1 = -np.dot(yt, lh)
    p2 = np.dot(one_minus_y_t,l1h)
    
    return (1/m)*(p1 - p2)
    
  
#
#  Tarefa 2:  Escrver a função custo Matricialmente
#
   
arq = open('../data/banknotes.txt', 'r')
texto = arq.readlines()
arq.close()


lx1=[]
lx2=[]
lx3=[]
lx4=[]
ly=[]

for l in texto:
   l1=l.split(",")
   lx1.append(float(l1[0]))
   lx2.append(float(l1[1]))
   lx3.append(float(l1[2]))
   lx4.append(float(l1[3]))
   ly.append(float(l1[4]))
   
   
lx1=standard(lx1)
lx2=standard(lx2)   
lx3=standard(lx3) 
lx4=standard(lx4)


      

lcusto=[]
theta=[0.5,0.5,0.5,0.5,0.5]

m=len(lx1)
var = 0.0001
n=5000
alpha=0.2
k=n
x1=[1.0 for i in range(m)]
nx=list(zip(x1,lx1,lx2,lx3,lx4))
nx=np.array(nx)
ly=np.array(ly)

print(' Custo para theta inicial =',custo(theta,ly,nx))
print('valor esperado=1.075...')
input('Tecle para continuar')

theta_teste=novotheta(theta,nx,ly,alpha)
print('gradiente inicial = ',theta_teste)
print('valores esperados : [0.466,0.402,0.456,0.511,0.474]')
input('Tecle para continuar')


for i in range(n):
    print(i)
    theta=novotheta(theta,nx,ly,alpha)
    lcusto.append(custo(theta,ly,nx))
    if (i>0)and np.abs((lcusto[i]-lcusto[i-1])/lcusto[i-1]) < var:
        k=i
        break
        
print(k)
print(theta)

plt.plot([i for i in range(k)],[lcusto[m] for m in range(k)],'yo')
plt.title('Custo ao longo das iterações')
plt.show()


ye=sig(np.dot(nx,theta))

#
#  tarefa 5 : obter o índice de acertos
#
#
c = []
for i in range(len(ye)):
    c.append( 1 if ye[i] > 0.5 else 0)

certos = 0    
for i in range(len(c)):
    if(int(c[i]) == int(ly[i])):
        certos += 1

print('índice=',certos/len(ye)) 
print('indice esperado=0.98177842...')      
       
print(theta)

        
cont1 = 0
for i in range(len(ly)):
    cont1 += 1 if ly[i] == 1 else 0

print('Porcentagem de amostras positivas: ', 100*cont1/len(ly), '%')

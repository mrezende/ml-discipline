# -*- coding: utf-8 -*-
"""
IPT - Aprendizado de Máquina 2018
Analisar código classificação One vs. All

Tarefa 1 : Preparar os vetores ly para cada classificação

Tarefa 2:obter acurácias nas 3 classificações

Tarefa 3 : Obter os thetas dos 3 classificadores para 
atividade 4


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
    return [fes, media, dp]
    
 



def grad(x,y,theta):
    m = len(y)
    xt = x.transpose()
    g = sig(np.dot(x, theta))
    
    return (1/m) * (np.dot(xt, (g - y)))
            
            
    

def novotheta(th,x,y,alpha):
     s=grad(x,y,th)
     for i in range(len(x[0])):
         th[i]=th[i]-alpha*s[i]
     return (th)


#

#

def sigmoid(x):
    return (1/(1+math.exp(-x)))

def sig(v):
    l = []
    for x in v:
        l.append(sigmoid(x))
    l = np.array(l)
    return l
  

def otimiza(nx,y,theta,alpha,n,var):
    lcusto=[]
    for i in range(n):
        theta=novotheta(theta,nx,ly,alpha)
        lcusto.append(custo(theta,ly,nx))
        if (i>0)and np.abs((lcusto[i]-lcusto[i-1])/lcusto[i-1]) < var:
            break
    return [theta,lcusto]


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

   
arq = open('../data/iris.txt', 'r')
texto = arq.readlines()
arq.close()


lx1=[]
lx2=[]
lx3=[]
lx4=[]
ly_txt=[]

media = []
m = 0.0
std = []
s = 0.0

for l in texto:
   l1=l.split(",")
   lx1.append(float(l1[0]))
   lx2.append(float(l1[1]))
   lx3.append(float(l1[2]))
   lx4.append(float(l1[3]))
   ly_txt.append(str(l1[4])[:-1])  
   

   

lx1, m, s = standard(lx1)
media.append(m)
std.append(s)
lx2, m, s=standard(lx2)   
media.append(m)
std.append(s)
lx3, m, s=standard(lx3)
media.append(m)
std.append(s)
lx4, m, s=standard(lx4)
media.append(m)
std.append(s)

#      
#one-vs-all parte 1 : 
#
# Iris-setosa = 1, outras =0
#
#
# montando ly Iris-setosa

ly=[]
for i in range(len(lx1)):
    if(ly_txt[i] == "Iris-setosa"):
        ly.append(1.0)
    else:
        ly.append(0.0)
#
#  
#
    

theta=[0.5,0.5,0.5,0.5,0.5]
#
#
m=len(lx1)
n=20000
var=0.000001
alpha=0.2
x1=[1.0 for i in range(m)]
nx=list(zip(x1,lx1,lx2,lx3,lx4))
nx=np.array(nx)
ly=np.array(ly)

#setosa
lresp=otimiza(nx,ly,theta,alpha,n,var)



theta=lresp[0]
lcusto=lresp[1]


plt.plot([i for i in range(len(lcusto))],[lcusto[m] for m in range(len(lcusto))],'yo')
plt.title('Custo ao longo das iterações')
plt.show()


ye=sig(np.dot(nx,theta))

for i in range(len(ye)):
    if(ye[i]>0.5):
        ye[i]=1.0
    else:
        ye[i]=0.0
        
certos=0
#calcular acurácia
for i in range(len(ye)):
    if(int(ye[i]) == int(ly[i])):
        certos += 1
 
print('taxa de acerto setosa =',certos/len(ye))  
print(theta)
     
       
input('tecle para continuar')  


#      
#one-vs-all parte 2 : 
#
# Iris-versicolor = 1, outras =0
#
#
#
# montando ly Iris-versicolor

ly=[]
for i in range(len(lx1)):
    if(ly_txt[i] == "Iris-versicolor"):
        ly.append(1.0)
    else:
        ly.append(0.0)
        


   

theta=[0.5,0.5,0.5,0.5,0.5]

ly=np.array(ly)
n=20000
var=0.000000000
alpha=0.5
#versicolor
lresp=otimiza(nx,ly,theta,alpha,n,var)



theta=lresp[0]
lcusto=lresp[1]


plt.plot([i for i in range(len(lcusto))],[lcusto[m] for m in range(len(lcusto))],'yo')
plt.title('Custo ao longo das iterações')
plt.show()


ye=sig(np.dot(nx,theta))

for i in range(len(ye)):
    if(ye[i]>0.5):
        ye[i]=1.0
    else:
        ye[i]=0.0
        
certos=0
#calcular acurácia
for i in range(len(ye)):
    if(int(ye[i]) == int(ly[i])):
        certos += 1
 
print('taxa de acerto versicolor=',certos/len(ye))       
print(theta) 
 
input('tecle para continuar')   
#      
#one-vs-all parte 3 : 
#
# Iris-virginica = 1, outras =0
#
#
# montando ly Iris-virginica

ly=[]
ly=[]
for i in range(len(lx1)):
    if(ly_txt[i] == "Iris-virginica"):
        ly.append(1.0)
    else:
        ly.append(0.0)

theta=[0.5,0.5,0.5,0.5,0.5]

ly=np.array(ly)
n=20000
var=0.000001
alpha=0.2
#virginica
lresp=otimiza(nx,ly,theta,alpha,n,var)


theta=lresp[0]
lcusto=lresp[1]


plt.plot([i for i in range(len(lcusto))],[lcusto[m] for m in range(len(lcusto))],'yo')
plt.title('Custo ao longo das iterações')
plt.show()


ye=sig(np.dot(nx,theta))

for i in range(len(ye)):
    if(ye[i]>0.5):
        ye[i]=1.0
    else:
        ye[i]=0.0
        
certos=0
#calcular acurácia
for i in range(len(ye)):
    if(int(ye[i]) == int(ly[i])):
        certos += 1


print('taxa de acerto virginica =',certos/len(ye))       
print(theta) 

print('Media: ', media)
print('Std: ', std)
   

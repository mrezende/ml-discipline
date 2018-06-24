# -*- coding: utf-8 -*-

"""
IPT - Aprendizagem de Máquina 2017
Tarefas : 
    

    Observar o uso do numpy para fazer operações matriciais


"""

import numpy as np

l1=[[1,2],[3,4]]
l2=[[1,1],[5,7]]

# convertendo as listas em matrizes

m1=np.array(l1)
m2=np.array(l2)

print(' A lista l1 virou a matriz m1')
print(m1)

input("Tecle para continuar...")

# multiplicando m1 x m2

prod=np.dot(m1,m2)
print(' Produto m1 x m2')
print(prod)
input("Tecle para continuar...")

# multiplicando a matriz m1 pelo escalar 2

m1=2*m1
print(' Produto de m1 pelo escalar 2')
print(m1)

# inversão da matriz m2 

m2inv=np.linalg.inv(m2)
print(' Inversão da matriz m2 com linalg (linear algebra)')
print(m2inv)
input("Tecle para continuar...")

# Se m2inv é m2 invertida....m2inv*m2=identidade..vamos verificar

iden=np.dot(m2inv,m2)
print(' Será que obtivemos a matriz identidade com m2inv*m2?')
print(iden)
input("Tecle para continuar...")

#qual será a dimensão de m2?

print(' qual será a dimensão de m2?')
print(np.shape(m2))
input("Tecle para continuar...")

#Obtendo a transposta de m2 ?


print('m2 e Transposta de m2?')
m2t=m2.transpose()
print(m2)
print(m2t)
input("Tecle para continuar...")

#mudando o formato de m2 de 2x2 para 4x1
print('Mudando o formato de 2x2 para 4x1 em m2')
m2=np.reshape(m2,(4,1))
print(m2)
input("Tecle para continuar...")
m2 = np.reshape(m2, (2,2))
print(m2)
input("Tecle para continuar...")

#criando uma matriz 3xx de zeros

print('Criando matriz 3x3 de zeros')
z3=np.zeros((3,3))
print(z3)
input("Tecle para continuar...")

#criando uma matriz 3xx de zeros

print('Criando matriz  identidade de dimensão 4')
i4=np.identity(4)
print(i4)


#Exercício 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt
from math import trunc
from math import hypot

catOp = int(input("O valor do cateto oposto: "))
catAdj = int(input("O valor do cateto adjacente: "))
#h²=ca²+co²
#Podemos fazer por: hip = sqrt(catOp **2 + catAdj**2)
#Podemos também fazer por hip = (catOp ** 2 + catAdj ** 2) ** (1/2)
hip = hypot(catOp, catAdj)
print('O valor da hipotenusa é {}'.format(hip))
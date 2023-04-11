'''Escreva um programa que leia três números e mostre qual é o
maior e qual é o menor'''
import math

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

list = [n1, n2, n3]
max = max(list)
print(max)
min = min(list)
print(min)


print('Vamos descobrir qual é o maior valor:')
maior = n3
if (n1 > n2 and n1 > n3):
    print('O primeiro valor é maior')
if (n2 > n1 and n2 > n3):
    print('O segundo valor é maior')

print('Vamos descobrir qual é o maior valor:')
menor = n3
if (n1 < n2 and n1 < n3):
    print('O primeiro valor é menor')
if (n2 < n1 and n2 < n3):
    print('O segundo valor é menor')

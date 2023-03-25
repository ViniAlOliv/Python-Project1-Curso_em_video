#Desafio 9: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

valor = int(input('Digite um valor: '))

#Do jeito simples
print('{} x {} = {}'.format(valor, 1, valor*1))
print('{} x {} = {}'.format(valor, 2, valor*2))
print('{} x {} = {}'.format(valor, 3, valor*3))
print('{} x {} = {}'.format(valor, 4, valor*4))
print('{} x {} = {}'.format(valor, 5, valor*5))
print('{} x {} = {}'.format(valor, 6, valor*6))
print('{} x {} = {}'.format(valor, 7, valor*7))
print('{} x {} = {}'.format(valor, 8, valor*8))
print('{} x {} = {}'.format(valor, 9, valor*9))
print('{} x {} = {}'.format(valor, 10, valor*10))
print('-'*20)
#De um jeito único
print('Tabuada de {0}:\n{0}x1 = {1}\n{0}x2 = {2}\n{0}x3 = {3}\n{0}x4 = {4}\n{0}x5 = {5}\n{0}x6 = {6}\n{0}x7 = {7}\n{0}x8 = {8}\n{0}x9 = {9}\n{0}x10 = {10}'.format(valor, valor*1, valor*2, valor*3, valor*4, valor*5, valor*6, valor*7, valor*8, valor*9, valor*10))
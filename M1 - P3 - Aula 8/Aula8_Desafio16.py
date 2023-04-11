#Exercício 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
#Exemplo:
#Digite um número: 6.127
#O número 6.127 tem a parte inteira 6

import math
num = float(input('Digite um valor: '))
print(num)
print('O número é {}'.format(math.trunc(num)))
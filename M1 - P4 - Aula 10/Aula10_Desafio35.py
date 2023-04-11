'''Escreva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo'''
r1 = int(input('Digite o primeiro valor: '))
r2 = int(input('Digite o segundo valor: '))
r3 = int(input('Digite o terceiro valor: '))
print('-='*20)
print('Analisador de triângulos')
print('-='*20)

if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('É possível fazer um triângulo')
else:
    print('Não é possível fazer um triângulo')
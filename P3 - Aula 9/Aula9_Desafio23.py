#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Ex: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

valor = int(input('Digite um valor: '))
'''valorSep = ' '.join(valor)
print(valorSep.split())
valorInt = int(valorSep)
print(valorInt)'''
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
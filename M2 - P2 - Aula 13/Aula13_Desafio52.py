#Faça um programa que leia um número inteiro e diga se é ou não um número primo

primo = int(input('Digite um número e eu validarei se ele é primo: '))
tot = 0
for c in range (1, primo+1):
    if (primo % c == 0):
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[33m', end=' ')  
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisível {} vezes'. format(primo, tot))

if (tot == 2):
    print('Este é um número primo')
else:
    print('Este não é um número primo')
'''
if (primo % 1 == 0) and (primo % primo == 0):
    for cont in range(3,17,2):
        if (primo % cont == 0):
            print("Este é um número primo")
        else:
            print("Não é primo")
'''
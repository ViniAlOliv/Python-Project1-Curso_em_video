#Faça um programa que leia o SEXO de uma pessoa, mas só aceite valores
# M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto
n = ''
while (n != 'M') and (n != 'F'):
    n = str(input('Digite seu sexo sendo [F] ou [M]: ')).strip().upper()[0]
    print(n)
print('End')

'''
Gustavo Guanabara way
sexo = str(input('Informe seu sexo [M / F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
'''
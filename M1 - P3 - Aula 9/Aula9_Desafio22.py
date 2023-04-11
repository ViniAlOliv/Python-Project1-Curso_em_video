#Crie um programa que mostre o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Nome completo: ')).strip()
print('Seu nome maiúsculo é {}'.format(nome.upper()))
print('Seu nome miúsculo é {}'.format(nome.lower()))
#Tive problema no strip e no contador removendo os espaços. Que podemos ver abaixo
#Incluí .strip no nome acima
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome {} letras'.format(nome.find(' ')))
print('Ou...')
print('O seu primeiro nome {} e tem {} letras'.format(separa[0], len(separa[0])))
#Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro: Ana
#Último: Souza

nome = str(input('Digite seu nome completo: ')).lower().title().strip().split()
print('O primeiro nome é: {}'.format(nome[0]))
print('O último nome é: {}'.format(nome[len(nome)-1]))


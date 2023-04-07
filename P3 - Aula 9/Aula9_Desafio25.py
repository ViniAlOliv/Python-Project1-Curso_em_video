#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
nome = (str(input('Diga o nome completo: ')).strip().lower())
title = nome.title()
silva = 'Silva' in title
print('O resultado é: {}'.format(silva))

'''O Gustavo Guanabara resolveu da seguinte forma:
nome = (str(input('Diga o nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
'''

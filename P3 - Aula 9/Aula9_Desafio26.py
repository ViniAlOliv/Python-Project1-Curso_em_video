#Faça um programa que leia uma frase pelo teclado e mostre
#Quantas vezes aparece a letra "a"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece na última vez

frase = str(input('Escreva uma frase: ')).lower().strip()
print(len(frase))
print('A letra "a" apareceu {} vezes na frase'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na {} posição'.format(frase.find('a')+1))
print('A letra "a" aparece pela última vez na {} posição'.format(frase.rfind('a')+1))
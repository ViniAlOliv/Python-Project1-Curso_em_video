''' Escreva um programa que faça o computador pensar em um número
inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número
escolhido pelo computador.

O programa deve escrever para o usuário se o mesmo venceu ou perdeu
'''

import random

numero = random.randint(0,5)
perg = int(input('Diga um número de 0 a 5: '))
if (perg == numero):
    print('Você acertou! Disse {} e era {}'.format(perg, numero))
else:
    print('Você errou,  Disse {} e era {}'.format(perg, numero))
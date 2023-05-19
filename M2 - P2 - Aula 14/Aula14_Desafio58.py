#Melhore o jogo 28 onde o computador vai "pensar" em um número entre
# 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer
#OBS: Agora tenho várias chances até acertar

'''Código antigo
import random

numero = random.randint(0,5)
perg = int(input('Diga um número de 0 a 5: '))
if (perg == numero):
    print('Você acertou! Disse {} e era {}'.format(perg, numero))
else:
    print('Você errou,  Disse {} e era {}'.format(perg, numero))
'''


#Melhore o jogo 28 onde o computador vai "pensar" em um número entre
# 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer
#OBS: Agora tenho várias chances até acertar

import random
palp = 0
perg = 11
numero = random.randint(0,10)
while (perg != numero):
    perg = int(input('Diga um número de 0 a 10: '))
    if (perg < 0) or (perg > 10):
        print('Número fora do range de valores. Digite novamente')
    elif (perg > numero):
        print('É menor...Você errou, tente novamente')
    elif (perg < numero):
        print('É maior...Você errou, tente novamente')
    palp = palp + 1
    
print('Você acertou. O número era {} e você precisou de {} palpites para acertar'.format(numero,palp))
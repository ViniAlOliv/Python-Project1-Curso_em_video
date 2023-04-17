#Crie um programa que faça o computador jogar Jokenpô com você
'''
Dizer as regras

'''
import random

jog1 = int(input('Escolha uma opção abaixo:\n 1) Pedra\n 2) Papel\n 3) Tesoura\n Qual das três opções você escolhe: '))
print('-='*20)
if (jog1 == 1):
    optJog1 = 'Pedra'
elif (jog1 == 2):
    optJog1 = 'Papel'
elif (jog1 == 3):
    optJog1 = 'Tesoura'
print('O jogador 1 escolheu a opção {}) {}'.format(jog1, optJog1))
jog2 = random.randint(1,3)
if (jog2 == 1):
    optJog2 = 'Pedra'
elif (jog2 == 2):
    optJog2 = 'Papel'
elif (jog2 == 3):
    optJog2 = 'Tesoura'
print('O jogador 2(PC) escolheu a opção {}) {}'.format(jog2, optJog2))
print('-='*20)
if (jog1 == jog2):
    print('Opa, {} x {} é empate! Tentem novamente!'.format(optJog1, optJog2))
elif (jog1 == 1 and jog2 == 2):
    print('Opa, {} x {} o jogador 2 vence!'.format(optJog1, optJog2))
elif (jog1 == 1 and jog2 == 3):
    print('Opa, {} x {} o jogador 1 vence!'.format(optJog1, optJog2))
elif (jog1 == 2 and jog2 == 1):
    print('Opa, {} x {} o jogador 1 vence!'.format(optJog1, optJog2))
elif (jog1 == 2 and jog2 == 3):
    print('Opa, {} x {} o jogador 2 vence!'.format(optJog1, optJog2))
elif (jog1 == 3 and jog2 == 1):
    print('Opa, {} x {} o jogador 2 vence!'.format(optJog1, optJog2))
elif (jog1 == 3 and jog2 == 2):
    print('Opa, {} x {} o jogador 1 vence!'.format(optJog1, optJog2))
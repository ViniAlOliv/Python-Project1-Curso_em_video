'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido 
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
'''
import random
opcao = 0
jogador = 0
computador = 0
vitoria = 0
derrota = 0
parImpar = 0
resposta = 0

while derrota == 0:
    opcao = int(input('Escolha sua opção:[1]Par e [2]Ímpar: '))
    while opcao < 1 or opcao > 2:
        opcao = int(input('Opção não existe. Escolha sua opção:[1]Par e [2]Ímpar: '))
    if opcao == 1:
        print('Opção do jogador: 1 - PAR')
    elif opcao == 2:
        print('Opção do jogador: 2 - ÍMPAR')
    
    jogador = int(input('Selecione um número de 0 a 10 para brincar de par ou ímpar: '))
    computador = random.randint(0,10)
    parImpar = jogador + computador
    print(f'Você escolheu {jogador} e o computador escolheu {computador}. A soma é {parImpar}')
    
    if parImpar %2 != 0:
        resposta = 2
        print('O resultado é ÍMPAR')
    elif parImpar %2 == 0:
        resposta = 1
        print('O resultado é PAR')
        
    if resposta == opcao:
        print('Você venceu!')
        vitoria = vitoria + 1
    elif resposta != opcao:
        print('Você perdeu')
        derrota = derrota + 1
    print('=-'*15)
    if derrota == 1:
        break
if vitoria == 0:
    print(f'Hey jogador, você não venceu a máquina 1 vez sequer. Que pena! =/')
elif vitoria == 1:
    print(f'Hey jogador, você venceu a máquina 1 vez!')
else:
    print(f'Hey jogador, você venceu a máquina {vitoria} vez(es) consecutiva(s)!')
    


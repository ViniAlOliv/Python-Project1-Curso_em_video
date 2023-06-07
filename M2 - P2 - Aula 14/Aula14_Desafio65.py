#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual
#foi o maior e o menor valores lidos. O programa deve perguntar ao
#usuário se ele quer ou não continuar a digitar valores
n = 0
soma = 0
media = 0
qt = 0
maior = 0
menor = 10000
resposta = 'S'

while resposta == 'Ss':
    n = int(input('Digite um valor: '))
    print('=-'*15)
    soma = soma + n
    media = media + 1
    qt = media
    if (n > maior):
        maior = n
    if (n < menor):
        menor = n
    resposta = str(input('Quer continuar digitando valores?\n(S)Sim\n(N)Não\n->')).upper().strip(0)[0]
print('Fim')
print('você digitou {} números e a média foi de {}.\nO maior valor lido foi {} e o menor valor lido foi {}'.format(qt,soma/media,maior,menor))
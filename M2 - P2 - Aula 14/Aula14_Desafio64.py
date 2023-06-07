#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números
#foram digitados e qual foi a soma entre eles (desconsiderando o
# flag)
n = 0
totalNum = 0
soma = 0

while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    if (n == 999):
        print()
    elif (n != 999):
        totalNum = totalNum + 1
        soma = soma + n
print('FIM')
print('O total de números digitados foi de {} e a soma entre eles foi {}'.format(totalNum, soma))
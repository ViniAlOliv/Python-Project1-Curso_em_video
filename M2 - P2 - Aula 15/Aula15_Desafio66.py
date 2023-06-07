'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário 
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando a flag) 
'''
n = qt = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    qt = qt + 1
    soma = soma + n
print(f'A quantidade de números foi de {qt} e a soma entre eles resultou em {soma}')
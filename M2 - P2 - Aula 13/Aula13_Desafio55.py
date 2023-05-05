#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos
maiorPeso = 0
menorPeso = 1000
for pessoa in range (1, 5 + 1):
    peso = float(input('Pessoa {} diga seu peso: '.format(pessoa)))
    if (peso > maiorPeso):
        maiorPeso = peso
    elif (peso < menorPeso):
        menorPeso = peso
print('=/'*12)
print('O maior peso foi de: {}'.format(maiorPeso))
print('O menor peso foi de: {}'.format(menorPeso))
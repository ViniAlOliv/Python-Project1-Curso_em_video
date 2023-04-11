#Desafio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (Considerar U$$1,00 = R$3,27)

qtDinheiro = float(input('Quanto você tem na carteira: R$254.69'))
print('Ora, você tem R${} reais, então conseguirá comprar somente US${:.2f} dólares'.format(qtDinheiro, qtDinheiro/3.27))
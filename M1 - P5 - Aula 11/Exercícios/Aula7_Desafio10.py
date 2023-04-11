#Desafio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (Considerar U$$1,00 = R$3,27)

qtDinheiro = float(input('Quanto você tem na carteira: R$'))
print('Ora, você tem \033[32mR${}\033[m reais, então conseguirá comprar somente \033[34mUS${:.2f}\033[m dólares'.format(qtDinheiro, qtDinheiro/3.27))
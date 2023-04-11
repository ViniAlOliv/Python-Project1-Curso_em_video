'''Escreva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200km e R$0,45 para viagens mais longas
'''
kmViagem = int(input('Quantos km terá a viagem: '))
if (kmViagem <= 200):
    print('Você irá pagar somente R$0,50 por Km viajado. O valor será de R${}! '.format(kmViagem * 0.50))
else:
    print('Você irá pagar somente R$0,45 por Km viajado. O valor será de R${}! '.format(kmViagem * 0.45))


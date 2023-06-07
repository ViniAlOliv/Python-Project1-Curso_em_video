'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000,00
C) Qual é o nome do produto mais barato
'''
produtoNome = ''
preco = 0
valorTotal = 0
continua = 0
nomeProdutoBarato = ''
precoMaisBarato = 10000000
produtosMilhas = 0

print('=-'*15)
print('Mercadin São Juaquim')
print('=-'*15)
while True:
    produtoNome = str(input('Nome do produto desejado: '))
    preco = float(input('Digite o preço: R$'))
    valorTotal = valorTotal + preco
    if preco < precoMaisBarato:
        precoMaisBarato = preco
        nomeProdutoBarato = produtoNome
    if preco > 1000:
        produtosMilhas = produtosMilhas + 1
    
    continua = int(input('Deseja continuar comprando? [1]S ou [2]Não -> '))
    if continua == 2:
        break
    elif continua < 1 or continua > 2:
        continua = int(input('Esse valor não existe. Deseja continuar comprando? [1]S ou [2]Não -> '))
    print('=-'*15)
print('=-'*15)
print('Fim da compra')
print(f'O total gasto na compra foi de R${valorTotal:.2f}')
print(f'Temos ao todo {produtosMilhas} produtos que custam mais de R$1000,00')
print(f'O produto mais barato é o {nomeProdutoBarato} que custa R${precoMaisBarato:.2f}')
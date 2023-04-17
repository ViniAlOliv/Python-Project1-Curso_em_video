#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu Preço normal e Condição de Pagamento:
'''
- À vista -> Dinheiro/Cheque -> 10% de desconto
- À vista -> Cartão -> 5% de desconto
- Em até 2x no cartão -> Preço normal
- 3x ou mais no cartão -> 20% de juros
'''

preco = float(input('Qual é o preço do produto: '))
print('Você pode fazer o pagamento:\n1) À vista -> Dinheiro/Cheque -> 10 por cento de desconto\n2) À vista -> Cartão -> 5 por cento de desconto\n3) Em até 2x no cartão -> Preço normal\n4) 3x ou mais no cartão -> 20 por cento de juros')
formaPag = int(input('Qual será a forma de pagamento: '))
if  (formaPag == 1):
    print('À vista em dinheiro/Cheque! Você pagará somente R${}'.format(preco - (preco * 0.1)))
elif (formaPag == 2):
    print('À vista no Cartão! Você pagará somente R${}'.format(preco - (preco * 0.05)))
elif (formaPag == 3):
    print('2x no cartão! Pagará o preço normal de R${:.2f} em duas parcelas de R${:.2f}'.format(preco, preco / 2))
elif (formaPag == 4):
    print('3x ou mais no cartão! Pagará com juros um valor total de R${:.2f}'.format(preco + (preco * 0.2)))
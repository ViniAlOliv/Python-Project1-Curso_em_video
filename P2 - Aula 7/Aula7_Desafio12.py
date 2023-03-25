#Desafio 12: Mostre um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

precoNormal = float(input('Qual é o preço do produto: R$'))
print('Opa, esse produto está em promoção e está saindo por R${} reais'.format(precoNormal - ((precoNormal * 5) / 100)))

precoDesconto = (precoNormal - ((precoNormal * 5) / 100))
print('Opa, esse produto está com desconto e está saindo por R${} reais'.format(precoDesconto))
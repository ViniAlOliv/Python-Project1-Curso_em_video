#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar:
# O valor da casa
# O salário do comprador
# Em quantos anos ele vai pagar

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print('Olá, tudo bem? Você quer comprar uma casa conosco:')
casaValor = float(input('Qual é o valor da casa: R$'))
salarioComprador = float(input('Quanto o comprador ganha por mês: R$'))
anosAPagar = int(input('Durante quantos anos irá pagar: '))

prestacaoMensal = casaValor / (anosAPagar * 12)
print('Prestação Mensal: R$ {:.2f}'.format(prestacaoMensal))

parteSalario = salarioComprador * 0.3
print('30 por cento do salário R${} é R${}'.format(salarioComprador, parteSalario))

if (prestacaoMensal > parteSalario):
    print('Infelizmente o empréstimo será negado.')
#elif (prestacaoMensal <= parteSalario):
#    print('Você pode adquirir o empréstimo. Parabéns!')
else:
    print('Você pode adquirir o empréstimo. Parabéns!')
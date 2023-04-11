#Desafio 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salarioAtual = float(input('Qual é o seu salário atual: R$'))
valorAumento = (salarioAtual * 15) / 100
print('O seu salário de R${} com mais 15% de aumento, então R${} agora passará a ser de RS{}'.format(salarioAtual, valorAumento, salarioAtual + valorAumento))
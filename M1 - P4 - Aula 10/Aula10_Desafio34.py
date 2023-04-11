'''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento

Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais o aumento é de 15%
'''
salario = float(input('Digite o seu salário: '))
print('O salário tem o valor de R${}'.format(salario))
if (salario <= 1250.00):
    print('Você terá um aumento de 15%. Seu salário passará a ser de R${:.2f}!'.format((salario * 0.15) + salario))
else:
    print('Você terá um aumento de 10%. Seu salário passará a ser de R${:.2f}!'.format((salario * 0.10) + salario))
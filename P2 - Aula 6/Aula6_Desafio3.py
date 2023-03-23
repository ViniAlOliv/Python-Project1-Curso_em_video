#Crie um programa que leia dois números e mostre a soma entre eles:
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
soma = n1 + n2
print('A soma entre {0} e {1} é: {2}'.format(n1, n2, soma))

print('')
print('')
#Crie outras coisas que faça leitura...
anoatual = int(input('Ano atual: '))
idade = int(input('Sua idade atual: '))
anoNasc = anoatual - idade
print('O ano atual é {0} e idade {1}, então nasceu no ano de {2}'.format(anoatual, idade, anoNasc))


#Conta de restaurante
qtPessoas = int(input('Quantidade de pessoas que foram jantar:'))
valorConta = float(input('Valor da conta: '))
valor = valorConta / qtPessoas
print('A conta deu R${0}. Para {1} pessoa/s ficou dividido em R${2} para cada pessoa'.format(valorConta, qtPessoas, valor))


#
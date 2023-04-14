#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
#1 para Binário
#2 para Octal
#3 para hexadecimal

numero = int(input('Escreva um número inteiro: '))
print('Selecione um conversor: \n [1] Binário\n [2] Octal\n [3] Hexadecimal')
conversao = int(input('Escolha um dos números: '))

if (conversao == 1):
    print('O valor {} convertido para binário é igual a {}'.format(numero, format(numero, "b")))
elif (conversao == 2):
    print('O valor {} convertido para octal é igual a {}'.format(numero, format(numero, "o")))
elif (conversao == 3):
    print('O valor {} convertido para hexadecimal é igual a {}'.format(numero, format(numero, "x")))
else:
    print('O devido valor incluso não foi encontrado. Tente novamente')
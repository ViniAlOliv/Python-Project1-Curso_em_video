#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares 
#Se o valor digitado for ímpar, desconsidere-o
lista = 0
soma = 0
for cont in range(1,6+1):
    dado = int(input('Diga o valor {}: '.format(cont)))
    if (dado%2 ==0):
        lista = lista + dado
        soma = soma + 1
if (soma == 0):
    print('Você não informou nenhum número par')
elif (soma == 1):
    print('Você informou somente 1 valor par, sendo esse o {}'.format(lista))
else:
    print('A soma dos {} valores encontrados foi de {}'.format(soma, lista))
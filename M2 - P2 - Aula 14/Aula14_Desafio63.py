#Escreva um programa que leia um número N inteiro qualquer e
#mostre na tela os N primeiros elementos de uma sequência de Fibonacci
#Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
n = int(input('Quantos elementos de Fibonacci você quer ver: '))
elemento = 0
elementoB = 0
termo = 0
qt = 0
while qt != n:
    if (qt == 0):
        print('{}'.format(elemento), end=' -> ')
        elemento = elemento + 1
        qt = qt + 1
    elif (qt > 0):
        print('{}'.format(elemento), end=' -> ')
        termo = elemento + elementoB
        elementoB = elemento
        elemento = termo
        qt = qt + 1
print('FIM')

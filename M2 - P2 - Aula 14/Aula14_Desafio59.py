#Crie um programa que leia dois valores e mostre um menu na tela:
'''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do Programa

Seu programa deverá realizar a operação solicitada em cada caso
'''
opt = 0
n1 = int(input('Digite um primeiro valor: '))
n2 = int(input('Digite um segundo valor: '))
while (opt != 5):
    opt = int(input('O que gostaria de fazer com os valores:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do Programa\nDigite aqui: '))
    if (opt == 1):
        print('Opção [1]: A soma de {} + {} é {}'.format(n1,n2,n1 + n2))
        print('=+'*12)
    elif (opt == 2):
        print('Opção [2]: A multiplicação de {} x {} é {}'.format(n1,n2,n1 * n2))
        print('=+'*12)
    elif (opt == 3):
        print('Primeiro valor: {}'.format(n1))
        print('Segundo valor: {}'.format(n2))
        if (n1 > n2):
            print('Opção [3]: O maior é o {}'.format(n1))
            print('=+'*12)
        elif (n2 > n1):
            print('Opção [3]: O maior e o {}'.format(n2))
            print('=+'*12)
        elif (n1 == n2):
            print('Os dois são iguais')
            print('=+'*12)
    elif (opt == 4):
        print('Recebendo novos valores:')
        n1 = int(input('Digite um primeiro valor: '))
        n2 = int(input('Digite um segundo valor: '))
        print('=+'*12)
    elif (opt == 5):
        print('Saindo do programa...')
    else:
        print('Valor incorreto, digite novamente')
        print('=+'*12)    
print('Fim')
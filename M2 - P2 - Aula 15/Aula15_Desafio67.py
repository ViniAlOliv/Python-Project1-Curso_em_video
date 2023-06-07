'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo
'''
n = 0
conta = 1

while n >= 0:
    print('==='*15)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('==='*15)
    if n < 0:
        break
    if conta > 10:
        conta = 1
    while conta <= 10:
        print(f'{n} x {conta} = {n*conta}')
        conta = conta + 1
print(f'Opa, o valor {n} é negativo. Encerro aqui a tabuada')


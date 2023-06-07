'''
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (numero inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS: COnsidere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
valorSacado = 0
total = 0
ced = 50
totalCed = 0

print('==='*10)
print('   BANCO RICO   ')
print('==='*10)

valorSacado = int(input('Que valor você quer sacar? R$'))
total = valorSacado
while True:
    if total >= ced:
        total = total - ced
        totalCed = totalCed + 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} cédulas de {ced}')
        
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        
        if total == 0:
            break
            
print('==='*10)
print('Volte Sempre!!')
print('==='*10)

#Faça um programa que leia um número qualquer e mostre seu fatorial:
# Ex: 5! = 5x4x3x2x1 = 120
n = int(input('Digite um número e eu digo seu fatorial !: '))
res = n
print('Fatorial de {}!: {} x '.format(n, n), end='')
while n - 1 != 0:
    res = res * (n - 1)
    n = n - 1
    print('{}'.format(n),end='')
    print(' x ' if n > 1 else ' = ', end='')
print(res)
    
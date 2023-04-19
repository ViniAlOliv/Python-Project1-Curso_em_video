#Aula 13 - Estrutura de Repetição FOR
'''
for c in range(1,10):
	passo
pega
'''
#Aula prática
#Oi
for c in range(1, 6):
    print('Oi')
print('FIM')
print('-='*20)

#Contar para trás
for c in range(6, 0, -1):
    print(c)
print('FIM')
print('-='*20)

#Pular de dois em dois
for c in range(0, 7, 2):
    print(c)
print('FIM')
print('-='*20)

# Recebendo input
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print (c)
print('Fim')
print('-='*20)
print('')

#Controlando todas as entradas
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')
print('-='*20)
print('')

#Comando dentro de FOR
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')
print('-='*20)
print('')
#Vai pedir valor 3 vezes

#Soma de valores passados
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
print('-='*20)
print('')

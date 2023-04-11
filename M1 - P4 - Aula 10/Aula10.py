#CONDIÇÕES

'''Condições simples e compostas
Estrutura sequencial
- Estrutura de código em sequência

Como representar uma condição:
if objeto.metodo():
    codigo
else:
    codigo
'''
#Exemplos:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

#No Python, exclusivamente, conseguimos reduzir esse código 
# e vale muito a pena quando o mesmo é pequeno:
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')

#Exercício 1
nome = str(input('Qual é o seu nome? '))
if nome == 'Vinicius':
    print('Que nome lindão')
else:
    print('Hum, nome diferente do meu dono...')
print('Bom dia, {}!'.format(nome))

#Exercício 2
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi de {}!'.format(m))
if m <= 0:
    print('A nota passada está errada')
else:
    if m >= 6.0:
        print('Sua média foi boa, parabéns!')
    else:
        print('Sua média foi ruim. Estude mais!')
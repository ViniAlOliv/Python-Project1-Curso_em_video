# Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
'''
- Equilátero -> Todos os lados iguais
- Isóceles -> Dois lados iguais
- Escaleno -> Todos os lados diferentes
'''

r1 = int(input('Digite o primeiro valor: '))
r2 = int(input('Digite o segundo valor: '))
r3 = int(input('Digite o terceiro valor: '))
print('-='*20)
print('Analisador de triângulos')
print('-='*20)

if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('É possível fazer um triângulo')
    if (r1 == r2 and r2 == r3 and r1 == r3):
        print('Você tem um triângulo Equilátero -> Todos os lados iguais')
    elif (r1 == r2 or r2 == r3 or r1 == r3):
        print('Você tem um triângulo Isóceles -> Dois lados iguais')
    elif (r1 != r2 and r2 != r3 and r1 != r3):
        print('Você tem um triângulo Escaleno -> Todos os lados diferentes')
else:
    print('Não é possível fazer um triângulo')
print('-='*20)


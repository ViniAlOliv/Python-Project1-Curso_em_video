#Refaça o desafio 9, de tabuada, mostrando de um número que o usuário escolher, só que
# agora utilizando um laço for
valor = int(input('Escreva um número para eu contar a tabuada dele de 1 a 10: '))
print('-='*5)
print('Tabuada')
print('-='*5)
for num in range(1,10+1):
    print('{} x {} = {}'.format(num, valor, num*valor))
print('Fim')
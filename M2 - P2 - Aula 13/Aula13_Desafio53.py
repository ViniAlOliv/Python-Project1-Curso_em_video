#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
#Ex: Arara, apos a sopa, a sacada da casa, anotaram a data da maratona
frase = str(input('Digite uma frase: '))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if (inverso == junto):
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

'''print('Você digitou a frase {}'.format(palavras))'''
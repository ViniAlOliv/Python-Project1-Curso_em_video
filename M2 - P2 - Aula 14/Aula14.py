#Estrutura de repetição WHILE
'''A estrutura é o ENQUANTO → Estrutura de repetição com teste lógico

Quando não sei o limite podemos utilizar o WHILE, na qual informa 
o “Enquanto não acontecer algo, eu continuo fazendo”'''

for c in range(1, 10+1):
    print(c)
print('fim')

#Com while
c = 1
while c < 10:
    print(c)
    c = c + 1
print(c)

print("")
print("=-=-=-=-=-=-")
print("")
print("=-=-=-=-=-=-")

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

print("=-=-=-=-=-=-")
print("")
print("=-=-=-=-=-=-")

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')

print("=-=-=-=-=-=-")
print("")
print("=-=-=-=-=-=-")

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if (n != 0):    
        if (n % 2 == 0):
            par += 1
        else:
            impar += 1
print('Foram selecionados {} nº pares e {} nº ímpares'.format(par,impar))
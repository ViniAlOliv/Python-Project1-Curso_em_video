'''Aula 15 - Interrompendo repetições While
No Python somente existe o For e o While, mas é possível simular o DO While, que é o caso dessa aula.

O DO tem o teste lógico no início, enquanto o WHILE tem o teste lógico no fim.

Quando temos o laço de repetição e algo no laço foi realizado não sendo necessário repeti-lo, inserimos no WHILE o comando break
'''
#Exemplo 1
'''cont = 1
while cont <= 10:
    print(cont, '', end='')
    cont += 1
print('Acabou')'''

#Se eu colocar o while acima como True, o sistema vai fazer infinitamente o comando. Como no exemplo a seguir:
'''cont = 1
while True:
    print(cont, '', end='')
    cont += 1
print('Acabou')'''

#Para que eu consiga parar o comando sem gambiarra, utilizo o break
n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break    
    s = s + n
print(f'A soma vale {s}')
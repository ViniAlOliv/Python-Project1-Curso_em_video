#Desenvolva um programa que leia o primeiro termo e a razão de uma P(Progressão aritmética). 
# No final, mostre os 10 primeiros termos dessa progressão

aUm = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
decimo = aUm + (10 -1) * razao

print("=="*10)
print("   10 termos de uma PA   ")
print("=="*10)

for c in range(aUm,decimo + razao,razao):
    print('{} '.format(c), end=' -> ')
print('Acabou')

#An = A1 + (N-1).R
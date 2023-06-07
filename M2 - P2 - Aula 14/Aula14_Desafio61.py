#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while

#Atv 61
aUm = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
termo = aUm
qt = 0

print("=="*20)
print("   10 termos de uma PA   ")
print("=="*20)

while qt != 10:
    print('{} '.format(termo), end=' -> ')
    termo = termo + razao
    qt = qt + 1
print('Acabou')    
#Escreva um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
'''
- Se ele vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
'''
anoNasc = int(input('Diga o ano de seu nascimento: '))
anoAtual = 2023

idade = anoAtual - anoNasc
print('Você tem {} anos!'.format(idade))
if (idade > 18):
    print('Opa, já passou o tempo de alistamento')
elif (idade == 18):
    print('Está na hora de se alistar!')
else:
    print('Você ainda não tem idade para se alistar')

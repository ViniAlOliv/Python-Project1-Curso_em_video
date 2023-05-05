#Crie o programa que leia o ano de nascimento de 7 pessoas
#Mostre quantas pessoas são maiores de idade e quantas não são
#Considere maioridade com 21 anos
from datetime import date
mId = 0
menId = 0
anoAtual = date.today().year

for pessoa in range (1,7 + 1):
    anoNasc = int(input('Diga o ano de nascimento da pessoa {}: '.format(pessoa)))
    if (anoAtual - anoNasc >= 21 ):
        mId = mId + 1
    elif (anoAtual - anoNasc < 21 and anoAtual - anoNasc > 0):
        menId = menId + 1
    else:
        print('Idade não contada pois é menor ou igual a zero')
print('='*20)
print('Maiores de idade: {}'.format(mId))
print('Menores de idade: {}'. format(menId))
print('='*20)
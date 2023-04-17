#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
'''
- Até 9 anos -> Mirim
- Até 14 anos -> Infantil
- Até 19 anos -> Junior
- Até 20 anos -> Senior
- Acima -> Master
'''

anoNasc = int(input('Diga o ano de seu nascimento: '))
idade = 2023 - anoNasc
print('Você tem {} anos'.format(idade))
if (idade <= 9):
    print('Você é da categoria Mirim')
elif (idade > 9 and idade <= 14):
    print('Você é da categoria Infantil')
elif (idade > 14 and idade <= 19):
    print('Você é da categoria Junior')
elif (idade > 19 and idade <= 20):
    print('Você é da categoria Senior')
else:
    print('Você é da categoria Master')
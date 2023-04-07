#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'
cidade = str(input('Diga o nome de uma cidade: ')).strip().upper()
separa = cidade.split()
santo = 'SANTO' in separa[0]
#santo = 'SANTO' in upper
print(santo)


'''O gustavo guanabara resolveu da seguinte forma:
cidade = str(input('Diga o nome de uma cidade: ')).strip()
print(cid[:5].upper()) == 'SANTO'

'''
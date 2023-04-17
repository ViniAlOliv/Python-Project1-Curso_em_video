#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
'''
- Média abaixo de 5.0 -> Reprovado
- Média entre 5.0 e 6.9 -> Recuperação
- Média 7.0 ou superior -> Aprovado
'''
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2
print('Sua média é: {}'.format(media))

if (media < 5):
    print('Você está reprovado!')
elif (media >= 5 and media <= 6.9):
    print('Você está de recuperação')
else:
    print('Você foi aprovado, parabéns!')
#Desenvolva um programa que leia o Nome, Idade e Sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo
#Qual o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos
somaIdade = 0
idMaisVelho = 0
qtMulheres = 0

for pessoa in range (1, 4 + 1):
    print('*******Pessoa {}*******'.format(pessoa))
    nome = str(input('Diga seu nome: '))
    idade = int(input('Diga sua idade: '))
    sexo = str(input('Diga seu sexo (Masc) ou (Fem): '))

    somaIdade = idade + somaIdade
    if (sexo == 'Masc' and idade > idMaisVelho):
        idMaisVelho = idade
        nomeMaisVelho = nome
    
    if (sexo == 'Fem' and idade < 20):
        qtMulheres = qtMulheres + 1
        
print('=-=-'*13)
print('A média de idade é: {}'.format(somaIdade/4))
print('O nome do home mais velho é {}'.format(nomeMaisVelho))
print('Mulheres com menos de 20 anos: {}'.format(qtMulheres))
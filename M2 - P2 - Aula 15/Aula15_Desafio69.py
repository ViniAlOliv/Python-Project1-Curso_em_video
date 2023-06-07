'''
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos 
'''

idade = maiorIdade = qtMulheres = sexo = masc = opcao = 0

while opcao != 2:
    print('=-'*15)
    idade = int(input('Digite a sua idade: '))
    if idade >= 18:
        maiorIdade = maiorIdade + 1
    
    sexo = int(input('Digite seu sexo:[1]F ou [2]M: ').strip().upper()[0])
    if sexo == 2:
        masc = masc + 1
    elif sexo == 1 and idade < 20:
        qtMulheres = qtMulheres + 1
    elif sexo < 1 or sexo > 2:
        sexo = int(input('Digite novamente seu sexo:[1]F ou [2]M: ').strip().upper()[0])    
    
    opcao = int(input('Deseja continuar cadastrando [1]Sim e [2]Não: '))
    if opcao == 2:
        break
    print('=-'*15)
print('=-'*15)
print(f'Temos nesse grupo {maiorIdade} pessoa(s) com 18 anos ou mais')
print(f'De todas as pessoas cadastradas, temos {masc} homens')
print(f'Nesse grupo cadastrado temos {qtMulheres} mulher(es) com menos de 20 anos')

    

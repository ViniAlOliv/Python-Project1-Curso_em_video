#Desafio 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nome = input('Nome do aluno: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = float((nota1 + nota2) /2)

print('O aluno {} teve: \nResultado 1: {} \nResultado 2: {} \nSua média foi de: {}'.format(nome, nota1, nota2, media))

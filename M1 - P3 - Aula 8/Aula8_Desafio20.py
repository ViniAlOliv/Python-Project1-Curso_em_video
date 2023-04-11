#Exercício 20: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random

grupo1 = str(input('Nome do grupo 1: '))
grupo2 = str(input('Nome do grupo 2: '))
grupo3 = str(input('Nome do grupo 3: '))
grupo4 = str(input('Nome do grupo 4: '))
list = [grupo1, grupo2, grupo3, grupo4]
random.shuffle(list)
print('Esta é a ordem dos grupos: ')
print(list)
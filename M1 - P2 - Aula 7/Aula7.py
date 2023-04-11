#Operadores aritméticos

# Adição → +
# Subtração → -
# Multiplicação → *
# Divisão → /
# Potência → **
# Divisão inteira → //
# Resto de divisão → %


#Ordem de precedência
#1 -> ()
#2 -> **
#3 ->  * / // %
#4 -> + e -


#Exercícios
#n1 = str(oi)
#n2 = int(8)
print('Oi' * 7)

#Podemos fazer uma soma sem variável de soma. Exemplo:
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma vale {}!'.format(n1+n2))


#Colocando casas decimais...
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))


#Atividades e desafios:

#Desafio 5: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

#Desafio 6: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

#Desafio 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

#Desafio 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

#Desafio 9: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

#Desafio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (Considerar U$$1,00 = R$3,27)

#Desafio 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo
#que cada litro de tinta pinta uma área de 2m²

#Desafio 12: Mostre um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

#Desafio 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
#Desafio 6: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um valor: '))
print('O número digitado foi {}. \n O seu dobro é: {}. \n O seu triplo é: {}. \n A sua raiz quadrada é: {:.3f}'.format(n, n*2, n*3, n**(1/2)))
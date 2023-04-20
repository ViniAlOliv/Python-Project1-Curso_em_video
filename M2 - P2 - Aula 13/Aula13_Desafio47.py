#Faça um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
for num in range(2,50+1,2):
    if (num %2 == 0):
        print(num, end=' ')
print('Fim')
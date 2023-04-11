#Desafio 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = int(input('Digite um valor: '))
centimetro = float(valor * 100)
milimetro = float(valor * 1000)
quilometro = float(valor / 1000)

print('O valor é {}m \nEm centímetros é {:.0f}cm \nEm milímetros é {:.0f}mm \nEm km é {:.0f}km'.format(valor, centimetro, milimetro, quilometro))
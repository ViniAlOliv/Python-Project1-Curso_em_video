#Desafio 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo
#que cada litro de tinta pinta uma área de 2m²

largura = float(input('Quantos metros tem de largura: '))
altura = float(input('Quanto metros tem de altura: '))
pintura = (largura * altura) / 2
print('A quantidade de tinta necessária para pintar toda a parede de {}m de largura e {}m de altura é {} litro(s)'.format(largura, altura, pintura))
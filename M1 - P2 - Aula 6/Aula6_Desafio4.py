#Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo e todas as informações possíveis sobre ele:

#Experimentar todos os IS...
n = input('Digite qualquer coisa: ')

#Tipo primitivo
print('O tipo é ', type(n))

#É um número?
print(n.isnumeric())
print('É numérico? ', n.isnumeric())

#É um título?
print(n.istitle())
print('É um título? ', n.istitle())

#É um valor decimal?
print(n.isdecimal())
print('É um decimal? ', n.isdecimal())

#É minúsculo?
print(n.islower())
print('Tem letra minúscula?', n.islower())

#É printável?
print(n.isprintable())
print('É printável? ', n.isprintable())
''' Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
multado

A multa vai custar R$7,00 por cada Km acima do limite
'''
carSpeed = float(input('Digite a velocidade que o carro passou: '))
print('O carro passou a {}km/h no radar'.format(carSpeed))
if (carSpeed > 80):
    print('Você foi multado!')
    print('Irá pagar uma multa no valor de R${},00'.format((carSpeed - 80) * 7))
else:
    print('Passou de boas, isso aí. Estamos de olho.')

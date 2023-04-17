#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
'''
- Abaixo de 18.5 -> Abaixo do peso
- Entre 18.5 e 25 -> Peso ideal
- 25 até 30 -> Sobrepeso
- 30 até 40 -> Obesidade
- Acima de 40 -> Obesidade mórbida
'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura **2)
print('Seu IMC foi de {:.2f}'.format(imc))
if (imc < 18.5):
    print('Você está abaixo do peso!')
elif (imc > 18.5 and imc < 25):
    print('Você está no peso ideal!')
elif (imc > 25 and imc < 30):
    print('Você está com sobrepeso!')
elif (imc > 30 and imc < 40):
    print('Você está com obesidade!')
elif (imc > 40):
    print('Você está com obsedidade mórbida!')

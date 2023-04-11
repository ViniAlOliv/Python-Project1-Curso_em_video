#Aluguel de carros
valorDiaria = float(input('Qual o valor da diária: R$'))
valorKm = float(input('Quantos Km rodados: '))
calculoKm = (valorKm * 10) / 100
totalDia = int(input('Quantos dias com o carro: '))

print('O valor do Fiat 147 alugado por {} dias que rodou {}km é de R${}'.format(totalDia, valorKm, (valorDiaria * totalDia) + calculoKm))
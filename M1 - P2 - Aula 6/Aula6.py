#Tipos primitivos
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1+n2
#Jeitos comuns
#print(s)
#print('A soma vale ', s)
#print('A soma entre ', n1, ' e ', n2, ' vale ', s)

#Jeito aprimorado
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))


#Is numeric?
#Obs: Para saber o tipo de um dado...
n = input('Digite um valor: ')
print(n.isnumeric())

#Is alpha?
#Para saber se é um valor alfabético
n = input('Digite qualquer coisa: ')
print(n.isalpha())

#Olha todos os is... possíveis..vale a pena
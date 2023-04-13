#Condições Aninhadas
'''
Caminhos da estrada

Exercícios:
'''
nome = str(input('Qual é o seu nome? '))
cores = {'vermelho':'\033[31m','branco':'\033[m'}
if (nome == 'Vini'):
    print('Olá, {}{}{}! Seu nome é bonito'.format(cores['vermelho'], nome, cores['branco']))
elif (nome == 'Maria' or 'João'):
    print('Olá {}, seu nome é muito {}comum e bonito{}'.format( nome, cores['vermelho'], cores['branco']))
elif (nome in 'Marinua Joquina Jão Peão Xoão'):
    print('Olá {}, seu nome é muito {}doido{}'.format( nome, cores['vermelho'], cores['branco']))
else:
    print('Olá {}. Tenha um bom dia!')
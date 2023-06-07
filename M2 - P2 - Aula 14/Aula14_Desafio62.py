#Melhore  desafio 61, perguntando para o usuário mostrar 
# se ele quer mostrar mais alguns termos. O programa vai parar 
# quando o usuário disser que quer mostrar 0 termos

aUm = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
termo = aUm
qt = 0
limite = 10
termomais = 1

print("   Gerador de PA   ")
print("=="*20)
while termomais != 0:
    while (qt != limite):
        print('{} '.format(termo), end=' -> ')
        termo = termo + razao
        qt = qt + 1
        termomais = qt
    print('PAUSA')
    termomais = int(input('Quantos termos você quer mostrar a mais? -> '))
    limite = limite + termomais
print('Acabou')
print('Progressão finalizada com {} termos mostrados'.format(qt))
        
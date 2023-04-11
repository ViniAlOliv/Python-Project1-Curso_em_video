'''Manipulando texto

Nome da cadeia de caracteres: **string**

Normalmente incluído em ‘aspas simples’

Forma de atribuição de String dentro de uma variável

```python
frase = ‘Curso em vídeo Python’
```

Para saber os índices podemos contar os espaços começando por 0 (zero)

Exemplo
Ver Notion
'''
frase = 'Curso em video Python'
print(frase)
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])


#Comprimento: len()
#Para mostrar o comprimento da frase usamos o len()
print(len(frase))

#Contador de dados
print(frase.count('o'))
frase2 = 'Vinicius'
print(frase2.count('i'))

#Contagem com fatiamento
print(frase.count('o',0,13))

#Contar quantas vezes foi encontrado a palavra X
print(frase.find('deo'))
#Encontramos a posição do objeto

#Caso eu procure uma coisa que não exista:
print(frase.find('Android'))
#Valor vai ser = -1


#Para procurar de outro jeito. Usando o operador IN
print('Curso' in frase)

print('')
print('Transformação')
print('')

#Replace
print(frase.replace('Python','Android'))
#Aonde tiver Python ele substitui por Android

#Tudo maiúsculo (upper)
print(frase.upper())
#O retorno me trará a frase toda maiúscula

#Tudo minúsculo(lower)
print(frase.lower())
#O retorno me trará a frase toda minúscula. Se tiver algo minúsculo, é mantido

#Capitalize
# Vai pegar a string inteira e só colocar a primeira letra em maiúscula. O restante em minúscula
print(frase.capitalize())

#Title
#Faz o capitalize contando espaços. Ou seja, cada palavra após espaço tem sua primeira letra maiúscula
print(frase.title())

print('')
fraseNova = '   Aprenda Python  '
#Reparar nos espaços

#Strip
#Remove os espaços do início e do final de uma frase caso tenham
#Exemplo: ‘   Aprendendo Python  ‘
print(fraseNova.strip())
#O resultado será ‘Aprendendo Python’

#RStrip
#Variação à direita. Só removerá os últimos espaços
print(fraseNova.rstrip())

#LStrip
#Variação à Esquerda. Só removerá os primeiros espaços
print(fraseNova.lstrip())
#O Resultado será ‘Aprendendo Python  ’

#Split
#Vai criar uma divisão da string com base nos espaços
print(frase.split())
#Separará então em ‘[Curso][em][Video][Python]’

#Join
print('-'.join(frase))
#C-u-r-s-o- -e-m- -v-i-d-e-o- -P-y-t-h-o-n

print('')
#Let's play
print(frase[::2])

#Alguns exemplos...

from math import ceil, floor, sqrt
#import math

num = int(input('Digite um número: '))
print(num)
raiz = math.sqrt(num)
print('A raiz de {} é {}'.format(num, raiz))

#Para arredondar para cima...
print('A raiz de {} é {}'.format(num, math.ceil(raiz)))

#Para arredondar para baixo...
print('A raiz de {} é {:.2f}'.format(num, math.floor(raiz)))


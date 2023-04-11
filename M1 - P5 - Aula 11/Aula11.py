#Cores no terminal
'''
Padrão ANSI → Tem escape sequence

Exemplo:

\033[(Aqui insiro o código)m

\033[**style:text:background** m

Ex1: \033[0:33:44m
 
Para o **estilo**, as melhores opções são:

0 → None

1 → Bold

4 → Underline

7 → Negative

**Texto:**

30 → Branco

31 → Vermelho

32 → Verde

33 → Amarelo

34 → Azul

35 → Roxo

36 → Azul piscina

37 → Cinza

**Background:**

40 → Branco

41 → Vermelho

42 → Verde

43 → Amarelo

44 → Azul

45 → Roxo

46 → Azul piscina

47 → Cinza
'''
print('Olá, mundo!')

#Escrito em vermelho
print('\033[7;30;41mOlá, mundo!\033[m')

#Mistura
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))

#Outros
nome = 'Vinicius'
cores = {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m'}
print('Olá, muito prazer em conhecer você, {}{}{}'.format(cores['amarelo'],nome,cores['limpa']))

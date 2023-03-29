#Aula 8 - Utilizando módulos
''''
Python trabalha com módulos pré instalados e pré definidos..

Ou seja, pra isso, vamos instalando os módulos.

O que são os módulos?

- São recursos aditivos para fazer algumas funcionalidades ao longo do dia.
- Podemos chamar de Bibliotecas (Toda linguagem tem módulos)
    - Sobre bibliotecas, podemos fazer **importações** de bibliotecas

Para incluir qualquer coisa tenho que realizar o seguinte comando:

```python
import
```

Exemplo:

![python3.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/534d5e79-97e5-4e03-8d59-f58f05873c41/python3.png)

Para importar comida, usarei o seguinte comando:

```python
import comida
```

Logo, **tudo** que estiver dentro dessa biblioteca será adicionado ao projeto

E se eu quiser importar somente alguma coisa?

```python
from comida import hamburguer
```

Exemplo de uma biblioteca padrão: **Math**

- Tudo o que fizemos na aula anterior, como soma, divisão e outras, é um padrão que vem no Python. Mas no **Math** há **outras coisas incluídas**.

Exemplo:

- Para trabalhar com arredondamentos:
    - **ceil** → Arredondamento pra cima
    - **floor** → Arredondamento pra baixo
    - **trunc** → Truncar o número. Da vírgula em diante ele não apresenta
    - **pow** → Elevar à potência
    - **sqrt** → Raiz quadrada
    - **factorial** → Descobrir o fatorial de um cálculo

Se eu quiser importar tudo:

```python
import math
```

Se eu quiser utilizar somente uma funcionalidade, ou duas:

```python
from math import sqrt
from math import sqrt, floor
```

E é assim com qualquer uma.
'''

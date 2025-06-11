import matplotlib # import genérico 
from random import randint # import específico 

import math 

num =float(input('Digite um número: '))
print(f'A raiz do número {num} é {math.sqrt(num)}') #importa da biblioteca inteira do math a função sqrt(raiz)

# import math as m  - importa math mas será chamada de m - {m.sqrt(num)}
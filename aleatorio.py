import random 
from random import shuffle

val= random.randint(1,20) # número aleatório inteiro entre 1 e 20
print(val)

valor=random.random() #número de ponro flutuante entre 0 e 1
print(f'Número gerado: {round(valor * 10,2)}')#round - arredonda    o valor gerado com duas casas decimais 

valor2= random.uniform(1,100)# será gerado um número de ponto flutuante entre 0 e 100
print(f'Número: {round(valor,4)}') # round arredonda o valor gerado com suas casas decimais 

# sortear um valor de uma lista específica 
l= [2,5,4,6,4,2,23,5,54,34,53,5,45,353,53]
n = random.choice(l) # - escolha = choise
print(n)

# extrair vários valores dentro de uma lista específica 
l= [2,5,4,6,4,2,23,5,54,34,53,5,45,353,53]
n = random.sample(l,3) # neste caso escolheu 3 números aleatoriamente da lista 
print(n)

#embaralhar os dados de uma sequência 
print(f'Exibir a lista original: {l} ')
random.shuffle(l) # função shuffle tem que estar sozinha na linha 
print(f'Lista embaralhada: {l}')
#A função random.shuffle(lista) embaralha a lista no local (in-place), ou seja,
#  ela modifica diretamente a lista original e não retorna nenhum valor (retorna None).
#  Por isso, quando você faz v = random.shuffle(l), a variável v recebe None.


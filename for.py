# O for é utilizado para percorrer ou iterar sobre uma sequência de dados 
# (seja esse uma lista, uma tupla, uma string),
#  executando um conjunto de instruções em cada item.

lista= [0,22,45,12,5,4,7]
nome = 'Matheus'
for item in lista:
    print(item)
for letra in nome:
    print(letra)

# quero fazer uma lista mas sem colocar item por item 
for num in range(1,10): # em uma faixa(range) de 1 até 9
    print(num)
for num in range (10): # vai gerar do 0 até o 9
    print(num)

# quero que o range escreva um nome x vezes
nome=input('Qual é o seu nome: ')
for x in range(10):
    print(f'{x+1} {nome}')

#range(valor inicial, valor final , incremento)
for x in range(2,20,2): # de dois até 19 contando de 2 em dois
    print(x)
# da pra fazer utilizando um decremento também (número negativo)
for x in range(20,2,-2): # de 20 até 2 contando de -2 em -2
    print(x)

pedras= ('Rubi','Esmeralda','Coco','Safira','Diamante','Turmalina') # tupla

for pedra in pedras:
    if pedra=='Coco':
        continue # quebra a interação atual do laço 
    print(pedra)
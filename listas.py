#permite armazenar vários dados em uma única variável - 
# lista- representa uma sequência de valores

# SINTAXE - nome_lista=[valores]

n1 = [3,4,45,4,4,5,3,2]
n2 = [12,1,65,7,7,868,78]

valores = n1 + n2 # vai concatenar as listas 
print(valores)
print(type(valores))

print(valores[0])# para acessar os itens específicos de uma lista,
# basta colocar o valor do índice do item - começa no 0 
#colocando o valor -1 acessa o último indice da lista, 
# -(sinal de negativo vai o final para o começo)

print(valores[0:4])

#quer saber quando elementos tem na lista 
print(len(valores)) # len = length - comprimento 

#valores da lista em ordem crescente
print(sorted(valores))

#do maior para o menor
print(sorted(valores, reverse=True))

#somar todos os valores da lista
print(sum(valores))

#valor mínimo e valor máximo 
print(min(valores))
print(max(valores))

#MANIPULANDO VALORES DA LIISTA 

valores.append(25) # append acrencenta um valor ao final da lista 
print(valores)

valores.pop() #exclui o último elemento de uma lista 
print(valores)

valores.pop(7) # o método pop exclui o valor que desejar, basta informar a posição 
print(valores)

valores.insert(7,33) #adiciona um valor na posição desejada 
print(valores)

print(33 in valores)#a o número 33 na lista valores

b1= input('Digite o nome de uma bebida: ')
b2= input('Digite o nome de outra bebida: ')
b3= input('Digite o nome de mais uma bebida: ')
b4= input('Digite o nome da penúltima bebida: ')
b5= input('Digite o nome da última bebida: ')

lista=[b1,b2,b3,b4,b5]

alfabeto= sorted(lista)

for n in alfabeto:
    print(n)












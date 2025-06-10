nome = 'Matheus '
nome1 = input('O que? ')

print(nome + nome1)

media = 0 
n1 = n2 = n3 = n4 = 0.0
nome4, idade = 'Jamal', 25
estado = True
# Função Type 
# Type exprime o tipo de dado da variável

print(type(media))
print(type(n1))     
print(type(idade))
print(type(nome4))
print(type(estado))
print(type(1+2j)) #valor complexo 

# Função isinstance() - verrifica de uma variável é de um tipo específico (pode haver vários tipos )
a = 10
b = 'Sol'

print(isinstance(a, str))
print(isinstance(a, int))
print(isinstance(a,(int,float))) # se a é int ou float - se ela for um dos dois, retorna True

a = 30 # reatribuição de valor 
c = 2
r= a*c #uma variével pode conter outras variáveis dentro dela 
print(r)
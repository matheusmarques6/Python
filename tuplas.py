# as tuplas são imutáveis - após criada o conteúdo da tupla não pode ser modificado 

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He','Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres # concatenação de tuplas 

t1 = (5,4,6,4,2,9,8,0,7,3,3,3,3,5,6,7,3,2)
print(t1.count(3))# conta quantas fezes este número específico aparece 
# - funcona para string tanbém

print('Cl' in halogenios) # Cl está na tupla halogenio 
print(sum(t1)) # soma todos os itens da tupla 
print(min(t1)) # mostra o menor valor da tupla 
print(max(t1)) # mostra o valor máximo da tupla

# Operações nãos disponiveis em tuplas: .sort() , .append() , reverse(), pop()... 
# - qualquer operação que mude o conteúdo da tupla

for elemento in elementos: 
    print(f'Elemento químico: {elemento}')

#criar uma lista apartir de uma tupla
grupo17 = list(halogenios)
print(type(grupo17))
print(grupo17)

# criar uma tupla a partir de uma lista 
grupo1= ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(type(alcalinos))
print(sorted(alcalinos))
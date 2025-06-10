# AND = apenas será verdadeiro quando todas as condições forem verdadeiras
# OR  = apenas será falsa quando todas as condições forem falsas 
# NOT = operador unário = recebe apenas um valor e o inverte - true para false e false para true


idade = 21
altura = 1.80

resultado = (idade >=18) and (altura >=1.75) # Verifica se a pessoa é maior de idade e tem altura maior ou igual a 1.75m
print('Pode participar do evento ? ', resultado )
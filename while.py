# while = enquanto 

num = 1
while (num <= 10):
    print(num)
    num += 1 # += função de incremento - adionionará o valor 1 a váriavel já existente 


nome = None
while True:
    p=(input('Digite seu nome, ou x para parar o programa: '))

    if p =='x' or p=='X':
        break 
    else:
        print(f'Bem Vindo {nome}')

print('Até logo!!')
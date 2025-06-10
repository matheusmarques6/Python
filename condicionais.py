# Simples, Composto , Encadeado 
# if - se
# else - se não 



n1=float(input('Digite a nota da primeira prova: '))
n2=float(input('Digite a nota da segunda prova: '))

# Calculo da média aritmética 
m=(n1+n2) / 2

if m >= 7: 
    print('Parabéns, você passou!!!')
elif (m>=5): # Condicional Encadeada - adiciona uma Terceira( ou mais ) condição
    print('Reprovado mas você ainda pode fazer a Recuperação !!!!')
else: # - se não tivesse o else seria uma Condicional Composta 
    print('Você foi reprovado :c')

print(f'Sua média é {m}')
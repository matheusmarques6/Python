#um laço de repetição dentro de outro laço

for cont in range(1,6):
    print(f'\nRodada: {cont}')
    for cont_in in range(2,11,2):
        print(f'Valor: {cont_in}')

print('Fim dos laços\n')

from random import randint
for A in range(1,6):
    print(f'\nSorteio {A}')
    for x in range(5):
        num = randint(1,100)
        print(f'Valor Sorteado: {num}')


lista_cores = ['verde', 'amarelo', 'vermelho' ]

for i in range(3):
    print(f'Cor do Aliginea atingido {lista_cores[i]}')
    if lista_cores[i] == 'verde':
        print('Acabou de ganhar 5 pontos por atingir o alienígena')
    if lista_cores[i] != 'verde':
        print('Acabou de ganhar 10 pontos por atingir o alienígena')
    if lista_cores[i] == 'vermelho':
        print('Acabou de ganhar 15 pontos por atingir o alienígena')

print('\n\t********************************')
print('\t********** Nuno Rocha **********')
print('\t********************************\n')

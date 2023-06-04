animais = [
    {
        'nome': 'piloto',
        'tipo': 'cão',
        'dono': 'nuno'
    },
    {
        'nome': 'pantufas',
        'tipo': 'gato',
        'dono': 'isbel'
    },
    {
        'nome': 'finfas',
        'tipo': 'coelho',
        'dono': 'mario'
    }
]

for animal in animais:
    print(f'O {animal["nome"].title()} é um {animal["tipo"].title()} e nome do dono é: {animal["dono"].title()}')

print('\n\tNuno Rocha\n')
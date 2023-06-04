x = 1
y = 2

comparacoes =  ['>', '<', '>=', '<=', '!=', '==']
resultado_esperado = ['False', 'True', 'False', 'True', 'True', 'False' ]

for comparacao, resultado in zip(comparacoes, resultado_esperado):
    print(f'\nO resultado esperado de ({x} {comparacao} {y}) é: {resultado}')
    print(eval(f'{x} {comparacao} {y}'))


carros = ['toyota', 'mercedes']
carros_teste = ['opel', 'seat']
condicoes = ['in', 'not in']
resultado_esperado_carros = ['False', 'True']

for carro_teste in carros_teste:
    for carro, condicao, resultado_carro in zip(carros, condicoes, resultado_esperado_carros):
        print(f'\nO resultado esperado de ({carro_teste} {condicao} carros) é: {resultado_carro}')
        print(eval(f"'{carro_teste}' {condicao} '{carro}'"))

print('\n\t********************************')
print('\t********** Nuno Rocha **********')
print('\t********************************\n')
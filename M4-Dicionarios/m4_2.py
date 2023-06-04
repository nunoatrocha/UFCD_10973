palavras = {
    'sort': 'ordena',
    'print': 'imprime',
    'input': 'entrada',
    'list': 'lista',
    'dict': 'dicionario',
}

for palavra, significado in palavras.items():   # ciclo for para imprimir as palavras e valores
    print(f'{palavra} = {significado}')
print()
for palavra in palavras.keys():   #  ciclo for para imprimir só as palavras
    print(f'{palavra}')
print()
for significado in palavras.values():   #ciclo for para imprimir os significados
    print(f'{significado}')

print('\n\tNuno Rocha\n')
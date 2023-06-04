pedidos_sandes = ['sandes de presunto', 'sandes de porco', 'sandes de queijo']
sandes_prontas = []

pedidos_sandes.reverse() # inverte a lista para preparar os pedidos por ordem de entrada
while pedidos_sandes:
    sandes_em_preparacao = pedidos_sandes.pop()
    sandes_prontas.append(sandes_em_preparacao)
print()
for sandes_pronta in sandes_prontas:
    print(f'A {sandes_pronta} está pronta')

print('\n\tNuno Rocha\n')

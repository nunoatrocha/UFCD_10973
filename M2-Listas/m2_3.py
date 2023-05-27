
"""
Atividade 2.3 - Ordenar listas

"""

# Locais a visitar
locais_a_visitar = ['Nova York', 'Japão', 'Sardenha', 'Roma', 'Antártida']
# imprimir lista
print(locais_a_visitar)
# imprimir lista de forma alfabética mantendo a ordem original
print(sorted(locais_a_visitar))
print(locais_a_visitar)
# imprimir lista de forma alfabética reversa mantendo a ordem original
print(sorted(locais_a_visitar, reverse=True)) 
print(locais_a_visitar)
# inverter a lista de forma permanente
locais_a_visitar.reverse()
print(locais_a_visitar)
# inverter a lista de forma permanente
locais_a_visitar.reverse()
print(locais_a_visitar)
# ordenar a lista de forma permanente alfabéticamente
locais_a_visitar.sort()
print(locais_a_visitar)
# ordenar a lista de forma permanente alfabéticamente reversa
locais_a_visitar.sort(reverse=True)
print(locais_a_visitar)
# imprimir o tamanho da lista
print(f'A lista tem {len(locais_a_visitar)} locais a visitar.')

print('\n\t***Nuno Rocha***')
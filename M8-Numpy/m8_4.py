import numpy as np

def comp_tam_nomes(nome):
    return len(nome)

nomes = np.array(['Carlos', 'Maria', 'Ana', 'Antonieta', 'André'])
print(nomes)

nomes_ordenados_alfab = np.sort(nomes)
print(nomes_ordenados_alfab)

nomes_ordenados_tam = np.array(sorted(nomes, key=comp_tam_nomes))
print(nomes_ordenados_tam)

print('Nuno Rocha')
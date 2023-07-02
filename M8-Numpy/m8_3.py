import numpy as np

numeros = np.array([2, 15, 10, 8, 19])

media = np.mean(numeros)
mask = numeros > media
print(numeros)
print(numeros > media)
print(numeros[mask])

print('Nuno Rocha')
import numpy as np

arr = np.array([[1, 2, 3, 11], [4, 5, 6, 12], [7, 8, 9, 13]])

print(arr)
print(np.sum(arr, axis=1))  # Calcula a soma de cada linha da matriz
print(np.prod(arr, axis=0)) # Calcula o produto de cada coluna da matriz

print('Nuno Rocha')
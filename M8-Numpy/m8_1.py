import numpy as np

def media(arr):
    soma = 0
    for nota in arr:
        soma += nota
    return soma / 10
    
notas = np.array([2, 15, 10, 8, 19, 4, 13, 12, 17, 9])
print(notas)
print(f'A media das notas é: {media(notas)}')

print('Nuno Rocha')
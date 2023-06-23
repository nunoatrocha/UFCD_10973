numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

try:
    soma = int(numero_1) + int(numero_2)
except ValueError:
    print('Digite numeros intereiros')
else:
    print(f'Resultado da soma: {soma}')

print('Nuno Rocha')
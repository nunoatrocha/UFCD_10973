import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, 'g', label='Curva 1')
plt.plot(x, y2, 'b', label='Curva 2')

plt.title('Gráfico de Linhas com Duas Curvas')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.legend()
plt.show()

print('Nuno Rocha')
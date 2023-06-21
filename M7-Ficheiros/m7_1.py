nome_ficheiro = 'aprender_python.txt'

with open(nome_ficheiro) as ficheiro:
    contents = ficheiro.read()
    print(contents)

with open(nome_ficheiro) as ficheiro:
    for line in ficheiro:
        print(line.strip())

with open(nome_ficheiro) as ficheiro:
    lista = []
    for line in ficheiro:
        lista.append(line.strip())

for line in lista:
    print(line)

print('Nuno Rocha')

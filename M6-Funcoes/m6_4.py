nome_magicos = ['nuno', 'pedro', 'joana', 'maria']

def exibir_magicos(nomes):
    for nome in nomes:
        print(nome.title())

exibir_magicos(nome_magicos)

def grandes_magicos(nomes):
    for i in range(0, len(nomes)):
        nomes[i] = 'O Grande' + ' ' + nomes[i].title()

grandes_magicos(nome_magicos)

exibir_magicos(nome_magicos)
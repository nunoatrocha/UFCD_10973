nome_magicos = ['nuno', 'pedro', 'joana', 'maria']

def exibir_magicos(nomes):
    for nome in nomes:
        print(nome.title())

def grandes_magicos(nomes):
    grandes_nomes = []
    for nome in nomes:
        grandes_nomes.append('O Grande ' + nome.title())
    return grandes_nomes

exibir_magicos(nome_magicos)

nome_magicos_modificados = grandes_magicos(nome_magicos[:])
exibir_magicos(nome_magicos)
exibir_magicos(nome_magicos_modificados)

print('Nuno Rocha')
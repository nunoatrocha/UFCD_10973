def cria_pessoa(nome, idade):
    pessoa = {'nome': nome, 'idade': idade}
    return pessoa

p = cria_pessoa('Nuno', 43)

idade1 = p.get('idade')
print(idade1)
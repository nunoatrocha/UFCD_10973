def lista_ficheiro(nome_do_ficheiro_txt):
    with open(nome_do_ficheiro_txt) as f:
        conteudo = f.readlines()
        return conteudo

linhas = lista_ficheiro("texto.txt")
print(linhas)

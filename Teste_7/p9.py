def linha_ficheiro(nome_do_ficheiro_txt):
    with open(nome_do_ficheiro_txt) as n:
        linhas = n.readlines()
        str = ''
    for linha in linhas:
        str += linha.strip()
    return str

linha = linha_ficheiro("texto.txt")
print(linha)


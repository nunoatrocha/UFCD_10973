def imprimir_ficheiro(nome_do_ficheiro_txt):
    nome = nome_do_ficheiro_txt
    with open(nome) as n:
        for linha in n:
            print(linha)
        
imprimir_ficheiro("texto.txt")
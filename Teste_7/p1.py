def imprimir_ficheiro(nome_do_ficheiro_txt):
    nome = nome_do_ficheiro_txt
    with open(nome) as n:
        conteodo = n.read()
        print(conteodo)
        
imprimir_ficheiro("texto.txt")
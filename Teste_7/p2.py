def imprimir_ficheiro(nome_do_ficheiro_txt):
    nome = nome_do_ficheiro_txt
    try:
        with open(nome) as n:
            conteodo = n.read()
            print(conteodo)
    except FileNotFoundError:
        msg = f'Desculpa, o ficheiro {nome} não existe.'
        print(msg)


        
imprimir_ficheiro("texto.txt")
imprimir_ficheiro("erro.txt")

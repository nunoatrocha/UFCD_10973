def criar_ficheiro(nome_do_ficheiro_txt, str):
    with open(nome_do_ficheiro_txt, 'w') as f:
        f.write(str)




criar_ficheiro("texto.txt","UFCD 10793 - Módulo 7 Ficheiros")


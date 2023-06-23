def criar_ficheiro(nome_do_ficheiro_txt, lst):
    with open(nome_do_ficheiro_txt, 'w', encoding='utf8') as f:
        for linha in lst:
            f.write(f'{linha}\n')


linhas = ["Olá Mundo!", "Python é o melhor","UFCD 10793"]
criar_ficheiro("text.txt",linhas) 
lista_convidados = 'registo_convidados.txt'

while True:
    nome = input('\nDigite o seu nome: ')
    print(f'Olá {nome} foi adicionado com sucesso.\n')
    with open(lista_convidados, 'a', encoding='utf-8') as convidado:
        convidado.write(nome + '\n')
    sair = input('Deseja acrescentar mais algum convidado [s/n]: ')
    if sair == 'n':
        break

print('\nNuno Rocha')
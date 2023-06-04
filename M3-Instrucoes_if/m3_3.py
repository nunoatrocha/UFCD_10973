users = ['nuno', 'vera', 'admin', 'isbel', 'pedro', 'mario']
lista_vazia = []

if users:
    for user in users:
        if user == 'admin':
            print(f'Bem-vindo caro Administrador da Rede, tenha um bom trabalho.')           
        else:
            print(f'Bem vindo {user.title()}')
else:
    print('Precisamos encontrar alguns utilizadores')

# Teste com a lista vazia
if lista_vazia:
    for user in users:
        if user == 'admin':
            print(f'Bem-vindo caro Administrador da Rede, tenha um bom trabalho.')           
        else:
            print(f'Bem vindo {user.title()}')
else:
    print('\nPrecisamos encontrar alguns utilizadores\n')

print('\tNuno Rocha\n')
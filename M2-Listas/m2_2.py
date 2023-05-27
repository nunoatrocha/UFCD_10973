
"""
Atividade 2.2 - Alterar, acrescentar e remover elementos

"""

# Lista de convidados inicial
convidados = ['Pedro', 'Nuno', 'João']
# Enviar convites
convite = f'Olá {convidados[0]}, está convidado para o jantar.'
print(convite)
convite = f'Olá {convidados[1]}, está convidado para o jantar.'
print(convite)
convite = f'Olá {convidados[2]}, está convidado para o jantar.'
print(convite)
# Mensagem
print(f'\nPor motivos pessoais o convidado: {convidados[1]} não vai poder comparecer.\n')
# alterar o convidado que não pode comparecer pelo novo convidado
convidados[1] = 'Rui'
# Enviar convites
convite = f'Olá {convidados[0]}, está convidado para o jantar.'
print(convite)
convite = f'Olá {convidados[1]}, está convidado para o jantar.'
print(convite)
convite = f'Olá {convidados[2]}, está convidado para o jantar.'
print(convite)
# Mensagem
print(f'\nMeus caros fui informado que temos um mesa maior para o nosso jantar.\n')
convidados.insert(0, 'Bruno')  # insere no inicio da lista
convidados.insert(2, 'Alexandre') # insere no meio da lista
convidados.append('Tito') # insere no fim da lista
# Enviar convites
convite = f'\nOlá {convidados[0]}, está convidado para o jantar.'
print(convite)
convite = f'Olá {convidados[1]}, está convidado para o jantar.'
print(convite)
convite = f'Olá {convidados[2]}, está convidado para o jantar.'
print(convite)
convite = f'Olá {convidados[3]}, está convidado para o jantar.'
print(convite)
convite = f'Olá {convidados[4]}, está convidado para o jantar.'
print(convite)
convite = f'Olá {convidados[5]}, está convidado para o jantar.'
print(convite)
print(f'\nApenas posso convidar duas pessoas.\n')
# remover os convidado em excesso na lista
print(f'Ola {convidados.pop()}, sinto muito mas não vou poder convida-lo para o jantar.')
print(f'Ola {convidados.pop()}, sinto muito mas não vou poder convida-lo para o jantar.')
print(f'Ola {convidados.pop()}, sinto muito mas não vou poder convida-lo para o jantar.')
print(f'Ola {convidados.pop()}, sinto muito mas não vou poder convida-lo para o jantar.\n')
# Mensagem
print(f'Olá {convidados[0]}, o convite ainda está valido.')
print(f'Olá {convidados[1]}, o convite ainda está valido.')
# remover os dois ult convidados
del convidados[0]
del convidados[0]
print(convidados)
print('\n\t***Nuno Rocha***')

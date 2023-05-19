"""
Atividade 1.2 - Strings

"""

nome = 'Nuno'
message = 'Olá ' + nome + ', estás a gostar de Python?'
print(message)

novo_nome = 'roCha  '  # nome escrito propositadamente desta forma: 'roCha  ' para poder usar os métodos solicitados
novo_nome = novo_nome.rstrip()

print('Nome com letras maiúsculas: ',  novo_nome.upper())
print('Nome com letras minúsculas: ',  novo_nome.lower())
print('Nome com a primeira letra maiúscula: ',  novo_nome.title())
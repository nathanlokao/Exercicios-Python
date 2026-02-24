# Dicionário com entrada do usuário
# Peça ao usuário:
# nome
# idade

# Armazene em um dicionário e imprima.

dicionario = {}

nome = input('Digite seu Nome: ')
idade = int(input('Digite sua Idade: '))

dicionario.update({'nome' : nome.strip().replace(' ', ''), 'idade' : idade})

print(dicionario)
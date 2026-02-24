# Crie um dicionário e faça uma cópia dele usando .copy().
# Altere a cópia e veja se o original mudou.

dados = {'nome': 'Lucas', 'idade': 19}
copia_dados = dados.copy()

copia_dados.update({'idade' : 20, 'cidade' : 'Curitiba'})

print(f'Dicionário Original: {dados}\nCópia do Dicionário: {copia_dados}')


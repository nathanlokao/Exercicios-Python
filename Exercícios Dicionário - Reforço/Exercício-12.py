# Use get() para tentar acessar a chave "cidade" sem dar erro

pessoa = {'nome': 'Carlos', 'idade': 25}

print(pessoa.get('cidade', 'Item descrito não existe'))

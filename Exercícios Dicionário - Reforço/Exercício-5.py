# Remova a chave ano do dicionário e mostre o resultado.

carro = {'marca' : 'Toyota', 'ano' : 2020, 'cor' : 'preto'}

# del carro['ano']
ano = carro.pop('ano')

print(ano)
print(carro)
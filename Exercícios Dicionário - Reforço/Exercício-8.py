# Crie um dicionário e peça para o usuário digitar uma chave.
# Verifique se ela existe no dicionário.

dicionario = {'Coca-Cola' : 7.5, 'Arroz 5kg' : 8, 'Video-Game' : 5000, 'Salgadinho' : 5, 'Pelúcia' : 50}

produto = input('Digite um Produto da Loja: ')

print(dicionario.get(produto, 'Infelizmente não temos'))
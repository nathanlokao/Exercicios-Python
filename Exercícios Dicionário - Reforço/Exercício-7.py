# Crie um dicionário com 5 produtos e seus preços.
# Depois, mostre:

# Quantos itens existem no dicionário

dicionario = {'Coca-Cola' : 7.5, 'Arroz 5kg' : 8, 'Video-Game' : 5000, 'Salgadinho' : 5, 'Pelúcia' : 50}

quantia_itens = 0

for chave in dicionario:
    quantia_itens = quantia_itens + 1

print(f'Dicionário possui: {quantia_itens} produtos')
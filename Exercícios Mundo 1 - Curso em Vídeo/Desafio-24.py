# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma Cidade: '))

if 'SANTO' in cidade.strip().replace(' ', '').upper()[0:5]:
    print('O nome da sua cidade COMEÇA com o nome SANTO')
else: 
    print('O nome da sua cidade NÃO COMEÇA com o nome SANTO')
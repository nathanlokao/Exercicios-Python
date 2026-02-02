# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input('Digite seu Nome Completo: ')).strip().title()

primeiro_nome = nome_completo.split()[0]
ultimo_nome = nome_completo.split()[-1]

print(f'Primeiro Nome: {primeiro_nome}\nÚltimo Nome: {ultimo_nome}')

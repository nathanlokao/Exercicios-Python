# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = input('Digite seu nome: ')

print('seu nome com Letras Maiúsculas:', nome.upper())
print('seu nome com Letras Minúsculas:', nome.lower())
print('A quantidade de Letras do seu Nome:', len(nome.strip().replace(' ', '')))
print('A quantidade de Letras do seu Primeiro Nome:', len(nome.split()[0]))
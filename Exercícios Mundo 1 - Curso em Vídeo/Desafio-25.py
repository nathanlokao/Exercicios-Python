# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite um nome que contenha "Silva": '))

if 'SILVA' in nome.strip().replace(' ', '').upper():
    print('O nome contém "Silva"')
else: 
    print('O nome NÃO contém "Silva"')
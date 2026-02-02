# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.


""" Versão adaptando o número para string (FALHA)

Observação: Fiquei curioso sobre como elaborar uma solução para esta versão em string.
FALHA: Caso utilize um número menor do que milhar, fará o índice ficar perdido e apontar para um endereço de caracter inexistente. IndexError: string index out of range.

numero = int(input('Digite um número entre 0 e 9999: '))

n = str(numero)

if numero >= 0 and numero <= 9999:
    unidade = n[3]

    dezena  = n [2]

    centena = n [1]

    milhar = n [0]

    print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}\n')

else:
    print('Valor inválido')
"""

numero = int(input('Digite um número entre 0 e 9999: '))

if numero >= 0 and numero <= 9999:

    unidade = numero // 1 % 10
    dezena =  numero // 10 % 10
    centena = numero // 100 % 10
    milhar =  numero // 1000 % 10

    print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}\n')

else:
    print('Valor inválido')
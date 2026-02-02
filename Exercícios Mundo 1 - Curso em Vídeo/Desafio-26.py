"""
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

"""

frase = str(input('Escreva uma frase qualquer: '))

print(f'A frase contém {frase.upper().count('A')} letra(s) "A"')
print(f'A primeira aparição da letra "A", é no índice {frase.upper().find('A')}')
print(f'A última aparição da letra "A", é no índice {frase.upper().rfind('A')}')



contador = 0

for i in range(1, 7):
    numero = int(input(f'Digite o {i}° valor: '))
    if numero % 2 == 0:
        contador = contador + numero
        print(f'Par')
    else:
        print('Impar')
print(f'A soma dos valores pares é: {contador}')
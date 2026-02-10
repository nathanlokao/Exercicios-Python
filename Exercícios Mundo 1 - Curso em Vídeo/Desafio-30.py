# Ímpar ou par

while True:
    try:
        numero = int(input('Digite um número inteiro: '))

        if numero % 2 == 0:
            print(f'O número {numero} é par')
        elif numero % 2 == 1:
            print(f'O número {numero} é ímpar')
    except ValueError:
        print('Digite um valor válido')

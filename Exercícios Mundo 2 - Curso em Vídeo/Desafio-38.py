# Comparativo de números

while True:
    try:
        n1 = float(input('Digite o Valor de N1: '))
        n2 = float(input('Digite o Valor de N2: '))

        if n1 > n2:
            print(f'Valor de N1: {n1}\nValor de N2: {n2}\n')
            print('O valor de N1 é MAIOR que N2\n')
        elif n1 < n2:
            print(f'Valor de N1: {n1}\nValor de N2: {n2}\n')
            print('O valor de N1 é MENOR que N2\n')
        elif n1 == n2:
            print(f'Valor de N1: {n1}\nValor de N2: {n2}\n')
            print('O valor de N1 e N2 são IGUAIS\n')
    except ValueError:
        print('Digite um valor válido\n')
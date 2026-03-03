while True:

    while True:
        try:
            posicao = int(input('Qual Termo de Fibonacci, deseja ver o valor? '))
            if posicao < 0:
                print('Números Negativos são Inválidos\n')
                continue
            elif posicao == 0:
                print(f'Valor do 0° Termo = 0\n')                
                continue
            elif posicao == 1:
                print('0 --> 1')
                print(f'Valor do 1° Termo = 1\n')
                continue                
            else:
                break
        except ValueError:
            print('Digite um Apenas Números Naturais\n')

    n1 = 0
    print(n1, end = ' --> ')

    n2 = 1
    print(n2, end = ' --> ')

    contador = 0
    while contador < (posicao - 1):
        r = n1 + n2
        print(r, end = ' --> ' if contador < (posicao - 2) else '')
        n1 = n2
        n2 = r

        contador += 1
    print(f'\nValor do {posicao}° Termo = {r}')
    print('')
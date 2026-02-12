# Conversor de Número Inteiro para:
# Binário, Octal e Hexadecimal


while True:
    try:
        escolha = int(input('Conversor de Número Inteiro para:\nBinário - 1\nOctal - 2\nHexadecimal - 3\n'))
        print('')

        if escolha == 1:
            numero = int(input('Digite um número inteiro: '))
            binario = bin(numero)[2:]
            print(f'O valor binário é: {binario}\n')
        elif escolha == 2:
            numero = int(input('Digite um número inteiro: '))
            octal = oct(numero)[2:]
            print(f'O valor octal é: {octal}\n')
        elif escolha == 3:
            numero = int(input('Digite um número inteiro: '))
            hexadecimal = hex(numero)[2:]
            print(f'O valor hexadecimal é: {hexadecimal}\n')
        else:
            print('Opção inválida\n')
    except ValueError:
        print('')
        print('Digite um valor válido\n')
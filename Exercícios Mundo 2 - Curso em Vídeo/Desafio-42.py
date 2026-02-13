# Validação de Triângulo e dizer o tipo do triângulo

while True:
    try:
        lado_A = float(input('Digite o valor do Lado A: '))
        lado_B = float(input('Digite o valor do Lado B: '))
        lado_C = float(input('Digite o valor do Lado C: '))

        if lado_A < (lado_B + lado_C) and lado_B < (lado_A + lado_C) and lado_C < (lado_A + lado_B):
            print('Triângulo Válido\n')

            if lado_A == lado_B and lado_B == lado_C:
                print('Tipo do Triângulo: Equilátero\n')
            elif lado_A == lado_B or lado_B == lado_C or lado_C == lado_A:
                print('Tipo do Triângulo: Isósceles\n')
            elif lado_A != lado_B and lado_B != lado_C and lado_C != lado_A:
                print('Tipo do Triângulo: Escaleno\n')
        
        else:
            print('Triângulo Inválido\n')

    except ValueError:
        print('Valor inválido\n')
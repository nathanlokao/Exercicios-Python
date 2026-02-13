while True:

    while True:
        try:
            altura = float(input('Qual é a sua altura? (metros): '))
            if altura < 0:
                print('Digite um valor positvo\n')
                continue
            else:
                break
        except ValueError:
            print('Digite um valor númerico\n')

    while True:
        try:
            peso = float(input('Qual é o seu peso?: '))
            if peso < 0:
                print('Digite um valor positvo\n')
                continue
            else:
                break
        except ValueError:
            print('Digite um valor númerico\n')

    imc = peso / (altura * altura)

    print(f'Valor IMC = {imc:.2f}')

    if imc < 18.5:
        print('Está ABAIXO DO PESO\n')
    elif imc >= 18.5 and imc < 25:
        print('PESO IDEAL\n')
    elif imc >= 25 and imc <= 30:
        print('Está com SOBREPESO\n')
    elif imc > 30 and imc <= 40:
        print('Está com OBESIDADE\n')
    elif imc > 40:
        print('Está com OBESIDADE MÓRBIDA\n')

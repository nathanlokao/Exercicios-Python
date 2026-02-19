while True:
    pesos = []

    for i in range(1, 6):
        while True:
            try:
                pessoa = float(input('Digite seu peso: '))
                break
            except ValueError:
                print('Digite apenas kilos\n')
        pesos.append(pessoa)

    print(f'{pesos}\nPeso Máximo: {max(pesos)}\nPeso Mínimo: {min(pesos)}\n')

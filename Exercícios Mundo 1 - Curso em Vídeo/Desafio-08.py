# Conversor de metros para centímetros e milímetros

print(8 * '#', 'Conversor de metros para centímetros e milímetros', 8 * '#')

while True:
    try:
        metros = float(input('Escreva o valor em Metros: '))
        centimetros = metros * 100
        milimetros = metros * 1000

        print(f'Resultado:\nMetros: {metros:.2f}m\nCentímetros: {centimetros:.2f}cm\nMilímetos: {milimetros:.2f}mm')

    except ValueError:
        print('Digite novamente')
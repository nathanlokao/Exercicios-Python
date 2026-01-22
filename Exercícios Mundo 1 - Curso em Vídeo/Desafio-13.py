# Calculadora de aumento em 15%

print('#' * 8, 'Calculadora de aumento em 15%', '#' * 8)

while True:
    try:
        x = float (input ('Digite o Valor Inicial: '))
        porcentagem = x * 0.15
        resultado = x + porcentagem

        print(f'Valor Inicial: {x}\nValor de Aumento: {porcentagem}\nResultado: {resultado}')

    except ValueError:
        print('Digite novamente')
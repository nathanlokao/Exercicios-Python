# Programa de Tabuada com float :3

print('#' * 8,'Tabuada', '#' * 8)

while True:
    try:
        x = float(input('Digite o valor para calcular a multiplicação: '))

        print(f'{x:.2f} X {1} = {x * 1:.2f}')
        print(f'{x:.2f} X {2} = {x * 2:.2f}')
        print(f'{x:.2f} X {3} = {x * 3:.2f}')
        print(f'{x:.2f} X {4} = {x * 4:.2f}')
        print(f'{x:.2f} X {5} = {x * 5:.2f}')
        print(f'{x:.2f} X {6} = {x * 6:.2f}')
        print(f'{x:.2f} X {7} = {x * 7:.2f}')
        print(f'{x:.2f} X {8} = {x * 8:.2f}')
        print(f'{x:.2f} X {9} = {x * 9:.2f}')
        print(f'{x:.2f} X {10} = {x * 10:.2f}')
    
    except ValueError:
        print('Digite novamente')
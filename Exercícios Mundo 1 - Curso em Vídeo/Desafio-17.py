import math

print('Programa para calcular triângulo retângulo')

while True:
    try:
        n1 = float (input ('Digite o valor do cateto oposto: '))
        n2 = float (input ('Digite o valor do cateto adjacente: '))

        resultado = math.hypot(n1,n2)

        print(f'A hipotenusa é: {resultado:.5f}\n')
    
    except ValueError:
        print('Digite um valor válido\n')
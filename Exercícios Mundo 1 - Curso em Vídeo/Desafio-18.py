from math import radians, sin, cos, tan

while True:
    try:

        graus = float (input ('Digite um valor em Graus: '))

        radianos = radians(graus)

        seno = sin(radianos)
        cosseno = cos(radianos)
        tangente = tan(radianos)

        print(f'Seno: {seno:.4}\nCosseno: {cosseno:.4}\nTangente: {tangente:.4}\n')
    
    except ValueError:
        print('Digite um valor válido!!!\n')
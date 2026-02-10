# Identificador de maior ou menor

while True:
    numero_a = float(input('Digite um número A: '))
    numero_b = float(input('Digite um número B: '))
    numero_c = float(input('Digite um número C: '))

    lista = [numero_a, numero_b, numero_c]
    lista_ordenada = sorted(lista)

    if lista_ordenada[0] == lista_ordenada[1] and lista_ordenada [1] == lista_ordenada[2]:
        print('Foi inputado valores iguais')
        continue

    print(f'{lista_ordenada[0]} < {lista_ordenada[1]} > {lista_ordenada[2]}')


'''
if numero_a > numero_b and numero_b > numero_c:
    print(f'{numero_c} < {numero_b} > {numero_a}')
elif numero_a > numero_c and numero_c > numero_b:
    print(f'{numero_b} < {numero_c} > {numero_a}')
elif numero_b > numero_a and numero_a > numero_c:
    print(f'{numero_c} < {numero_a} > {numero_b}')
elif numero_b > numero_c and numero_c > numero_a:
    print(f'{numero_a} < {numero_c} > {numero_b}')
elif numero_c > numero_a and numero_a > numero_b:
    print(f'{numero_b} < {numero_a} > {numero_c}')
elif numero_c > numero_b and numero_b > numero_a:
    print(f'{numero_a} < {numero_b} > {numero_c}')
'''
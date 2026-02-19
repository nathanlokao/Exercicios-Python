while True:
    frase = input('Digite uma frase: ')
    frase_tratada = frase.strip().replace(' ', '')

    if frase_tratada.isalpha():

        frase_guardada = []

        for letra in frase_tratada:
            frase_guardada.append(letra)

        frase_guardada_invertida = frase_guardada[:: -1]

        print(frase_guardada)
        print(frase_guardada_invertida)

        if frase_guardada == frase_guardada_invertida:
            print('\nEsta frase é um palíndromo\n')
        else:
            print('\nEsta frase NÃO é um palíndromo\n')
    else:
        print('Apenas frases sem números\n')
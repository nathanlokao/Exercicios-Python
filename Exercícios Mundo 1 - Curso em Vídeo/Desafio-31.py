# Preço variável da viagem
# 0,50 até 200 Km
# 0,45 acima de 200 Km

while True:
    try:
        distancia_percorrida = float(input('Digite a distância percorrida: '))

        if distancia_percorrida <= 200 and distancia_percorrida >= 0:
            print(f'Custo da viagem (até 200 Km): R${distancia_percorrida * 0.50:.2f}')
        elif distancia_percorrida > 200:
            print(f'Custo da viagem (acima de 200 Km): R${distancia_percorrida * 0.45:.2f}')
        else:
            print('Valor negativo inválido')
    except ValueError:
        print('Valor inválido')
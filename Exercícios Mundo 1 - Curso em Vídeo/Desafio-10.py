# Conversor Real para Dólar

print('Conversor Real para Dólar')

while True: 
    try:
        carteira = float(input('Digite quantos reais tem na carteira: '))

        real = carteira

        dolar = real * 3.27

        print(f'O usuário pode comprar com {real:.2f} reais, {dolar:.2f} dólares')
    
    except ValueError:
        print('Digite novamente')
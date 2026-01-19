# Calcular quantidade de tinta gasta para pintar uma parede

print('Calculadora para calcular a quantidade de litros de tinta dedicadas para pintar uma parede')

while True:
    try:
        comprimento = float(input('Digite o comprimento da parede: '))
        largura = float(input('Digite a largura da parede: '))

        area = comprimento * largura
        cobertura_tinta = 2

        tinta = area / cobertura_tinta

        print(f'Área da parede: {area}m²\nTinta gasta: {tinta} Litros')
    
    except ValueError:
        print('Digite novamente')
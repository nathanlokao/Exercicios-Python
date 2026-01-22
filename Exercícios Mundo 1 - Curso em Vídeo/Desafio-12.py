# Desconto de 5% ao custo do produto

print('Calculadora de desconto de 5%')

while True:
    try:
        x = float (input ('Digite o valor que vai descontar em 5%: '))
        porcentagem = x * 0.05
        resultado = x - porcentagem

        print(f'Valor Inicial: {x}\nDesconto com 5%: {porcentagem}\nResultado: {resultado}')
    
    except ValueError:
        print('Digite novamente')
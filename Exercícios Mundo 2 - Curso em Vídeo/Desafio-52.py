# Documentação, outra forma de realizar o exércicio: 
# Para realizar o cálculo, pode desconsiderar números menores/iguais a 1 e desconsiderar o valor final (número do input)
# Assim focando apenas nos números entre valor_inicial e valor_final
# Logo na região do For, ficaria assim "for i in range(2, numero):" e tratar todos números divisíveis por i, como não primos

# Então, seguindo a lógica, realizando este procedimento vai garantir que não existem mais de duas divisão com o número do input.

while True:
    try:
        numero = int(input('Digite um número: '))
        total = 0

        for i in range(1, numero + 1):
            if numero % i == 0:
                total = total + 1
            else:
                continue

        if total == 2:
            print(f'O número {numero} é Primo\n')
        else:
            print(f'O número {numero} NÃO é Primo\n')
    except ValueError:
        print('Digite um valor válido\n')

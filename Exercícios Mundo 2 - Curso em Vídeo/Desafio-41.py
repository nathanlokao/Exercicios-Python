import datetime

while True:
    try:
        ano_nascimento = int(input('Digite seu Ano de Nascimento: '))
        if ano_nascimento < 0:
            print('Apenas anos, depois de Cristo\n')
            continue
        ano_atual = datetime.date.today().year

        idade_usuario = ano_atual - ano_nascimento

        if idade_usuario >= 0 and idade_usuario <= 9:
            print('Categoria: Mirim\n')

        elif idade_usuario >= 0 and idade_usuario <= 14:
            print('Categoria: Infantil\n')

        elif idade_usuario >= 0 and idade_usuario <= 19:
            print('Categoria: Junior\n')

        elif idade_usuario >= 0 and idade_usuario == 20:
            print('Categoria: Sênior\n')

        elif idade_usuario >= 0 and idade_usuario > 20:
            print('Categoria: Master\n')
        else:
            print('Você nem nasceu ainda\n')
    except ValueError:
        print('Digite um valor válido\n')    
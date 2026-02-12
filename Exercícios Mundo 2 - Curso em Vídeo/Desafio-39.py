import datetime

print('VERIFICADOR DE IDADE PARA ALISTAMENTO\n')

while True:
    try:
        ano_nascimento = int(input('Qual é seu ano de nascimento?: '))
        ano_atual = datetime.date.today().year

        if ano_nascimento > ano_atual:
            print('\033[34mVocê é um viajante do tempo?!?!?!?\033[m\n')
        elif ano_nascimento < 0:
            print('\033[35mVocê é velho pra caramba!!!\033[m\n')
        else:
            idade_usuario = ano_atual - ano_nascimento

            if idade_usuario < 18:
                tempo_faltante = 18 - idade_usuario
                if tempo_faltante == 1:
                    print('Falta 1 Ano ou MENOS!!!')
                    print('\033[33mVocê ainda não pode se Alistar. Aproveita a vida enquanto dá tempo!!!\033[m\n')
                else:
                    print(f'Faltam aproximadamente {tempo_faltante} Anos')
                    print('\033[33mVocê ainda não pode se Alistar. Aproveita a vida enquanto dá tempo!!!\033[m\n')
            elif idade_usuario > 18:
                tempo_excedente = -1 * (18 - idade_usuario)
                if tempo_excedente == 1:
                    print(f'\033[31mVOCÊ EXCEDEU O PERÍODO PARA JURAR BANDEIRA EM {tempo_excedente} ANO\033[m\n')
                else:
                    print(f'\033[31mVOCÊ EXCEDEU O PERÍODO PARA JURAR BANDEIRA EM {tempo_excedente} ANOS\033[m\n')
            elif idade_usuario == 18:
                print('TÁ FAZENDO O QUE PARADO AÍ?!?!?')
                print('\033[32mCORRE PARA IR JURAR BANDEIRA\033[m\n')
    except ValueError:
        print('Digite um valor válido')

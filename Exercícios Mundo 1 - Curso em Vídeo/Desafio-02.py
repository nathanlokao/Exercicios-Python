import calendar

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~<=Sua data de Aniversário=>~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

dia_nascimento = int (input('Qual é o seu dia de Nascimento?\n'))
mes_nascimento = int (input('Em qual mês você nasceu? (em número)\n'))
ano_nascimento = int (input('Seu ano de Nascimento:\n'))

calendario_dia = calendar.weekday(ano_nascimento, mes_nascimento, dia_nascimento)
calendario_mes = calendar.month_name[mes_nascimento]

dias_da_semana = {
    0 : 'Segunda-Feira',
    1 : 'Terça-Feira',
    2 : 'Quarta-Feira',
    3 : 'Quinta-Feira',
    4 : 'Sexta-Feira',
    5 : 'Sábado',
    6 : 'Domingo'
}

meses_do_ano = {
    'January' : 'Janeiro',
    'February' : 'Fevereiro',
    'March' : 'Março',
    'April' : 'Abril',
    'May' : 'Maio',
    'June' : 'Junho',
    'July' : 'Julho',
    'August' : 'Agosto',
    'September' : 'Setembro',
    'October' : 'Outubro',
    'November' : 'Novembro',
    'December' : 'Dezembro'
}

print(f'Você nasceu no dia {dia_nascimento} ({dias_da_semana.get(calendario_dia)}) no mês de {meses_do_ano.get(calendario_mes)} no ano de {ano_nascimento}')
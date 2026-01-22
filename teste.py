#  Programa ainda não finalizado, upado para trabalho contínuo

alunos  = {}
id = 1

def adicionar_aluno():
    global id
    nome = str(input('Digite o nome do Aluno: '))
    alunos[id] = {'nome' : nome}
    id += 1

def adicionar_notas():

    x = int(input('Escolha o aluno para atribuir as notas (ID): '))

    n1 = float(input('Digite a primeira nota: '))
    alunos[x]['n1'] = n1
    n2 = float(input('Digite a segunda nota: '))
    alunos[x]['n2'] = n2
    media = (n1 + n2) / 2
    alunos[x]['media'] = media

    print(f'A primeira nota: {n1} (ADICIONADO COM SUCESSO)')
    print(f'A segunda nota: {n2} (ADICIONADO COM SUCESSO)')
    print(f'A media das notas: {media} (ADICIONADO COM SUCESSO)')

def visualizar_alunos():

    for id, dados in alunos.items():
        print(f'Identificador: {id}, Nome do aluno: {dados['nome']}, Nota 1: {dados['n1']}, Nota 2: {dados['n2']}, Media: {dados['media']}')

while True:

    print('-' * 8, 'Menu', '-' * 8)
    print('1 - Adicionar Aluno\n2 - Visualizar Alunos Matriculados\n3 - Atribuir Nota\n0 - Encerrar Programa')
    
    try:
        escolha = int(input('Qual funcionalidade deseja executar?:\n'))

        if escolha == 1 :    
            adicionar_aluno()

        elif escolha == 2 :
            visualizar_alunos()

        elif escolha == 3 :
            adicionar_notas()

        elif escolha == 0 :
            break
    
    except ValueError:
        print('Digita direita ae!!! >:/')

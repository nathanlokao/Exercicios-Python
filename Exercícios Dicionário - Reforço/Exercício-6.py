aluno = {'nome': 'Ana', 'nota': 8.5, 'status': 'aprovado'}

# Solução menos performática que items()
# for chave in aluno:
#    valor = aluno[chave]
#    print(chave, valor)

for chave, valor in aluno.items():
   print(chave, valor)
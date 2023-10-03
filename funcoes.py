# Módulo para gerenciar o dicionário de alunos
alunos = {}

def AdicionarAluno():
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    alunos[matricula] = nome
    print(f"Aluno {nome} com matrícula {matricula} foi adicionado com sucesso!")

def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno que deseja remover: ")
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f"Aluno {nome} com matrícula {matricula} foi removido com sucesso!")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado no dicionário.")

def AtualizarAluno():
    matricula = input("Digite o número de matrícula do aluno que deseja atualizar: ")
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print(f"Nome do aluno com matrícula {matricula} foi atualizado para {novo_nome}.")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado no dicionário.")

def VerAlunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")

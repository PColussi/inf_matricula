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

# Exemplo de uso:
if __name__ == "__main__":
    while True:
        print("\nOpções:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Atualizar aluno")
        print("4. Ver alunos")
        print("5. Sair")
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            AdicionarAluno()
        elif escolha == "2":
            RemoverAluno()
        elif escolha == "3":
            AtualizarAluno()
        elif escolha == "4":
            VerAlunos()
        elif escolha == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

print(alunos)


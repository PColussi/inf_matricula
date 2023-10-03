from funcoes import *

dic_alunos = {}

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








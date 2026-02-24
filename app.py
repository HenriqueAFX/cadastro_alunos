import os

def limpar():
    os.system('clear')

alunos = ["henrique", "duda", "phablo"]
notas = [5.6, 8.9, 3.4]

# =====================================================

while True:
    limpar()
    menu = int(input("""[1] Cadastro de Alunos
[2] Informações de Alunos
[3] Modificar nota
[4] Média de notas
[0] Sair

Escolha uma opção: """))

    if menu == 1:
        while True:
            limpar()

            print("CADASTRO DE ALUNO\n\n")
            nome = input("Nome completo: ")
            nota = float(input("Nota: "))

            alunos.append(nome.replace(" ", "_").upper())
            notas.append(nota)

            op = 0
            op = int(input("\nDeseja cadastrar mais algum aluno? [1] Sim | [2] Não\n"))

            if op == 2:
                break

    elif menu == 2:
        while True:
            limpar()
            print("INFORMAÇÕES DE ALUNOS\n\n")

            if alunos == []:
                print("Não há alunos registrados.")
                input("\nPressione 'Enter' para voltar ao menu principal. ")
                break

            else:
                i = 0
                for n in alunos:
                    print(f"Matricula: {i+1}")
                    print(f"Nome: {alunos[i]}")
                    print(f"Nota: {notas[i]}\n")
                    i += 1

                input("\nPressione 'Enter' para voltar ao menu principal. ")
                break

    elif menu == 3:
        while True:
            limpar()
            print("MODIFICAR NOTAS DE ALUNOS\n\n")

            mat = int(input("Digite a matricula do aluno: "))
            i = mat-1

            limpar()
            print(f"Matricula: {mat}")
            print(f"Nome: {alunos[i]}")
            print(f"Nota: {notas[i]}\n")

            notas[i] = float(input("Digite a nova nota: "))
            
            limpar()
            print("Nota atualizada!\n")

            print(f"Matricula: {mat}")
            print(f"Nome: {alunos[i]}")
            print(f"Nota: {notas[i]}\n")

            op = 0
            op = int(input("\nDeseja atualizar a nota de mais algum aluno? [1] Sim | [2] Não\n"))

            if op == 2:
                break           
    elif menu == 4:
        while True:
            limpar()
            print("MÉDIA DE NOTAS DE ALUNOS\n\n")

            i = 0
            media = 0.0
            for n in notas:
                media = media + n
                i += 1

            media = media / i
            print(f"A média dos {i} alunos cadastrados é: {media:.2f}")

            input("\nPressione 'Enter' para voltar ao menu principal. ")
            break

    elif menu == 0:
        while True:
            limpar()
            print("Encerrando sistema...")
            
            input("\nPressione 'Enter' para iniciar o sistema. ")
            break
    
    else:
        print("Escolha inválida. Tente novamente.")
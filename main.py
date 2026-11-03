from datetime import datetime

atendimentos = []
proximo_id = 1


def cadastrar_atendimento():
    global proximo_id

    nome = input("Nome do cliente: ").strip()
    descricao = input("Descrição da solicitação: ").strip()

    if not nome or not descricao:
        print("Nome e descrição são obrigatórios.")
        return

    atendimento = {
        "id": proximo_id,
        "cliente": nome,
        "descricao": descricao,
        "status": "Aberto",
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    atendimentos.append(atendimento)
    proximo_id += 1
    print("Atendimento cadastrado com sucesso!")


def listar_atendimentos():
    if not atendimentos:
        print("Nenhum atendimento cadastrado.")
        return

    for item in atendimentos:
        print(f"\nID: {item['id']}")
        print(f"Cliente: {item['cliente']}")
        print(f"Solicitação: {item['descricao']}")
        print(f"Status: {item['status']}")
        print(f"Data: {item['data']}")


def atualizar_status():
    try:
        identificador = int(input("Digite o ID do atendimento: "))
    except ValueError:
        print("Digite um número válido.")
        return

    for item in atendimentos:
        if item["id"] == identificador:
            print("1 - Aberto\n2 - Em andamento\n3 - Concluído")
            opcao = input("Novo status: ")

            status = {
                "1": "Aberto",
                "2": "Em andamento",
                "3": "Concluído"
            }

            if opcao in status:
                item["status"] = status[opcao]
                print("Status atualizado!")
            else:
                print("Opção inválida.")
            return

    print("Atendimento não encontrado.")


def menu():
    while True:
        print("\n=== SISTEMA DE ATENDIMENTO ===")
        print("1 - Cadastrar atendimento")
        print("2 - Listar atendimentos")
        print("3 - Atualizar status")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_atendimento()
        elif opcao == "2":
            listar_atendimentos()
        elif opcao == "3":
            atualizar_status()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()

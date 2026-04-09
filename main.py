import json

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(tarefas, arquivo)

tarefas = carregar_tarefas()

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Deletar tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada!")

    elif opcao == "2":
        print("\nLista de tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i} - {tarefa}")

    elif opcao == "3":
        for i, tarefa in enumerate(tarefas):
            print(f"{i} - {tarefa}")

        try:
            indice = int(input("Digite o número da tarefa que deseja atualizar: "))

            if indice < 0 or indice >= len(tarefas):
                print("Índice inválido!")
                continue

            nova_tarefa = input("Digite a nova tarefa: ")
            tarefas[indice] = nova_tarefa
            salvar_tarefas(tarefas)
            print("Tarefa atualizada!")

        except ValueError:
            print("Digite um número válido!")

    elif opcao == "4":
        for i, tarefa in enumerate(tarefas):
            print(f"{i} - {tarefa}")

        try:
            indice = int(input("Digite o número da tarefa que deseja deletar: "))

            if indice < 0 or indice >= len(tarefas):
                print("Índice inválido!")
                continue

            tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print("Tarefa removida!")

        except ValueError:
            print("Digite um número válido!")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
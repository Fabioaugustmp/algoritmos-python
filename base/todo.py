# Função para adicionar uma tarefa
def adicionar_tarefa(lista, nome):
    lista.append(nome)
    print("Tarefa adicionada com sucesso!\n")

# Função para exibir todas as tarefas
def exibir_tarefas(lista):
    if not lista:
        print("Nenhuma tarefa cadastrada.\n")
    else:
        print("Tarefas:")
        for i in range(len(lista)):  # Índice começa em 0
            print(f"{i}. {lista[i]}")
        print()

# Função para remover uma tarefa pelo índice
def remover_tarefa(lista, indice):
    if 0 <= indice < len(lista):  # Verifica se o índice é válido
        tarefa_removida = lista.pop(indice)  # Remove a tarefa pelo índice
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!\n")
    else:
        print("Índice inválido. Nenhuma tarefa foi removida.\n")

# Função para buscar uma tarefa pelo nome
def buscar_tarefa(lista, nome):
    for tarefa in lista:
        if tarefa.lower() == nome.lower():
            print(f"Tarefa encontrada: {tarefa}\n")
            return
    print("Tarefa não encontrada.\n")

# Função principal para exibir o menu e gerenciar o programa
def gerenciador_tarefas():
    tarefas = []
    while True:
        print("=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Exibir tarefas")
        print("3. Remover tarefa")
        print("4. Buscar tarefa")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                nome = input("Informe o nome da tarefa: ")
                adicionar_tarefa(tarefas, nome)
            case "2":
                exibir_tarefas(tarefas)
            case "3":
                exibir_tarefas(tarefas)  # Mostra as tarefas antes de remover
                indice = int(input("Informe o identificador da tarefa que deseja remover: "))
                remover_tarefa(tarefas, indice)
            case "4":
                nome = input("Informe o nome da tarefa que deseja buscar: ")
                buscar_tarefa(tarefas, nome)
            case "5":
                print("Encerrando o programa. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.\n")

# Executar o programa
gerenciador_tarefas()

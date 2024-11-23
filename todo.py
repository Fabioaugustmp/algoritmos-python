# 1. Adicionar tarefa
# 2. Exibir tarefas
# 3. Remover tarefa
# 4. Buscar tarefa
# 5. Sair

def adicionar_tarefa(lista, nome):
    lista.append(nome)
    print(f"A sua atividade: [{nome}] foi adicionada a lista!")

def exibir_tarefa(lista):
    # O sistema deverá exibir todas as tarefas cadastradas, mostrando cada tarefa com
    # seu índice correspondente (iniciando em 0).
    # Caso não haja tarefas, o sistema deverá exibir a mensagem "Nenhuma tarefa
    # cadastrada.
    print()

def remover_tarefa(lista, indice):
    # O sistema permitirá remover uma tarefa pelo índice.
    # Se o índice informado for inválido (fora do intervalo da lista), o sistema deverá
    # notificar o usuário com a mensagem "Índice inválido. Nenhuma tarefa foi removida."
    # para remover basta utilizar a funcao pop()
    lista.pop(indice)
    print()

def buscar_tarefa(lista, indice):
    # O sistema permitirá ao usuário buscar uma tarefa pelo índice da tarefa.
    # Caso a tarefa seja encontrada, o sistema exibirá a mensagem "Tarefa encontrada:
    # [nome da tarefa]."
    # Se a tarefa não for encontrada, a mensagem exibida será "Tarefa não encontrada."
    print()

#Inicio
def gerenciador_tarefas():
    tarefas = []
    while True:
        print("=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Exibir tarefas")
        print("3. Remover tarefa")
        print("4. Buscar tarefa")
        print("5. Sair")

        escolha:int = int(input("Escolha uma opção: "))

        match escolha:
            case 1:
                nome = input("Informe o nome da tarefa: ")
                adicionar_tarefa(tarefas, nome)
            # case 2:
            # case 3:
            # case 4:
            case 5:
                print("Encerrando o programa, até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente! \n")

# Função que invoca o início do meu sistema.
gerenciador_tarefas()
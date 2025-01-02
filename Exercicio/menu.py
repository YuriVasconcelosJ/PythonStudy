def adicionar_tarefas(lista, tarefa):
    """Adiciona uma nova tarefa à lista"""
    lista.append(tarefa)
    print(f"A tarefa '{tarefa}' foi adicionada com sucesso")

def listas_tarefas(lista):
    """Exibe todas as tarefas da lista"""
    if not lista:
        print('Nenhuma tarefa listada')
    else:
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")


def remover_tarefas(lista, indice):
    """Remove uma tarefa selecionada pelo index"""
    if not lista:
        print('Nenhuma tarefa listada')
    else:
        if 0 <= indice < len(lista):
            tarefa_removida = lista.pop(indice)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso")
        else:
            print('Índice inválido. Por favor, tente novamente.')

def exibir_menu():
    """Exibe o menu"""
    print("\n=== Menu ===")
    print("\n=== Menu ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def main():
    """Função principal que gerencia o fluxo do programa"""
    listas_de_tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção")

        if opcao == "1":
            tarefa_input = input("Digite a tarefa")
            adicionar_tarefas(listas_tarefas, tarefa_input)
        elif opcao == '2':
            listas_tarefas(listas_tarefas)
        elif opcao == '3':
            try:
                indice = int(input('Digite o número da tarefa a ser removida'))
                remover_tarefas(listas_tarefas, indice)
            except ValueError:
                print('Por favor, digite um número válido')
        elif opcao == '4':
            print('Saindo do programa. Até logo!')
            break
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == 'main':
    main()
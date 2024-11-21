lista_tarefas = []

def adicionar_tarefa(nome, categoria, prioridade='media'):
    for tarefa in lista_tarefas:
        if tarefa['nome'] == nome:
            print(f"Tarefa '{nome}' já existe!")
            return
    
    # Validate prioridade input
    if prioridade.lower() not in ['baixa', 'media', 'alta']:
        print("Prioridade inválida! Use 'baixa', 'media' ou 'alta'.")
        return
    
    tarefa = {
        'nome': nome,
        'categoria': categoria,
        'prioridade': prioridade.lower(),
        'concluida': False
    }
    lista_tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada!")

def listar_tarefas():
    if not lista_tarefas:
        print("Não há tarefas cadastradas.")
        return
    
    for tarefa in sorted(lista_tarefas, key=lambda x: ['baixa', 'media', 'alta'].index(x['prioridade'])):
        status = " Ok " if tarefa['concluida'] else " "
        print(f"[{status}] {tarefa['nome']} | {tarefa['categoria']} | {tarefa['prioridade']}")

def concluir_tarefa(nome):
    for tarefa in lista_tarefas:
        if tarefa['nome'] == nome:
            tarefa['concluida'] = True
            print(f"Tarefa '{nome}' concluída!")
            return
    print("Tarefa não encontrada.")

def remover_tarefa(nome):
    for tarefa in lista_tarefas:
        if tarefa['nome'] == nome:
            lista_tarefas.remove(tarefa)
            print(f"Tarefa '{nome}' removida!")
            return
    print("Tarefa não encontrada.")

def menu():
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome da tarefa: ")
            while not nome.strip():
                print("Nome da tarefa não pode ser vazio!")
                nome = input("Nome da tarefa: ")
            
            categoria = input("Categoria: ")
            while not categoria.strip():
                print("Categoria não pode ser vazia!")
                categoria = input("Categoria: ")
            
            prioridade = input("Prioridade (baixa/media/alta): ") or 'media'
            adicionar_tarefa(nome, categoria, prioridade)
        
        elif opcao == '2':
            listar_tarefas()
        
        elif opcao == '3':
            nome = input("Nome da tarefa a concluir: ")
            concluir_tarefa(nome)
        
        elif opcao == '4':
            nome = input("Nome da tarefa a remover: ")
            remover_tarefa(nome)
        
        elif opcao == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

menu()
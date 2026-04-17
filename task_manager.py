task_list = []


def adicionar_tarefa(nome):
    task_list.append(nome)
    print(f'\nTarefa "{nome}", adcionada com sucesso!')
    print('\n' + '-' * 48)

def remover_tarefa(indice):
    try:
        posição = indice - 1
        valor_removido = task_list.pop(posição)
        print(f'\nTarefa "{valor_removido}", removida com sucesso!')
    except IndexError:
        print('\nErro: Esse número de tarefa não existe!')

def listar_tarefas():
    if not task_list:
        print('\nSua lista está vazia no momento!')
    else:
        print('\n--- Sua Lista de Tarefas ---')
        print()
        for i, tarefa in enumerate(task_list, start=1):
            print(f'{i}. {tarefa}')

def imprimir_lista():
    if not task_list:
        print('\nNão há nada para imprimir, a lista está vazia!')
        return
    with open('Lista de tarefas.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('--- Lista de Tarefas ---\n\n')
        for i, tarefa in enumerate(task_list, start=1):
            arquivo.write(f'{i}. {tarefa}\n')

    print('\n' + '-' * 48)
    print('\nSeu arquivo .txt, está pronto para impressão')

while True:
    print('\n' + '-' * 48)
    print()
    print('Lista de Tarefas'.center(45))
    print('\n1. Adicionar | 2. Remover | 3. Listar | 4. Imprimir | 5. Sair')
    
    try:
        resposta = int(input('\n')) 
    except ValueError:
        print('\n' + '-' * 48)
        print('\nPor favor, digite apenas números!')
        continue
    if resposta == 1:
        while True:
            new_task = input('\nDigite a nova tarefa, ou "Fim" para parar: ')
            if new_task.lower() == "fim":
                break
            elif new_task.strip() == "":
                print('\n' + '-' * 48)
                print('\nVocê não pode adicionar uma tarefa vazia!')
                print('\n' + '-' * 48)
            else:
                adicionar_tarefa(new_task)
    elif resposta == 2:
        while True:
            listar_tarefas()
            if not task_list:
                break

            entrada = input('\nDigite o número da tarefa que deseja remover, ou "Fim" para retornar: ')

            if entrada.lower() == "fim":
                break
            try:
                escolha = int(entrada)
                remover_tarefa(escolha)
            except ValueError:
                print('\n' + '-' * 48)
                print('\nErro: Por favor, digite apenas números ou "Fim"!')
                print('\n' + '-' * 48)
    
    elif resposta == 3:
        listar_tarefas()

    elif resposta == 4:
        imprimir_lista()

    else:
        break

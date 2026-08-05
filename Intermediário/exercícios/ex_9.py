#listar tarefas com possibilidade de refazer ou desfazer
todo = []
comandos = ["listar", "desfazer", "refazer"]
deletados = []
while True:
    comando = input('Comandos: listar, desfazer, refazer\nDigite uma tarefa ou comando:')

    if comando in comandos:
        if comando == "listar":
            for i in todo:
                print(i)
        elif comando == "desfazer":
            deletados.append(todo[-1])
            del todo[-1] 

        elif comando == "refazer":
            todo.append(deletados[0])
            del deletados[0]

    elif comando == "sair":
        break

    else:
        todo.append(comando)
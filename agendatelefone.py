agenda = {}
while True:
    print('---- Agenda Telefônica ----')
    print('1 - Adicionar contato', '\n2 - Editar telefone', '\n3 - Remover contato', '\n4 - Buscar contato', '\n5 - Listar todos', '\n6 - Sair')
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('---- ADICIONANDO CONTATO ----')
        nome = input('Digite o nome do contato: ')
        if nome not in agenda:
            agenda[nome] = input(f"Digite o telefone de {nome}: ")
            print(f'{nome} foi adicionado com sucesso!' )
            print(agenda) # Pra testar se está funcionando
        else:
            print('Já existe um contato cadastrado com esse nome!')

    elif opcao == '2':
        print('---- EDITANDO CONTATO ----')
        nome = input('Digite o nome do contato cadastrado: ')
        if nome in agenda:
            agenda[nome] = input(f'Digite o novo telefone de {nome}: ')
            print(f'Telefone de {nome} alterado com sucesso!')
        else:
            print('Não existe nenhum contato cadastrado com esse nome!')

    elif opcao == '3':
        print('---- REMOVENDO CONTATO ----')
        nome = input('Digite o nome do contato que deseja remover: ')
        if nome in agenda:
            del agenda[nome]
            print('Contato removido com sucesso!')
        else:
            print('Não existe nenhum contato cadastrado com esse nome!')

    elif opcao == '4':
        print('---- BUSCADOR DE CONTATO ----')
        nome = input('Digite o nome do contato que deseja buscar: ')
        if nome in agenda:
            print(f"Telefone: {agenda[nome]}")
        else:
            print('Esse contato não existe!')

    elif opcao == '5':
        print('--- CONTATOS DISPONÍVEIS ----')
        for key in agenda:
            print(f"Nome: {key} - Telefone: {agenda[nome]}")

    elif opcao == '6':
        print('Você saiu do programa!')
        break

    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE...')
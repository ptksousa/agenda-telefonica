from funcoes.funcoes import menu, cadastrar_contato


agenda = []

while True:
    # Menu formatado
    chave = menu()

    if chave == 1:
        # Cadastrar contato na agenda
        cadastrar_contato(agenda)

    elif chave == 2:
        # Remover contato da agenda

        print('-='*20)
        print('0 - RETORNAR AO MENU')

        # Agenda formatada para escolha do contato a ser deletado
        for i, f in enumerate(agenda):
            print(f'{i+1} - Nome: {f[0]}| Número: {f[1]}')

        while True:
            try:
                remover = int(input('Escolha o índice: '))

                if 0 <= remover <= len(agenda):
                    break
                else:
                    print('Escolha apenas números presentes nos índices.')

            except:
                print('Digíte apenas números presentes nos índices.')

        if remover == 0: 
            # Só para quebrar linha, já que o usuário deseja retornar ao menu.
            print() 
        else:
            # Remoção do item da agenda
            del agenda[remover-1]
    
    elif chave == 3:
        # Agenda formatada para visualização completa
        print('-='*20)
        for i, f in enumerate(agenda):
            print(f'{i+1} - Nome: {f[0]} | Número: {f[1]}')
        input('Pressione ENTER.')
    
    elif chave == 4:
        # Fim do programa
        break
    
    else:
        input('Escolha números existentes nos índices do menu. (PRESSIONE ENTER)')

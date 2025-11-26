from funcoes.funcoes import menu, cadastrar_contato


agenda = []

while True:
    chave = menu()

    if chave == 1:
        cadastrar_contato(agenda)

    elif chave == 2:
        print('-='*20)
        print('0 - RETORNAR AO MENU')
        for i, f in enumerate(agenda):
            print(f'{i+1} - Nome: {f[0]}| Número: {f[1]}')
        remover = int(input('Escolha o índice: '))
        if remover == 0: 
            print()
        else:
            del agenda[remover-1]
    
    elif chave == 3:
        print('-='*20)
        for i, f in enumerate(agenda):
            print(f'{i+1} - Nome: {f[0]}| Número: {f[1]}')
        input('Pressione ENTER.')
    
    elif chave == 4:
        break
    
    else:
        input('Escolha números existentes nos índices do menu. (PRESSIONE ENTER)')

def menu():
    print('-='*20)
    print('MENU'.center(40))
    print('-='*20)
    print('[ 1 ] CADASTRAR CONTATO')
    print('[ 2 ] REMOVER CONTATO')
    print('[ 3 ] VER AGENDA')
    print('[ 4 ] SAIR')
    while True:
        try:
            opcao = int(input('ESCOLHA UMA OPÇÃO: '))
            if opcao in range(1,5):
                return opcao
        except:
            print('Digíte apenas números.')
        else:
            print('Somente números de 1 a 4.')



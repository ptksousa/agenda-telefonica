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
            chave = int(input('Escolha uma opção: '))
            if chave < 5 and chave > 0:
                return chave
            else:
                print('Escolha apenas números presentes nos índices do menu.')
        except:
            print('Digíte apenas números presentes no índice do menu.')


def cadastrar_contato(lista):
    print('-='*20)
    nome = input('Digíte o nome: ').upper()
    while True:
        try:
            numero = int(input('Digíte o número: '))
            break
        except:
            print('Dígite um número de telefone válido')
    contato = []
    contato.append(nome)
    contato.append(numero)
    lista.append(contato[:])
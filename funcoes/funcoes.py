def menu():
    print('-='*20)
    print('MENU'.center(40))
    print('-='*20)
    print('[ 1 ] CADASTRAR CONTATO')
    print('[ 2 ] REMOVER CONTATO')
    print('[ 3 ] VER AGENDA')
    print('[ 4 ] SAIR')

    chave = int(input('Escolha uma opção: '))
    return chave


def cadastrar_contato(lista):
    print('-='*20)
    nome = input('Digíte o nome: ').upper()
    numero = int(input('Digíte o número: '))
    contato = []
    contato.append(nome)
    contato.append(numero)
    lista.append(contato[:])
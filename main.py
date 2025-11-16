from funcoes.funcoes import menu

agenda = []

escolha = menu()

if escolha == 1:
    while True: 
        contato = []
        nome = input('Digíte o nome: ')
        numero = int(input('Digíte o número de telefone: '))
        contato.append(nome)
        contato.append(numero)
        agenda.append(contato[:])
        break
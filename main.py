from fila import *
from cliente import *

def menu():
    fila = FilaAtendimento()

    while True:
        print('\n--- MENU DE ATENDIMENTO ---')
        print('1. Adicionar cliente comum')
        print('2. Adicionar cliente VIP')
        print('3. Atender próximo cliente')
        print('4. Ver fila')
        print('5. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Nome do cliente comum: ')
            fila.adicionar_cliente(Cliente(nome))
        
        elif opcao == '2':
            nome = input('Nome do cliente VIP: ')
            fila.adicionar_cliente(Cliente(nome, vip=True))

        elif opcao == '3':
            fila.atender_cliente()
        
        elif opcao == '4':
            fila.listar_fila()

        elif opcao == '5':
            print('Encerrando o sistema.')
            break

        else:
            print('Opção inválida.')

if __name__ == '__main__':
    print('Sistema de Atendimento Iniciado!')
    menu()             
class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, cliente):
        if cliente.vip:
            self.fila.insert(0, cliente)
        else:
            self.fila.append(cliente)
    
    def atender_cliente(self):
        if self.fila:
            cliente = self.fila.pop(0)
            print(f'Atendendo: {cliente}')
        else:
            print(f'Fila vazia!')

    def listar_fila(self):
        if not self.fila:
            print('A fila está vazia!')
        else:
            print(f'Fila de atendimento:')
            for i, cliente in enumerate(self.fila, 1):
                print(f'{i}. {cliente}')
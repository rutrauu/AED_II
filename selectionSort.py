class Node:
    def __init__(self, numero):
        self.valor = numero
        self.next = None

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_valor(self, valor):
        novo_no = Node(valor)

        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.next = novo_no
            self.tail = novo_no


    def imprime_lista(self):
        if self.head is None:
            print("A lista está vazia.")
            return

        valores_da_lista = []
        no_atual = self.head

        while no_atual is not None:
            valores_da_lista.append(no_atual.valor)
            no_atual = no_atual.next

        print(valores_da_lista)


    def ordena_selection(self):
        # Se a lista estiver vazia ou tiver apenas um elemento, não há nada a ordenar.
        if self.head is None or self.head.next is None:
            return

        # 'left' percorre a lista. Ele marca o início da porção não ordenada.
        left = self.head
        while left is not None:
            # 'minval' guarda o nó com o menor valor encontrado na porção não ordenada.
            # Começamos assumindo que o nó atual é o menor.
            minval = left
            
            # 'right' percorre a lista a partir do próximo nó para encontrar o menor valor.
            right = left.next
            while right is not None:
                if right.valor < minval.valor:
                    minval = right
                right = right.next
            
            # Após encontrar o menor nó, troca os valores com o nó da posição atual.
            left.valor, minval.valor = minval.valor, left.valor
            
            # Avança para o próximo elemento da lista.
            left = left.next


lista_desordenada = [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]
lista = Lista()
for numero in lista_desordenada:
    lista.add_valor(numero)

print("Lista Desordenada.")
lista.imprime_lista()

# Chamando o novo método de ordenação Selection Sort
lista.ordena_selection()

print("\nLista Ordenada.")
lista.imprime_lista()
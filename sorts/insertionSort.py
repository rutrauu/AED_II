import time

class Node:
    def __init__(self, numero):
        self.valor = numero
        self.next = None
        self.prev = None

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
            novo_no.prev = self.tail
            self.tail = novo_no

    def imprime_lista(self):
        if self.head is None:
            print("A lista está vazia.")
        else:
            atual = self.head
            res = []
            while atual is not None:
                res.append(atual.valor)
                atual = atual.next
            print(res)

    def ordena_insertion(self):
        if self.head is None or self.head.next is None:
            return

        atual = self.head.next
        while atual is not None:
            value = atual.valor
            move = atual.prev

            while move is not None and move.valor > value:
                move.next.valor = move.valor
                move = move.prev

            if move is None:
                self.head.valor = value
            else:
                move.next.valor = value

            atual = atual.next

lista_desordenada = [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]
lista = Lista()
for numero in lista_desordenada:
    lista.add_valor(numero)

print("Lista Desordenada:")
lista.imprime_lista()

# inicio = time.time()
lista.ordena_insertion()
# fim = time.time()

print("Lista Ordenada com Insertion Sort:")
lista.imprime_lista()

# print(f"Tempo de execução: {fim - inicio:.6f} segundos")
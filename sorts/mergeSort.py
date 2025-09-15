import time
class Node:
    def __init__(self, numero):
        self.value = numero
        self.next = None
        self.prev = None

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_valor(self, value):
        novo_no = Node(value)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.next = novo_no
            novo_no.prev = self.tail
            self.tail = novo_no

    def printList(self):
        if self.head is None:
            print("A lista está vazia.")
        else:
            atual = self.head
            while atual is not None:
                print(f"Valor: {atual.value}")
                atual = atual.next

    def mergeSort(self):
        self.head = self._merge_sort(self.head)
        # Atualiza tail após ordenação
        atual = self.head
        prev = None
        while atual:
            atual.prev = prev
            prev = atual
            if atual.next is None:
                self.tail = atual
            atual = atual.next

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        meio = self._split(head)
        left = self._merge_sort(head)
        right = self._merge_sort(meio)

        return self._merge(left, right)

    def _split(self, head):
        lento = head
        rapido = head

        while rapido.next and rapido.next.next:
            lento = lento.next
            rapido = rapido.next.next

        meio = lento.next
        lento.next = None
        if meio:
            meio.prev = None
        return meio

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.value <= right.value:
            resultado = left
            resultado.next = self._merge(left.next, right)
            if resultado.next:
                resultado.next.prev = resultado
        else:
            resultado = right
            resultado.next = self._merge(left, right.next)
            if resultado.next:
                resultado.next.prev = resultado

        resultado.prev = None
        return resultado


lista_desordenada = [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]
lista = Lista()
for numero in lista_desordenada:
    lista.add_valor(numero)

print("Lista Desordenada:")
lista.printList()

# inicio = time.time()
lista.mergeSort()
# fim = time.time()
print("Lista Ordenada com Insertion Sort:")
lista.printList()

# print(f"Tempo de execução: {fim - inicio:.6f} segundos")


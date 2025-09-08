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
            while atual is not None:
                print(f"Valor: {atual.valor}")
                atual = atual.next


    def ordena_quick(self):
        self._quick_sort(self.head, self.tail)

    def _quick_sort(self, inicio, fim):
        if inicio is not None and fim is not None and inicio != fim and inicio != fim.next:
            pivo = self._particiona(inicio, fim)
            self._quick_sort(inicio, pivo.prev)
            self._quick_sort(pivo.next, fim)

    def _particiona(self, inicio, fim):
        pivo_valor = fim.valor
        i = inicio.prev
        j = inicio

        while j != fim:
            if j.valor <= pivo_valor:
                i = i.next if i else inicio
                i.valor, j.valor = j.valor, i.valor
            j = j.next

        i = i.next if i else inicio
        i.valor, fim.valor = fim.valor, i.valor
        return i


lista = Lista()
for numero in [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]:
    lista.add_valor(numero)

print("Lista Desordenada:")
lista.imprime_lista()
# inicio = time.time()
lista.ordena_quick()
# fim = time.time()
print("Lista Ordenada com Quick Sort:")
lista.imprime_lista()

# print(f"Tempo de execução: {fim - inicio:.6f} segundos")


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

    def ordena_merge(self):
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

        meio = self._divide(head)
        esquerda = self._merge_sort(head)
        direita = self._merge_sort(meio)

        return self._merge(esquerda, direita)

    def _divide(self, head):
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

    def _merge(self, esquerda, direita):
        if esquerda is None:
            return direita
        if direita is None:
            return esquerda

        if esquerda.valor <= direita.valor:
            resultado = esquerda
            resultado.next = self._merge(esquerda.next, direita)
            if resultado.next:
                resultado.next.prev = resultado
        else:
            resultado = direita
            resultado.next = self._merge(esquerda, direita.next)
            if resultado.next:
                resultado.next.prev = resultado

        resultado.prev = None
        return resultado


lista_desordenada = [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]
lista = Lista()
for numero in lista_desordenada:
    lista.add_valor(numero)

print("Lista Desordenada:")
lista.imprime_lista()

# inicio = time.time()
lista.ordena_merge()
# fim = time.time()
print("Lista Ordenada com Insertion Sort:")
lista.imprime_lista()

# print(f"Tempo de execução: {fim - inicio:.6f} segundos")


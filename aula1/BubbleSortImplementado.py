class No:
    def __init__(self, num) -> None:
        self.valor = num
        self.proximo = None


class Lista:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        """Insere um novo nó no final da lista"""
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def exibir(self):
        """Exibe a lista como array"""
        elementos = []
        atual = self.inicio
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        print(elementos)

    def tamanho(self):
        """Retorna o tamanho da lista encadeada"""
        count = 0
        atual = self.inicio
        while atual:
            count += 1
            atual = atual.proximo
        return count

    def bubbleSort(self):
        """Ordena a lista encadeada usando Bubble Sort com for"""
        n = self.tamanho()
        for i in range(n - 1):
            atual = self.inicio
            for j in range(n - i - 1):
                if atual.valor > atual.proximo.valor:
                    atual.valor, atual.proximo.valor = atual.proximo.valor, atual.valor
                atual = atual.proximo


# -------------------------
# Exemplo de uso
# -------------------------
valores = [5, 10, 14, 18, 20, 13, 27, 29, 19, 15, 37, 3, 72, 81]

lista = Lista()
for v in valores:
    lista.inserir(v)

print("Lista antes da ordenação:")
lista.exibir()

lista.bubbleSort()

print("Lista depois da ordenação:")
lista.exibir()

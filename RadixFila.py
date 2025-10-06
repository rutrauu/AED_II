# -*- coding: utf-8 -*-

from collections import deque

class Fila:
    """
    Uma implementação simples de uma estrutura de dados de Fila (Queue)
    usando collections.deque para eficiência.
    """
    def __init__(self):
        self._items = deque()

    def is_empty(self):
        """Retorna True se a fila estiver vazia, False caso contrário."""
        return not self._items

    def enqueue(self, item):
        """Adiciona um item ao final da fila."""
        self._items.append(item)

    def dequeue(self):
        """Remove e retorna o item do início da fila."""
        if self.is_empty():
            raise IndexError("dequeue de uma fila vazia")
        return self._items.popleft()

    def __len__(self):
        """Retorna o número de itens na fila."""
        return len(self._items)

class RadixSort:
    """
    Implementação do algoritmo RadixSort (LSD - Least Significant Digit)
    de forma orientada a objetos, usando Filas como baldes.
    Esta implementação funciona para inteiros não negativos.
    """
    def __init__(self, dados):
        # Valida se todos os itens são inteiros não negativos
        for item in dados:
            if not isinstance(item, int) or item < 0:
                raise ValueError("RadixSort nesta implementação só funciona com inteiros não negativos.")
        
        # Cria uma cópia da lista para não modificar a original
        self.dados = list(dados)

    def sort(self):
        """
        Executa o algoritmo RadixSort.
        """
        if not self.dados:
            return []

        # 1. Encontrar o número máximo para saber o número de dígitos
        max_num = max(self.dados)

        # 2. Fazer a ordenação para cada casa decimal (dígito)
        # A variável 'place' representa a casa atual (1, 10, 100, ...)
        place = 1
        while max_num // place > 0:
            
            # --- Fase de Distribuição ---
            # Cria 10 baldes (filas), um para cada dígito (0-9)
            buckets = [Fila() for _ in range(10)]
            
            # Coloca cada número no balde correspondente
            for num in self.dados:
                # Calcula o dígito na casa decimal 'place'
                digit = (num // place) % 10
                buckets[digit].enqueue(num)
            
            # --- Fase de Coleta ---
            # Esvazia os baldes de volta para a lista, na ordem
            i = 0
            for bucket in buckets:
                while not bucket.is_empty():
                    self.dados[i] = bucket.dequeue()
                    i += 1
            
            # Move para a próxima casa decimal
            place *= 10
            
        return self.dados

    def display(self):
        """Exibe os dados atuais."""
        print(self.dados)

# --- Exemplo de Uso ---
if __name__ == "__main__":
    lista_desordenada = [170, 45, 75, 90, 802, 24, 2, 66]
    
    print("Lista Original:")
    print(lista_desordenada)
    
    # Cria uma instância do RadixSort com a lista
    sorter = RadixSort(lista_desordenada)
    
    # Chama o método de ordenação
    lista_ordenada = sorter.sort()
    
    print("\nLista Ordenada:")
    print(lista_ordenada)

    # Exemplo com lista maior e com números de diferentes qtd de dígitos
    outra_lista = [432, 8, 530, 90, 88, 231, 11, 45, 677, 199]
    print("\nOutra Lista Original:")
    print(outra_lista)
    
    sorter_2 = RadixSort(outra_lista)
    lista_ordenada_2 = sorter_2.sort()
    
    print("\nOutra Lista Ordenada:")
    print(lista_ordenada_2)

    # Exemplo de erro com número negativo
    try:
        lista_com_negativo = [10, 20, -5, 30]
        sorter_erro = RadixSort(lista_com_negativo)
    except ValueError as e:
        print(f"\nTeste de erro (esperado): {e}")
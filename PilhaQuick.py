# -*- coding: utf-8 -*-

class Pilha:
    """
    Uma implementação simples de uma estrutura de dados de Pilha (Stack).
    Utiliza uma lista Python internamente, expondo apenas as operações
    fundamentais de uma pilha.
    """
    def __init__(self):
        self._items = []

    def is_empty(self):
        """Retorna True se a pilha estiver vazia, False caso contrário."""
        return not self._items

    def push(self, item):
        """Adiciona um item ao topo da pilha."""
        self._items.append(item)

    def pop(self):
        """Remove e retorna o item do topo da pilha."""
        if self.is_empty():
            raise IndexError("pop de uma pilha vazia")
        return self._items.pop()

    def peek(self):
        """Retorna o item do topo da pilha sem removê-lo."""
        if self.is_empty():
            raise IndexError("peek de uma pilha vazia")
        return self._items[-1]

    def __len__(self):
        """Retorna o número de itens na pilha."""
        return len(self._items)

class QuickSort:
    """
    Implementação do algoritmo QuickSort de forma iterativa usando uma Pilha
    para gerenciar os sub-arrays a serem ordenados.
    """
    def __init__(self, dados):
        # Cria uma cópia da lista para não modificar a original
        self.dados = list(dados)

    def _partition(self, low, high):
        """
        Esta função escolhe o último elemento como pivô, posiciona o pivô
        em sua posição correta na lista ordenada e coloca todos os menores
        (menores que o pivô) à sua esquerda e todos os maiores à sua direita.
        """
        # Define o pivô como o último elemento do sub-array
        pivo = self.dados[high]
        
        # i é o índice do último elemento menor que o pivô encontrado
        i = low - 1

        for j in range(low, high):
            # Se o elemento atual for menor ou igual ao pivô
            if self.dados[j] <= pivo:
                # Incrementa o índice do menor elemento
                i += 1
                # Troca dados[i] com dados[j]
                self.dados[i], self.dados[j] = self.dados[j], self.dados[i]
        
        # Coloca o pivô em sua posição final correta
        # trocando-o com o elemento seguinte ao último menor encontrado
        self.dados[i + 1], self.dados[high] = self.dados[high], self.dados[i + 1]
        
        # Retorna o índice onde o pivô foi colocado
        return i + 1

    def sort(self):
        """
        Executa o algoritmo QuickSort de forma iterativa.
        """
        if not self.dados:
            return []

        # Cria a pilha para armazenar os índices dos sub-arrays
        pilha = Pilha()
        
        # Define os limites iniciais (a lista inteira)
        low = 0
        high = len(self.dados) - 1
        
        # Empilha o primeiro "trabalho" (ordenar a lista inteira)
        pilha.push((low, high))
        
        # O loop continua enquanto houver sub-arrays para processar na pilha
        while not pilha.is_empty():
            # Desempilha os índices de início (low) e fim (high) do sub-array atual
            low, high = pilha.pop()
            
            # Se houver mais de um elemento no sub-array, particiona
            if low < high:
                # Encontra o índice do pivô, particionando o sub-array
                pi = self._partition(low, high)
                
                # Após a partição, temos dois sub-arrays para ordenar:
                # 1. Elementos antes do pivô: [low, pi - 1]
                # 2. Elementos depois do pivô: [pi + 1, high]

                # Empilha o sub-array da esquerda se ele tiver elementos
                if pi - 1 > low:
                    pilha.push((low, pi - 1))
                
                # Empilha o sub-array da direita se ele tiver elementos
                if pi + 1 < high:
                    pilha.push((pi + 1, high))
        
        return self.dados

    def display(self):
        """Exibe os dados atuais."""
        print(self.dados)

# --- Exemplo de Uso ---
if __name__ == "__main__":
    lista_desordenada = [10, 80, 30, 90, 40, 50, 70, 2, 15, 55]
    
    print("Lista Original:")
    print(lista_desordenada)
    
    # Cria uma instância do QuickSort com a lista
    sorter = QuickSort(lista_desordenada)
    
    # Chama o método de ordenação
    lista_ordenada = sorter.sort()
    
    print("\nLista Ordenada:")
    print(lista_ordenada)

    # Exemplo com lista maior e elementos repetidos
    outra_lista = [5, 3, 8, 4, 2, 7, 1, 10, 5, 9, 6, 6]
    print("\nOutra Lista Original:")
    print(outra_lista)
    
    sorter_2 = QuickSort(outra_lista)
    lista_ordenada_2 = sorter_2.sort()
    
    print("\nOutra Lista Ordenada:")
    print(lista_ordenada_2)
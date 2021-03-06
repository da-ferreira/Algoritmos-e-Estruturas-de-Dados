
"""
Autor: David Ferreira de Almeida

Algoritmo de ordenação Selection Sort
Complexidade: O(n²)
Categoria: Algoritmo Guloso
"""

def selection_sort(array):
    """
    :param array: lista a ser ordenada
    :return: None
    """
    
    for i in range(len(array)):
        posicao_menor = i

        for j in range(i + 1, len(array)):  # acumulando a área dos números sorteados
            if array[j] < array[posicao_menor]:
                posicao_menor = j
        
        array[i], array[posicao_menor] = array[posicao_menor], array[i]  # trocando menor com maior

          

"""
Búsqueda binaria iterativa (requiere lista ordenada).

Divide el espacio de búsqueda a la mitad en cada paso.

Args:
    lst: Lista ordenada de elementos a buscar.
    target: Elemento a encontrar.

Returns:
    Índice del elemento si se encuentra, -1 en caso contrario.

Complejidad:
    Tiempo: O(log n)  |  Espacio: O(1)
"""

def binary_search(lst: list, target) -> int:

    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
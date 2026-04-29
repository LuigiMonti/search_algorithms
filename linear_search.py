"""
Búsqueda lineal iterativa.

Recorre la lista elemento por elemento hasta encontrar el target.

Args:
    lst: Lista de elementos a buscar.
    target: Elemento a encontrar.

Returns:
    Índice del elemento si se encuentra, -1 en caso contrario.

Complejidad:
    Tiempo: O(n)  |  Espacio: O(1)
"""

def linear_search(lst: list, target) -> int:

    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1
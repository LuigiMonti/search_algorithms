import pytest
from binary_search import binary_search

def test_encontrado_inicio():
    assert binary_search([1, 2, 3, 4, 5], 1) == 0

def test_encontrado_final():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4

def test_encontrado_medio():
    assert binary_search([10, 20, 30, 40, 50], 30) == 2

def test_no_encontrado():
    assert binary_search([1, 2, 3], 99) == -1

def test_lista_vacia():
    assert binary_search([], 5) == -1
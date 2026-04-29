# test_bench.py

import pytest
from linear_search import linear_search
from binary_search import binary_search

DATA = list(range(100_000))  # lista ordenada de 0 a 99,999
TARGET = -1                  # no existe en DATA → peor caso para ambos


def run_search(search_function):
    return search_function(DATA, TARGET)


def test_linear(benchmark):
    benchmark.pedantic(
        run_search,
        args=(linear_search,),
        rounds=5,
        iterations=5
    )


def test_binary(benchmark):
    benchmark.pedantic(
        run_search,
        args=(binary_search,),
        rounds=5,
        iterations=5
    )


# Para correrlo:
# pytest test_bench.py -v --benchmark-enable
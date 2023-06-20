"""Módulo com as funções de manipulação de matrizes."""
import math

import numpy as np

from tipos import Escalar, Matriz


def soma(x: Matriz, y: Matriz) -> Matriz | None:
    """Soma duas matrizes"""
    if len(x) != len(y) or len(x[0]) != len(y[0]):
        return []
    rows = len(x)
    columns = len(x[0])
    soma_matrizes = [[0.0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            soma_matrizes[i][j] = x[i][j] + y[i][j]
    return soma_matrizes

def multiplying_by_scalar(matriz: Matriz, escalar: Escalar) -> Matriz:
    """Multiplicando por um escalar"""
    rows = len(matriz)
    columns = len(matriz[0])
    conta = [[0.0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            conta[i][j] = matriz[i][j] * escalar


def multiplication(x: Matriz, y: Matriz) -> Matriz | None:
    """"Multiplicando matrizes"""
    if len(x[0]) != len(y):
        return None

    result = [[0.0 for _ in enumerate(y[0])] for _ in enumerate(x)]
    for i in enumerate(x):
        for j in enumerate(y[0]):
            for k in enumerate(y):
                result[i][j] += x[i][k] * y[k][j]

    return result

def norma(x: Matriz) -> Escalar:
    """Calcula a norma de uma matriz"""
    if len(x) == 0 or len(x[0]) == 0:
        return None
    quadrado_soma = 0.0
    for i in x:
        for element in i:
            quadrado_soma += element**2
    norma_calculada = math.sqrt(quadrado_soma)
    return norma_calculada


def is_simmetric(x: Matriz) -> bool:
    """Verifica se uma matriz é simétrica"""
    matrix = np.array(x)
    transpose_matrix = np.transpose(matrix)
    return np.array_equal(matrix, transpose_matrix)


def transposta(x: Matriz) -> Matriz:
    """Calcula a transposta de uma matriz"""
    transposed_matrix = np.transpose(x)
    return transposed_matrix.tolist()

matriz_t1 = [1, 2]
matriz_t2 = [2, 3]
print(soma(matriz_t1, matriz_t2))
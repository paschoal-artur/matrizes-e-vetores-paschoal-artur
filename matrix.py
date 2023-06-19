"""Módulo com as funções de manipulação de matrizes."""
import math
import numpy as np
from typing import List

def soma(x: list[list[float]], y: list[list[float]]) -> list[list[float]] | None:
    """Soma duas matrizes"""
    if len(x) != len(y) or len(x[0]) != len(y[0]):
        return None
    rows = len(x)
    columns = len(x[0])
    soma_matrizes = [[0.0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            soma_matrizes[i][j] = x[i][j] + y[i][j]
    return soma_matrizes

def multiplicação_por_escalar(matriz: list[list[float]], escalar: float) -> list[list[float]]:
    """Multiplica uma matriz por um escalar"""
    rows = len(matriz)
    columns = len(matriz[0])
    conta = [[0.0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            conta[i][j] = matriz[i][j] * escalar

def multiplicação(x: list[list[float]], y: list[list[float]]) -> list[list[float]] | None:
    """Multiplica duas matrizes"""
    # TODO: implementar
    # a multiplicação de duas matrizes [[1, 2, 4], [2, 3, 4]] por [[2, 3, 4], [1, 2, 4]] é [[10, 17, 28], [12, 20, 32]]
    # a multiplicação só pode ser realizada se a quantidade de colunas da primeira matriz é igual a quantidade de linhas da segunda matriz.
    # caso contrário, deve retornar None


def norma(x: list[list[float]]) -> float:
    """Calcula a norma de uma matriz"""
    if len(x) == 0 or len(x[0]) == 0:
        return None
    quadrado_soma = 0.0
    for i in x:
        for element in i:
            quadrado_soma += element ** 2
    norma = math.sqrt(quadrado_soma)
    return norma

def é_simétrica(x: list[list[float]]) -> bool:
    """Verifica se uma matriz é simétrica"""
    matrix = np.array(x)
    transpose_matrix = np.transpose(matrix)
    return np.array_equal(matrix, transpose_matrix)

def transposta(x: list[list[float]]) -> list[list[float]]:
    """Calcula a transposta de uma matriz"""
    transposed_matrix = np.transpose(x)
    return transposed_matrix.tolist()

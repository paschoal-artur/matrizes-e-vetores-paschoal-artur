"""Módulo com as funções de manipulação de vetores."""
import math

import numpy as np

from tipos import Escalar, Matriz, Vetor


def norma(x: Vetor) -> Escalar | None:
    """Calcula a norma de um vetor"""
    if x == []:
        return None

    quadrado_soma = 0.0

    for element in x:
        quadrado_soma += element**2

    norma_calculada = math.sqrt(quadrado_soma)

    return norma_calculada


def soma(x: Vetor, y: Vetor) -> Vetor | None:
    """Soma dois vetores"""
    if len(x) != len(y):
        return None

    soma_vetores = []

    for i, x_i in enumerate(x):
        soma_vetores.append(x_i + y[i])

    return soma_vetores


def multiplicacao_por_escalar(vetor: Vetor, escalar: Escalar) -> Vetor:
    """Multiplicando por escalar"""
    vetor_multiplicado = [element * escalar for element in vetor]

    return vetor_multiplicado


def produto_interno(x: Vetor, y: Vetor) -> Escalar | None:
    """Calcula o produto interno de dois vetores"""
    if len(x) != len(y):
        return None

    if x == [] and y == []:
        return 0

    produto_vetores = 0.0

    for i, x_i in enumerate(x):
        produto_vetores += x_i * y[i]

    return produto_vetores


def produto_vetorial(x: Vetor, y: Vetor) -> Vetor | None:
    """Calcula o produto vetorial de dois vetores"""
    if len(x) != 3 or len(y) != 3:
        return None

    resultado = np.cross(x, y)

    return resultado.tolist()


def produto_diadico(x: Vetor, y: Vetor) -> Matriz | None:
    """Calculo do produto diadico"""
    if len(x) == 0 or len(y) == 0:
        return []

    if len(x) != len(y):
        return None

    result = []

    for x_i in x:
        row = []
        for y_j in y:
            row.append(x_i * y_j)
        result.append(row)

    return result

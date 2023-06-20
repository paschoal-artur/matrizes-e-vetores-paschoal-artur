"""Módulo com as funções de manipulação de vetores."""
import math

import numpy as np

import tipos


def norma(x: list[float]) -> float | None:
    """Calcula a norma de um vetor"""
    if x == 0:
        return None
    quadrado_soma = 0.0
    for element in x:
        quadrado_soma += element**2
    norma_calculada = math.sqrt(quadrado_soma)
    return norma_calculada


def soma(x: list[float], y: list[float]) -> list[float] | None:
    """Soma dois vetores"""
    if len(x) != len(y):
        return None
    soma_vetores = []
    for i in enumerate(x):
        soma_vetores.append(x[i] + y[i])
    return soma_vetores


def multiplying_by_scalar(vetor: list[float], escalar: float) -> list[float]:
    vetor_multiplicado = [element * escalar for element in vetor]
    return vetor_multiplicado


def produto_interno(x: list[float], y: list[float]) -> float | None:
    """Calcula o produto interno de dois vetores"""
    if len(x) != len(y):
        return None
    produto_vetores = 0.0
    for i in enumerate(x):
        produto_vetores += x[i] * y[i]
    return produto_vetores


def produto_vetorial(x: list[float], y: list[float]) -> list[float] | None:
    """Calcula o produto vetorial de dois vetores"""
    if len(x) != 3 or len(y) != 3:
        return None
    resultado = np.cross(x, y)
    return resultado.tolist()


def produto_diadico(x: list[float], y: list[float]) -> list[list[float]] | None:
    if not x and not y:
        print("Hello world")

"""Módulo com as funções de manipulação de vetores."""
import math
from typing import List

def norma(x: list[float]) -> float | None:
    """Calcula a norma de um vetor"""
    if x == 0:
      return None
    quadrado_soma = 0.0
    for element in x:
        quadrado_soma += element ** 2
    norma = math.sqrt(quadrado_soma)
    return norma

def soma(x: list[float], y: list[float]) -> list[float] | None:
    """Soma dois vetores"""
    if len(x) != len(y) :
        return None
    soma_vetores = []
    for i in range(len(x)):
        soma_vetores.append(x[i] + y[i])
    return soma_vetores

def multiplicação_por_escalar(vetor: list[float], escalar: float) -> list[float]:
    """Multiplica um vetor por um escalar"""
    vetor_multiplicado = [element * escalar for element in vetor]
    return vetor_multiplicado
    # TODO: implementar
    # a multiplicação de um vetor [1, 2, 4] por um escalar 2 é [2, 4, 8]


def produto_interno(x: list[float], y: list[float]) -> float | None:
    """Calcula o produto interno de dois vetores"""
    if len(x) != len(y):
        return None
    produto_vetores = 0.0
    for i in range(len(x)):
        produto_vetores += x[i] * y[i]
    return produto_vetores

def produto_vetorial(x: list[float], y: list[float]) -> list[float] | None:
    """Calcula o produto vetorial de dois vetores"""
    # TODO: implementar
    # o produto vetorial de dois vetores [1, 2, 4] e [2, 3, 4] é [-4, 4, -1]
    # o produto vetorial só pode ser realizado se os vetores tem 3 elementos.
    # caso contrário, deve retornar None


def produto_diádico(x: list[float], y: list[float]) -> list[list[float]] | None:
    """Calcula o produto diádico de dois vetores"""
    # TODO: implementar
    # o produto diádico de dois vetores [1, 2, 4] e [2, 3, 4] é [[2, 3, 4], [4, 6, 8], [8, 12, 16]]
    # o produto diádico só pode ser realizado se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None

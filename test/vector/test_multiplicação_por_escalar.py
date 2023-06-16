"""Esse arquivo testa o arquivo vector.py"""

import unittest  # for creating the test case
from vector import multiplicação_por_escalar as multi


class TestVectorMultiplicaçãoPorEscalar(unittest.TestCase):
    """Classe para testar a função multiplicação_por_escalar no arquivo vector.py"""

    def test_multiplicação_por_escalar_vazia(self):
        """Testa se a resposta é vazia para vetores vazios"""
        self.assertEqual(multi([], 2), [])

    def test_multiplicação_por_escalar_1(self):
        """Testa se a resposta é correta para o vetor [1] e escalar 2"""
        x = [1]
        self.assertEqual(multi(x, 2), [2])

    def test_multiplicação_por_escalar_2(self):
        """Testa se a resposta é correta para o vetor [1, 2] e escalar 2"""
        x = [1, 2]
        self.assertEqual(multi(x, 2), [2, 4])

    def test_multiplicação_por_escalar_3(self):
        """Testa se a resposta é correta para o vetor [1, 2, 3] e escalar 2"""
        x = [1, 2, 3]
        self.assertEqual(multi(x, 2), [2, 4, 6])

    def test_multiplicação_por_escalar_4(self):
        """Testa se a resposta é correta para o vetor [1, 2, 3, 4] e escalar 3"""
        x = [1, 2, 3, 4]
        self.assertEqual(multi(x, 3), [3, 6, 9, 12])

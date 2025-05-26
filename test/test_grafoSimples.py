import pytest
from Metodos.matrizAdjSimples import matrizAdjSimples
from Objetos.Vertice import Vertice
import pandas as pd

@pytest.mark.parametrize("dataframeFiltrado, expected", [
    (
        [
            Vertice("MAT101", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-"),
            Vertice("FIS101", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-"),
            Vertice("QUI101", "Química I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-")
        ],
        [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
    ),
    (
        [
            Vertice("MAT101", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-"),
            Vertice("FIS101", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-"),
            Vertice("BIO101", "Biologia I", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-")
        ],
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ]
    ),
    (
        [
            Vertice("MAT101", "Matemática I", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-"),
            Vertice("FIS101", "Física I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-")
        ],
        [
            [0, 0],
            [0, 0]
        ]
    ),
])
def test_matriz_adj_simples(dataframeFiltrado, expected):
    matriz = matrizAdjSimples(dataframeFiltrado)
    assert matriz == expected, f"Esperado {expected}, mas obteve {matriz} para {dataframeFiltrado}"

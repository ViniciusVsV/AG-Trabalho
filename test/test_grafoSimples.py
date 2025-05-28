import pytest
from Metodos.MontaMatrizAdjSimples import MontaMatrizAdjSimples
from Objetos.Vertice import Vertice
import pandas as pd

@pytest.mark.parametrize("disciplinasFiltradas, expected", [
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-"),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-"),
            Vertice("QUI101", "CCO", "Química I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-")
        ],
        [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
    ),
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-"),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-"),
            Vertice("BIO101", "CCO", "Biologia I", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-")
        ],
        [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ]
    ),
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-"),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-")
        ],
        [
            [0, 0],
            [0, 0]
        ]
    ),
])
def test_matriz_adj_simples(disciplinasFiltradas, expected):
    matriz = MontaMatrizAdjSimples(disciplinasFiltradas)
    assert matriz == expected, f"Esperado {expected}, mas obteve {matriz} para {disciplinasFiltradas}"

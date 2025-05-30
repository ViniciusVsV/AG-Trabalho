import pytest
from Metodos.MontaListaAdjSimples import MontaListaAdjSimples
from Objetos.Vertice import Vertice

@pytest.mark.parametrize("disciplinasFiltradas, expected", [
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", 0),
            Vertice("QUI101", "CCO", "Química I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", 0)
        ],
        [
            [1],
            [0],
            []
        ]
    ),
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", 0),
            Vertice("BIO101", "CCO", "Biologia I", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-", 0)
        ],
        [
            [1, 2],
            [0],
            [0]
        ]
    ),
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", 0)
        ],
        [
            [],
            []
        ]
    ),
])
def test_MontaListaAdjSimples(disciplinasFiltradas, expected):
    listaAdj = MontaListaAdjSimples(disciplinasFiltradas)
    assert listaAdj == expected, f"Esperado {expected}, mas obteve {listaAdj} para {disciplinasFiltradas}"

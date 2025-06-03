import pytest
from Metodos.MontaListaAdjSimples import MontaListaAdjSimples
from Objetos.Vertice import Vertice

@pytest.mark.parametrize("disciplinasFiltradas, expected", [
    (
        [
            Vertice("MAT101", "Matemática I", "CCO", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", "-", 0),
            Vertice("FIS101", "Física I", "CCO", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", "-", 0),
            Vertice("QUI101", "Química I", "CCO", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", "-", 0)
        ],
        [
            [1],
            [0],
            []
        ]
    ),
    (
        [
            Vertice("MAT101", "Matemática I", "CCO", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", "-", 0),
            Vertice("FIS101", "Física I", "CCO", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", "-", 0),
            Vertice("BIO101", "Biologia I", "CCO", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-", "-", 0)
        ],
        [
            [1, 2],
            [0],
            [0]
        ]
    ),
    (
        [
            Vertice("MAT101", "Matemática I", "CCO", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-", "-", 0),
            Vertice("FIS101", "Física I", "CCO", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", "-", 0)
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

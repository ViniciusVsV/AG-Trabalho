import pytest
from Metodos.MontaListaAdjDirigida import MontaListaAdjDirigida
from Objetos.Vertice import Vertice

@pytest.mark.parametrize("disciplinas, expected", [
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 2, "NÃO", "2M23 3T2", 60, "MAT101", 0),
            Vertice("MAT102", "CCO", "Química I", "Obrigatória", 2, "NÃO", "4M1 5T2", 60, "MAT101", 0),
            Vertice("FIS102", "CCO", "Química I", "Obrigatória", 3, "NÃO", "4M1 5T2", 60, "FIS101 E MAT102", 0)
        ],
        [
            [],
            [0],
            [0],
            [1, 2]
        ]
    ),
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 2, "NÃO", "2M23 3T2", 60, "MAT101", 0),
            Vertice("MAT102", "CCO", "Matemática II", "Obrigatória", 2, "NÃO", "2M1 3T3", 60, "MAT101", 0)
        ],
        [
            [],
            [0],
            [0]
        ]
    ),
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-", 0),
            Vertice("MAT102", "CCO", "Matemática II", "Obrigatória", 2, "NÃO", "4M1 5T2", 60, "MAT101", 0)
        ],
        [
            [],
            [0]
        ]
    ),
])
def test_MontaListaAdjDirigida(disciplinas, expected):
    listaAdj = MontaListaAdjDirigida(disciplinas)
    assert listaAdj == expected, f"Esperado {expected}, mas obteve {listaAdj} para {disciplinas}"

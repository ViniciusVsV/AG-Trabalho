import pytest
from Metodos.CalculaPesos import CalculaPesos
from Objetos.Vertice import Vertice

@pytest.mark.parametrize("listaAdj, disciplinas, expected", [
    (
        [
            [],
            [0],
            [0],
            [1, 2]
        ],
        [
            Vertice("PROJ101", "CCO", "Projeto Integrado", "Obrigatória", 1, "SIM", "2M12 3T3", 60, "-", 8),
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 8),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 2, "NÃO", "2M23 3T2", 60, "MAT101", 7),
            Vertice("MAT102", "CCO", "Química I", "Obrigatória", 2, "NÃO", "4M1 5T2", 60, "MAT101", 7),
            Vertice("FIS102", "CCO", "Química I", "Obrigatória", 3, "NÃO", "4M1 5T2", 60, "FIS101 E MAT102", 6)
        ],
        [

        ]
    )
])
def test_CalculaPesos(listaAdj, disciplinas, expected):
    verticesComPesos = CalculaPesos(listaAdj, disciplinas)
    assert verticesComPesos == expected, f"Esperado {expected}, mas obteve {verticesComPesos} para {verticesComPesos}"

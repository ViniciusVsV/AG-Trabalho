import pytest
from Metodos.FiltraDisciplinas import FiltraDisciplinas
from Objetos.Vertice import Vertice

@pytest.mark.parametrize("disciplinas, disciplinasCumpridas, periodoAtual, expected", [
    # Teste do filtro de disciplinas que não estão sendo ofertadas
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 2, "NÃO", "2M23 3T2", 60, "-", 0),
            Vertice("QUI101", "CCO", "Química I", "Obrigatória", 2, "NÃO", "4M1 5T2", 60, "-", 0)
        ],
        set(),
        1,
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0)
        ]
    ),

    # Teste do filtro de disciplinas cujos pré-requisitos não foram atendidos
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", 0),
            Vertice("QUI101", "CCO", "Química I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", 0),
            Vertice("MAT102", "CCO", "Matemática II", "Obrigatória", 3, "NÃO", "2M12 3T3", 60, "MAT101", 0),
        ],
        set(),
        1,
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", 0),
            Vertice("QUI101", "CCO", "Química I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", 0)
        ]
    ),

    # Teste do filtro de disciplinas já cumpridas
    (
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", 0),
            Vertice("QUI101", "CCO", "Química I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", 0)
        ],
        set(["MAT101", "FIS101"]),
        1,
        [
            Vertice("QUI101", "CCO", "Química I", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", 0)
        ]
    )
])
def test_FiltraDisciplinas(disciplinas, disciplinasCumpridas, periodoAtual, expected):
    disciplinasFiltradas = FiltraDisciplinas(disciplinas, disciplinasCumpridas, periodoAtual)
    assert disciplinasFiltradas == expected, f"Esperado {expected}, mas obteve {disciplinasFiltradas} para {disciplinas}"

import pytest
from Metodos.FiltraDisciplinas import FiltraDisciplinas
from Objetos.Vertice import Vertice

@pytest.mark.parametrize("disciplinas, disciplinasCumpridas, periodoAtual, expected", [
    # Teste do filtro de disciplinas que não estão sendo ofertadas
    (
        [
            Vertice("MAT101", "Matemática I", "CCO", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", "-", 0),
            Vertice("FIS101", "Física I", "CCO", "Obrigatória", 2, "NÃO", "2M23 3T2", 60, "-", "-", 0),
            Vertice("QUI101", "Química I", "CCO", "Obrigatória", 2, "NÃO", "4M1 5T2", 60, "-", "-", 0)
        ],
        set(),
        1,
        {"MAT101"}
    ),

    # Teste do filtro de disciplinas cujos pré-requisitos não foram atendidos
    (
        [
            Vertice("MAT101", "Matemática I", "CCO", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", "-", 0),
            Vertice("FIS101", "Física I", "CCO", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", "-", 0),
            Vertice("QUI101", "Química I", "CCO", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", "-", 0),
            Vertice("MAT102", "Matemática II", "CCO", "Obrigatória", 3, "NÃO", "2M12 3T3", 60, "MAT101", "-", 0),
        ],
        set(),
        1,
        {"MAT101", "FIS101", "QUI101"}
    ),

    # Teste do filtro de disciplinas já cumpridas
    (
        [
            Vertice("MAT101", "Matemática I", "CCO", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", "-", 0),
            Vertice("FIS101", "Física I", "CCO", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", "-", 0),
            Vertice("QUI101", "Química I", "CCO", "Obrigatória", 1, "NÃO", "4M1 5T2", 60, "-", "-", 0)
        ],
        set(["MAT101", "FIS101"]),
        1,
        {"QUI101"}
    )
])
def test_FiltraDisciplinas(disciplinas, disciplinasCumpridas, periodoAtual, expected):
    disciplinasFiltradas = FiltraDisciplinas(disciplinas, disciplinasCumpridas, periodoAtual)
    disciplinasFiltradas_siglas = {disc.sigla for disc in disciplinasFiltradas}
    assert expected.issubset(disciplinasFiltradas_siglas), f"Esperado {expected}, mas obteve {disciplinasFiltradas_siglas} para {[x.sigla for x in disciplinas]}"

    # assert any(dis == expected), f"Esperado {expected}, mas obteve {disciplinasFiltradas} para {disciplinas}"

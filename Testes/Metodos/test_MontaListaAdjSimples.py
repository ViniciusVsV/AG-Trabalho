import pytest
from Metodos.MontaListaAdjSimples import MontaListaAdjSimples
from Objetos import Turma

@pytest.mark.parametrize("disciplinasFiltradas, expected", [
    (
        [
            Turma(
                nro_turma=1,
                horarios="2M12 3T3",
                peso=0.0
            ),
            Turma(
                nro_turma=1,
                horarios="2M23 3T2",
                peso=0.0
            ),
            Turma(
                nro_turma=1,
                horarios="4M1 5T2",
                peso=0.0
            )
        ],
        [
            [1],
            [0],
            []
        ]
    ),
    (
        [
            Turma(
                nro_turma=1,
                horarios="2M12 3T3",
                peso=0.0
            ),
            Turma(
                nro_turma=1,
                horarios="2M23 3T2",
                peso=0.0
            ),
            Turma(
                nro_turma=1,
                horarios="2M1 3T3",
                peso=0.0
            )
        ],
        [
            [1, 2],
            [0],
            [0]
        ]
    ),
    (
        [
            Turma(
                nro_turma=1,
                horarios="2M1 3T3",
                peso=0.0
            ),
            Turma(
                nro_turma=1,
                horarios="4M1 5T2",
                peso=0.0
            )
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

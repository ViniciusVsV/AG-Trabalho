import pytest
from Metodos.CalculaPesos import CalculaPesos
from Objetos import Disciplina

@pytest.mark.parametrize("listaAdj, disciplinas, expected", [
    (
        [
            [],
            [0],
            [0],
            [1, 2]
        ],
        [
            Disciplina(sigla="PROJ101", nome="Projeto Integrado", curso="CCO", categoria="Obrigatória", periodo=1, anualidade="SIM", cargaHoraria=60, preRequisitos="-", peso=8),
            Disciplina(sigla="MAT101", nome="Matemática I", curso="CCO", categoria="Obrigatória", periodo=1, anualidade="NÃO", cargaHoraria=60, preRequisitos="-", peso=8),
            Disciplina(sigla="FIS101", nome="Física I", curso="CCO", categoria="Obrigatória", periodo=2, anualidade="NÃO", cargaHoraria=60, preRequisitos="MAT101", peso=7),
            Disciplina(sigla="MAT102", nome="Química I", curso="CCO", categoria="Obrigatória", periodo=2, anualidade="NÃO", cargaHoraria=60, preRequisitos="MAT101", peso=7),
            Disciplina(sigla="FIS102", nome="Química I", curso="CCO", categoria="Obrigatória", periodo=3, anualidade="NÃO", cargaHoraria=60, preRequisitos="FIS101 E MAT102", peso=6)
        ],
        [

        ]
    )
])
@pytest.mark.skip(reason="Ainda não finalizado")
def test_CalculaPesos(listaAdj, disciplinas, expected):
    verticesComPesos = CalculaPesos(listaAdj, disciplinas)
    assert verticesComPesos == expected, f"Esperado {expected}, mas obteve {verticesComPesos} para {verticesComPesos}"

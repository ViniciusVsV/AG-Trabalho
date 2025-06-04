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
            Disciplina(sigla="PROJ101", nome="Projeto Integrado", curso="CCO", categoria="Obrigatória", semestre=1, anualidade="SIM", carga_horaria=60, pre_requisitos="-", peso=8),
            Disciplina(sigla="MAT101", nome="Matemática I", curso="CCO", categoria="Obrigatória", semestre=1, anualidade="NÃO", carga_horaria=60, pre_requisitos="-", peso=8),
            Disciplina(sigla="FIS101", nome="Física I", curso="CCO", categoria="Obrigatória", semestre=2, anualidade="NÃO", carga_horaria=60, pre_requisitos="MAT101", peso=7),
            Disciplina(sigla="MAT102", nome="Química I", curso="CCO", categoria="Obrigatória", semestre=2, anualidade="NÃO", carga_horaria=60, pre_requisitos="MAT101", peso=7),
            Disciplina(sigla="FIS102", nome="Química I", curso="CCO", categoria="Obrigatória", semestre=3, anualidade="NÃO", carga_horaria=60, pre_requisitos="FIS101 E MAT102", peso=6)
        ],
        [

        ]
    )
])
@pytest.mark.skip(reason="Ainda não finalizado")
def test_CalculaPesos(listaAdj, disciplinas, expected):
    verticesComPesos = CalculaPesos(listaAdj, disciplinas)
    assert verticesComPesos == expected, f"Esperado {expected}, mas obteve {verticesComPesos} para {verticesComPesos}"

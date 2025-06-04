import pytest
from Metodos.MontaListaAdjDirigida import MontaListaAdjDirigida
from Objetos import Disciplina

@pytest.mark.parametrize("disciplinas, expected", [
    (
        [
            Disciplina(
                codigo="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="-",
                equivalentes="-",
                correquisito="-",
                peso=0.0
            ),
            Disciplina(
                codigo="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=2,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="MAT101",
                equivalentes="-",
                correquisito="-",
                peso=0.0
            ),
            Disciplina(
                codigo="MAT102",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=2,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="MAT101",
                equivalentes="-",
                correquisito="-",
                peso=0.0
            ),
            Disciplina(
                codigo="FIS102",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=3,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="FIS101 E MAT102",
                equivalentes="-",
                correquisito="-",
                peso=0.0
            ),
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
            Disciplina(
                codigo="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="-",
                equivalentes="-",
                correquisito="-",
                peso=0.0
            ),
            Disciplina(
                codigo="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=2,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="MAT101",
                equivalentes="-",
                correquisito="-",
                peso=0.0
            ),
            Disciplina(
                codigo="MAT102",
                nome="Matemática II",
                curso="CCO",
                categoria="Obrigatória",
                semestre=2,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="MAT101",
                equivalentes="-",
                correquisito="-",
                peso=0.0
            ),
        ],
        [
            [],
            [0],
            [0]
        ]
    ),
    (
        [
            Disciplina(
                codigo="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="-",
                equivalentes="-",
                correquisito="-",
                peso=0.0
            ),
            Disciplina(
                codigo="MAT102",
                nome="Matemática II",
                curso="CCO",
                categoria="Obrigatória",
                semestre=2,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="MAT101",
                equivalentes="-",
                correquisito="-",
                peso=0.0
            ),
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

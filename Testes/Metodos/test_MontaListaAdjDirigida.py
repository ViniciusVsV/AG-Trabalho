import pytest
from Metodos.MontaListaAdjDirigida import montaListaAdjDirigida
from Objetos import Disciplina

@pytest.mark.parametrize("disciplinas, expected", [
    (
        [
            Disciplina(
                sigla="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="-",
                equivalentes="-",
                correquisitos="-",
                peso=0.0
            ),
            Disciplina(
                sigla="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=2,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="MAT101",
                equivalentes="-",
                correquisitos="-",
                peso=0.0
            ),
            Disciplina(
                sigla="MAT102",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=2,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="MAT101",
                equivalentes="-",
                correquisitos="-",
                peso=0.0
            ),
            Disciplina(
                sigla="FIS102",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=3,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="FIS101 E MAT102",
                equivalentes="-",
                correquisitos="-",
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
                sigla="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="-",
                equivalentes="-",
                correquisitos="-",
                peso=0.0
            ),
            Disciplina(
                sigla="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=2,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="MAT101",
                equivalentes="-",
                correquisitos="-",
                peso=0.0
            ),
            Disciplina(
                sigla="MAT102",
                nome="Matemática II",
                curso="CCO",
                categoria="Obrigatória",
                periodo=2,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="MAT101",
                equivalentes="-",
                correquisitos="-",
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
                sigla="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="-",
                equivalentes="-",
                correquisitos="-",
                peso=0.0
            ),
            Disciplina(
                sigla="MAT102",
                nome="Matemática II",
                curso="CCO",
                categoria="Obrigatória",
                periodo=2,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="MAT101",
                equivalentes="-",
                correquisitos="-",
                peso=0.0
            ),
        ],
        [
            [],
            [0]
        ]
    ),
])
def test_montaListaAdjDirigida(disciplinas, expected):
    listaAdj = montaListaAdjDirigida(disciplinas)
    assert listaAdj == expected, f"Esperado {expected}, mas obteve {listaAdj} para {disciplinas}"

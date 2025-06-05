import pytest
from Metodos.FiltraTurmas import FiltraTurmas
from Objetos import Disciplina

@pytest.mark.parametrize("disciplinas, disciplinasCumpridas, semestreAtual, expected", [
    # Teste do filtro de disciplinas que não estão sendo ofertadas
    (
        [
            Disciplina(
                sigla="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60
            ),
            Disciplina(
                sigla="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=2,
                anualidade="NÃO",
                cargaHoraria=60
            ),
            Disciplina(
                sigla="QUI101",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=2,
                anualidade="NÃO",
                cargaHoraria=60
            )
        ],
        set(),
        1,
        {"MAT101"}
    ),

    # Teste do filtro de disciplinas cujos pré-requisitos não foram atendidos
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
                preRequisitos="-"
            ),
            Disciplina(
                sigla="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="-"
            ),
            Disciplina(
                sigla="QUI101",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="-"
            ),
            Disciplina(
                sigla="MAT102",
                nome="Matemática II",
                curso="CCO",
                categoria="Obrigatória",
                periodo=3,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="MAT101"
            )
        ],
        set(),
        1,
        {"MAT101", "FIS101", "QUI101"}
    ),

    # Teste do filtro de disciplinas já cumpridas
    (
        [
            Disciplina(
                sigla="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60
            ),
            Disciplina(
                sigla="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60
            ),
            Disciplina(
                sigla="QUI101",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60
            )
        ],
        {"MAT101", "FIS101"},
        1,
        {"QUI101"}
    )
])
def test_FiltraTurmas(disciplinas, disciplinasCumpridas, semestreAtual, expected):
    disciplinasFiltradas = FiltraTurmas(disciplinas, disciplinasCumpridas, semestreAtual)
    disciplinasFiltradas_siglas = {disc.sigla for disc in disciplinasFiltradas}
    assert expected.issubset(disciplinasFiltradas_siglas), f"Esperado {expected}, mas obteve {disciplinasFiltradas_siglas} para {[x.sigla for x in disciplinas]}"

    # assert any(dis == expected), f"Esperado {expected}, mas obteve {disciplinasFiltradas} para {disciplinas}"

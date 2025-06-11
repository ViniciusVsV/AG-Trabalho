import pytest
from Metodos.FiltraTurmas import filtraTurmas
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
                cargaHoraria=60,
                turmas=[(1, "2M3", 1)]
            ),
            Disciplina(
                sigla="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=2,
                anualidade="NÃO",
                cargaHoraria=60,
                turmas=[(1, "2M2", 2)]
            ),
            Disciplina(
                sigla="QUI101",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=2,
                anualidade="NÃO",
                cargaHoraria=60,
                turmas=[(1, "2M1", 2)]
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
                preRequisitos="-",
                turmas=[(1, "2M4", 1)]
            ),
            Disciplina(
                sigla="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="-",
                turmas=[(1, "2M3", 1)]
            ),
            Disciplina(
                sigla="QUI101",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="-",
                turmas=[(1, "2M2", 1)]
            ),
            Disciplina(
                sigla="MAT102",
                nome="Matemática II",
                curso="CCO",
                categoria="Obrigatória",
                periodo=3,
                anualidade="NÃO",
                cargaHoraria=60,
                preRequisitos="MAT101",
                turmas=[(1, "2M1", 3)]
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
                cargaHoraria=60,
                turmas=[(1, "2M1", 1)]
            ),
            Disciplina(
                sigla="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60,
                turmas=[(1, "2M2", 1)]
            ),
            Disciplina(
                sigla="QUI101",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                periodo=1,
                anualidade="NÃO",
                cargaHoraria=60,
                turmas=[(1, "2M3", 1)]
            )
        ],
        {"MAT101", "FIS101"},
        1,
        {"QUI101"}
    )
])
def test_filtraTurmas(disciplinas, disciplinasCumpridas, semestreAtual, expected):
    turmasFiltradas = filtraTurmas(disciplinas, disciplinasCumpridas, semestreAtual)
    turmasFiltadas_siglas = {turma.sigla for turma in turmasFiltradas}
    assert expected.issubset(turmasFiltadas_siglas), f"Esperado {expected}, mas obteve {turmasFiltadas_siglas} ({len(turmasFiltradas)}) para {[x.sigla for x in disciplinas]}"

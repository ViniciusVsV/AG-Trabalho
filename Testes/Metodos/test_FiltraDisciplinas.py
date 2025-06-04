import pytest
from Metodos.FiltraDisciplinas import FiltraDisciplinas
from Objetos import Disciplina

@pytest.mark.parametrize("disciplinas, disciplinasCumpridas, periodoAtual, expected", [
    # Teste do filtro de disciplinas que não estão sendo ofertadas
    (
        [
            Disciplina(
                codigo="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60
            ),
            Disciplina(
                codigo="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=2,
                anualidade="NÃO",
                carga_horaria=60
            ),
            Disciplina(
                codigo="QUI101",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=2,
                anualidade="NÃO",
                carga_horaria=60
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
                codigo="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="-"
            ),
            Disciplina(
                codigo="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="-"
            ),
            Disciplina(
                codigo="QUI101",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="-"
            ),
            Disciplina(
                codigo="MAT102",
                nome="Matemática II",
                curso="CCO",
                categoria="Obrigatória",
                semestre=3,
                anualidade="NÃO",
                carga_horaria=60,
                pre_requisitos="MAT101"
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
                codigo="MAT101",
                nome="Matemática I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60
            ),
            Disciplina(
                codigo="FIS101",
                nome="Física I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60
            ),
            Disciplina(
                codigo="QUI101",
                nome="Química I",
                curso="CCO",
                categoria="Obrigatória",
                semestre=1,
                anualidade="NÃO",
                carga_horaria=60
            )
        ],
        {"MAT101", "FIS101"},
        1,
        {"QUI101"}
    )
])
def test_FiltraDisciplinas(disciplinas, disciplinasCumpridas, periodoAtual, expected):
    disciplinasFiltradas = FiltraDisciplinas(disciplinas, disciplinasCumpridas, periodoAtual)
    disciplinasFiltradas_codigos = {disc.codigo for disc in disciplinasFiltradas}
    assert expected.issubset(disciplinasFiltradas_codigos), f"Esperado {expected}, mas obteve {disciplinasFiltradas_codigos} para {[x.codigo for x in disciplinas]}"

    # assert any(dis == expected), f"Esperado {expected}, mas obteve {disciplinasFiltradas} para {disciplinas}"

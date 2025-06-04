import pytest
from Metodos.MontaListaAdjSimples import MontaListaAdjSimples
from Objetos import Disciplina, Turma

@pytest.mark.parametrize("disciplinasFiltradas, expected", [
    (
        [
            Turma(
                disciplina=Disciplina(
                    codigo="MAT101", nome="Matemática I", curso="CCO",
                    categoria="Obrigatória", semestre=1, anualidade="NÃO",
                    carga_horaria=60
                ),
                nro_turma=1,
                horarios="2M12 3T3",
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    codigo="FIS101", nome="Física I", curso="CCO",
                    categoria="Obrigatória", semestre=1, anualidade="NÃO",
                    carga_horaria=60
                ),
                nro_turma=1,
                horarios="2M23 3T2",
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    codigo="QUI101", nome="Química I", curso="CCO",
                    categoria="Obrigatória", semestre=1, anualidade="NÃO",
                    carga_horaria=60
                ),
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
                disciplina=Disciplina(
                    codigo="MAT101", nome="Matemática I", curso="CCO",
                    categoria="Obrigatória", semestre=1, anualidade="NÃO",
                    carga_horaria=60
                ),
                nro_turma=1,
                horarios="2M12 3T3",
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    codigo="FIS101", nome="Física I", curso="CCO",
                    categoria="Obrigatória", semestre=1, anualidade="NÃO",
                    carga_horaria=60
                ),
                nro_turma=1,
                horarios="2M23 3T2",
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    codigo="BIO101", nome="Biologia I", curso="CCO",
                    categoria="Obrigatória", semestre=1, anualidade="NÃO",
                    carga_horaria=60
                ),
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
                disciplina=Disciplina(
                    codigo="MAT101", nome="Matemática I", curso="CCO",
                    categoria="Obrigatória", semestre=1, anualidade="NÃO",
                    carga_horaria=60
                ),
                nro_turma=1,
                horarios="2M1 3T3",
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    codigo="FIS101", nome="Física I", curso="CCO",
                    categoria="Obrigatória", semestre=1, anualidade="NÃO",
                    carga_horaria=60
                ),
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

import pytest
from Metodos.MontaListaAdjSimples import montaListaAdjSimples
from Objetos import Disciplina, Turma

@pytest.mark.parametrize("disciplinasFiltradas, expected", [
    (
        [
            Turma(
                disciplina=Disciplina(
                    sigla="MAT101", nome="Matemática I", curso="CCO",
                    categoria="Obrigatória", periodo=1, anualidade="NÃO",
                    cargaHoraria=60
                ),
                numeroTurma=1,
                horario="2M12 3T3",
                semestre=1,
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    sigla="FIS101", nome="Física I", curso="CCO",
                    categoria="Obrigatória", periodo=1, anualidade="NÃO",
                    cargaHoraria=60
                ),
                numeroTurma=1,
                horario="2M23 3T2",
                semestre=1,
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    sigla="QUI101", nome="Química I", curso="CCO",
                    categoria="Obrigatória", periodo=1, anualidade="NÃO",
                    cargaHoraria=60
                ),
                numeroTurma=1,
                horario="4M1 5T2",
                semestre=1,
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
                    sigla="MAT101", nome="Matemática I", curso="CCO",
                    categoria="Obrigatória", periodo=1, anualidade="NÃO",
                    cargaHoraria=60
                ),
                numeroTurma=1,
                horario="2M12 3T3",
                semestre=1,
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    sigla="FIS101", nome="Física I", curso="CCO",
                    categoria="Obrigatória", periodo=1, anualidade="NÃO",
                    cargaHoraria=60
                ),
                numeroTurma=1,
                horario="2M23 3T2",
                semestre=1,
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    sigla="BIO101", nome="Biologia I", curso="CCO",
                    categoria="Obrigatória", periodo=1, anualidade="NÃO",
                    cargaHoraria=60
                ),
                numeroTurma=1,
                horario="2M1 3T3",
                semestre=1,
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
                    sigla="MAT101", nome="Matemática I", curso="CCO",
                    categoria="Obrigatória", periodo=1, anualidade="NÃO",
                    cargaHoraria=60
                ),
                numeroTurma=1,
                horario="2M1 3T3",
                semestre=1,
                peso=0.0
            ),
            Turma(
                disciplina=Disciplina(
                    sigla="FIS101", nome="Física I", curso="CCO",
                    categoria="Obrigatória", periodo=1, anualidade="NÃO",
                    cargaHoraria=60
                ),
                numeroTurma=1,
                horario="4M1 5T2",
                semestre=1,
                peso=0.0
            )
        ],
        [
            [],
            []
        ]
    ),
])
def test_montaListaAdjSimples(disciplinasFiltradas, expected):
    listaAdj = montaListaAdjSimples(disciplinasFiltradas)
    assert listaAdj == expected, f"Esperado {expected}, mas obteve {listaAdj} para {disciplinasFiltradas}"
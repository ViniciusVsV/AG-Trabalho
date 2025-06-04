from Metodos import LeHistorico, MontaListaAdjDirigida, CalculaPesos, FiltraDisciplinas, MontaListaAdjSimples, CalculaCIM, GeraGrafoDisciplina
from Objetos import Turma, Disciplina

import pandas as pd
import uuid

if __name__ == "__main__":
    while True:
        realizarTeste = input("Deseja realizar um teste (S/N)? ")

        if realizarTeste != "S" and realizarTeste != "s" and realizarTeste != "N" and realizarTeste != "n":
            print("Digita certo seu jumento")
            continue

        elif realizarTeste == "N" or realizarTeste == "n":
            break

        else:
            id = str(uuid.uuid4())

            # Obtem input do usuário (curso, disciplinas já feitas, preferencias de optativas, nPeriodos do curso, semestre para previsão)
            # Atualmente usando input. Temporário
            curso = str(input("Digite o seu curso (CCO/SIN): "))
            if curso != "CCO" and curso != "SIN":
                print("Mas ce é burro hein")
                continue

            disciplinasCumpridas = set()
            preferenciasOptativas = []
            
            nPeriodos = 8

            semestrePrevisao = int(input("Digite o semestre do ano para previsão (1/2): "))
            if semestrePrevisao != 1 and semestrePrevisao != 2:
                print("Digita certo carai")
                continue

            # Lê o dataset pertinente
            dataframe = pd.read_csv(
                "Datasets/Disciplinas" + curso + ".csv" ,
                na_values=[],
                keep_default_na=False
            )

            # Cria o array das disciplinas do curso
            disciplinas = []
            disciplinas_processadas: dict[str, Disciplina] = dict()

            turma_count = 0

            for index, row in dataframe.iterrows():
                if row['SIGLA'] in disciplinas_processadas:
                    # Se a disciplina já foi processada, apenas adiciona o horário
                    disciplinas_processadas[row['SIGLA']].adicionar_turma(row['HOR']
                                                                          , turma_count # row['TURMA']
                                                                          )
                    turma_count += 1
                    continue

                disciplina = Disciplina(
                    codigo          =   row['SIGLA'],
                    nome            =   row['NOME'],
                    curso           =   row['CURSO'],
                    categoria       =   row['CAT'],
                    semestre        =   row['PER'],
                    anualidade      =   row['AN'],
                    carga_horaria   =   row['CH'],
                    pre_requisitos  =   row['REQ'],
                    # equivalentes=   row['EQ'],
                    # correquisito=   row['COR'],

                    peso        =   nPeriodos - row['PER'] + 1
                )

                disciplina.adicionar_turma(row['HOR'], turma_count # row['TURMA']
                                           )
                turma_count += 1

                disciplinas_processadas[row['SIGLA']] = disciplina
                disciplinas.append(disciplina)

            # Constrói o grafo de pré-requisitos
            listaAdjDirigida = MontaListaAdjDirigida(disciplinas)

            GeraGrafoDisciplina(listaAdjDirigida, disciplinas, True, id, curso)

            # Calcula os pesos das disciplinas
            disciplinas = CalculaPesos(listaAdjDirigida, disciplinas)

            # Filtra as disciplinas
            disciplinasFiltradas = FiltraDisciplinas(disciplinas, disciplinasCumpridas, semestrePrevisao)

            turmas = []

            # Cria as turmas a partir das disciplinas filtradas
            for disciplina in disciplinasFiltradas:
                turmas.extend(disciplina.criaTurmas())

            # Constrói o grafo de conflitos de horários
            listaAdjSimples = MontaListaAdjSimples(turmas)

            # GeraGrafoDisciplina(listaAdjSimples, disciplinasFiltradas, False, id, curso)

            # Calcula os conjuntos independentes


            # Retorna o resultado ao usuário
            # Atualmente só printa as disciplinas e seus pesos. Temporário
            pesosOrdenados = sorted(disciplinasFiltradas, key=lambda d: d.peso, reverse=True)

            for p in pesosOrdenados:
                print(p.codigo, "-", p.nome, "--", p.categoria, "---", p.curso, "----", p.peso, "--- Turmas:", len(p.turmas))
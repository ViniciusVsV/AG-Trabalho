from Metodos import LeHistorico, MontaListaAdjDirigida, CalculaPesos, FiltraTurmas, MontaListaAdjSimples, CalculaCIM, GeraGrafo
from Objetos import Disciplina
from Metodos.mwis.branchAndBound import BranchAndBound

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
            caminhoArquivo = "./Testes/Historicos/historico_CCO-1.pdf"
            
            #disciplinasCumpridas = set()
            #curso = 'CCO'
            
            (curso, disciplinasCumpridas) = LeHistorico(caminhoArquivo)
            print(f"Disciplinas cumpridas: {disciplinasCumpridas}")

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
            disciplinas: list[Disciplina] = []
            disciplinasProcessadas: dict[tuple[str, str], Disciplina] = dict()

            qtdTurmas = 0

            for index, row in dataframe.iterrows():
                if (row['SIGLA'], row['CAT']) in disciplinasProcessadas:
                    # Se a disciplina já foi processada, apenas adiciona o horário
                    disciplinasProcessadas[(row['SIGLA'], row['CAT'])].adicionar_turma(
                                                                            qtdTurmas # row['TURMA']
                                                                          , row['HOR']
                                                                          , row['PER']
                                                                          )
                    qtdTurmas += 1
                    continue

                disciplina = Disciplina(
                    sigla           =   row['SIGLA'],
                    nome            =   row['NOME'],
                    curso           =   row['CURSO'],
                    categoria       =   row['CAT'],
                    semestre        =   row['PER'],
                    anualidade      =   row['AN'],
                    carga_horaria   =   row['CH'],
                    pre_requisitos  =   row['REQ'],
                    equivalentes    =   row['EQV'],
                    correquisito    =   row['COREQ'],

                    peso            =   nPeriodos - row['PER'] + 1
                )

                disciplina.adicionar_turma(qtdTurmas, row['HOR'], row['PER'])
                qtdTurmas += 1

                disciplinasProcessadas[(row['SIGLA'], row['CAT'])] = disciplina

                disciplinas.append(disciplina)


            # for disciplina in disciplinas:
            #     for turma in disciplina.cria_turmas():
            #         print(disciplina.nome + "---" + str(turma.semestre))

            # Constrói o grafo de pré-requisitos
            listaAdjDirigida = MontaListaAdjDirigida(disciplinas)

            # GeraGrafo(listaAdjDirigida, disciplinas, id, curso, True)

            # Calcula os pesos das disciplinas
            disciplinas = CalculaPesos(listaAdjDirigida, disciplinas)

            # Filtra as disciplinas
            turmas = FiltraTurmas(disciplinas, disciplinasCumpridas, semestrePrevisao)

            for disciplina in [d for d in disciplinas if d.sigla in set(d.sigla for d in turmas)]:
                print(f"{disciplina.sigla} - {disciplina.nome} - {disciplina.categoria} ({disciplina.peso})")

            # Constrói o grafo de conflitos de horários
            listaAdjSimples = MontaListaAdjSimples(turmas)

            # GeraGrafo(listaAdjSimples, disciplinasFiltradas, id, curso, False)

            # Calcula os conjuntos independentes
            conjuntoIM = BranchAndBound(
                (turmas, listaAdjSimples)
            )

            print(f"Conjunto Independente Máximo (CIM):")
            for turma in conjuntoIM.cmi:
                print(f"{turma.disciplina.sigla} - {turma.disciplina.nome} - {turma.horarios} ({turma.peso})")
            print(f"Peso do Conjunto Independente Máximo (CIM): {conjuntoIM.max_weight}")

            # Retorna o resultado ao usuário
            # Atualmente só printa as disciplinas e seus pesos. Temporário
            # pesosOrdenados = sorted(turmas, key=lambda d: d.peso, reverse=True)

            # for p in pesosOrdenados:
            #     print(p.disciplina.sigla, "-", p.disciplina.nome, "--", p.disciplina.categoria, "---", p.disciplina.curso, "----", p.peso)
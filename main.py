from Metodos import leHistorico, montaListaAdjDirigida, calculaPesos, filtraTurmas, montaListaAdjSimples, calculaCIM, geraGrafoPreRequisitos, geraGrafoConflitosHorario
from Objetos import Disciplina
from Metodos.mwis.branchAndBound import BranchAndBound

import pandas as pd

if __name__ == "__main__":
    while True:
        realizarTeste = input("Deseja realizar um teste (S/N)? ")

        if realizarTeste != "S" and realizarTeste != "s" and realizarTeste != "N" and realizarTeste != "n":
            print("Digita certo seu jumento")
            continue

        elif realizarTeste == "N" or realizarTeste == "n":
            break

        else:
            # Obtem input do usuário (curso, disciplinas já feitas, preferencias de optativas, nPeriodos do curso, semestre para previsão)
            # Atualmente usando input. Temporário
            # caminhoArquivo = "./Testes/Historicos/Historico_CCO_LV.pdf"
            caminhoArquivo = "./Testes/Historicos/historico_CCO-1.pdf"
            
            #disciplinasCumpridas = set()
            #curso = 'CCO'
            
            (curso, disciplinasCumpridas) = leHistorico(caminhoArquivo)
            print(f"Disciplinas cumpridas: {disciplinasCumpridas}")

            preferenciasOptativas = []
            
            nPeriodos = 8

            semestrePrevisao = int(input("Digite o semestre do ano para previsão (1/2): "))
            if semestrePrevisao != 1 and semestrePrevisao != 2:
                print("Digita certo carai")
                continue

            semestrePrevisao %= 2

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
                    disciplinasProcessadas[(row['SIGLA'], row['CAT'])].\
                        adicionaTurma(qtdTurmas, row['HOR'], row['SEM'])
                    
                    qtdTurmas += 1
                    continue

                disciplina = Disciplina(
                    sigla           =   row['SIGLA'],
                    nome            =   row['NOME'],
                    curso           =   row['CURSO'],
                    categoria       =   row['CAT'],
                    periodo         =   row['PER'],
                    anualidade      =   row['AN'],
                    cargaHoraria    =   row['CH'],
                    preRequisitos   =   row['REQ'],
                    equivalentes    =   row['EQV'],
                    correquisitos   =   row['COREQ'],

                    peso            =   nPeriodos - row['PER'] + 1
                )

                disciplina.adicionaTurma(qtdTurmas, row['HOR'], row['SEM'])
                qtdTurmas += 1

                disciplinasProcessadas[(row['SIGLA'], row['CAT'])] = disciplina

                disciplinas.append(disciplina)

            # Constrói o grafo de pré-requisitos
            listaAdjDirigida = montaListaAdjDirigida(disciplinas)

            geraGrafoPreRequisitos(listaAdjDirigida, disciplinas, curso)

            # Calcula os pesos das disciplinas
            disciplinas = calculaPesos(listaAdjDirigida, disciplinas)

            # Filtra as disciplinas e obtém as turmas disponíveis
            turmasFiltradas = filtraTurmas(disciplinas, disciplinasCumpridas, semestrePrevisao)

            #for disciplina in [d for d in disciplinas if d.sigla in set(d.sigla for d in turmasFiltradas)]:
            #    print(f"{disciplina.sigla} - {disciplina.nome} - {disciplina.categoria} ({disciplina.peso})")

            # Constrói o grafo de conflitos de horários, primeiro sem ser interconectado
            listaAdjSimples = montaListaAdjSimples(turmasFiltradas, False)
            geraGrafoConflitosHorario(listaAdjSimples, turmasFiltradas, curso, False)

            listaAdjSimples = montaListaAdjSimples(turmasFiltradas, True)

            geraGrafoConflitosHorario(listaAdjSimples, turmasFiltradas, curso, True)

            # Calcula os conjuntos independentes
            conjuntoIM = BranchAndBound(
                (turmasFiltradas, listaAdjSimples)
            )

            print(f"Conjunto Independente Máximo (CIM):")
            for turma in conjuntoIM.cmi:
                print(f"{turma.disciplina.sigla} - {turma.disciplina.nome} - {turma.horario} ({turma.peso})")
            print(f"Peso do Conjunto Independente Máximo (CIM): {conjuntoIM.max_weight}")

            print(f"\nOutros Conjuntos Máximos Independentes (CIMs):")
            conjuntosIM = conjuntoIM.calculate_others_cmis(4)
            for i, (turma, peso) in enumerate(conjuntosIM):
                print(f"{i+1} - Peso: {peso:.3f} | Carga horária: {sum(t.disciplina.cargaHoraria for t in turma)}")
                for t in turma:
                    print(f"{t.disciplina.sigla}\t- {t.disciplina.nome} - {t.horario} ({t.disciplina.peso:.3f})")
                print()

            
            jac_dist = []
            # Calcular a similaridade entre os conjuntos independentes
            for i in range(len(conjuntosIM)):
                for j in range(i+1, len(conjuntosIM)):
                        cj1 = set(t.sigla for t in conjuntosIM[i][0])
                        cj2 = set(t.sigla for t in conjuntosIM[j][0])

                        distancia_jaccard = len(cj1.intersection(cj2)) / len(cj1.union(cj2))
                        print(f"Distância de Jaccard entre CIM {i+1} e CIM {j+1}: {distancia_jaccard:.2f}")
                        jac_dist.append(distancia_jaccard)
            
            print(f"\nMaior distância de Jaccard entre CIMs: {max(jac_dist):.2f}")
            print(f"Menor distância de Jaccard entre CIMs: {min(jac_dist):.2f}")
            print(f"Média das distâncias de Jaccard entre CIMs: {sum(jac_dist) / len(jac_dist):.2f}")
            print(f"Desvio padrão das distâncias de Jaccard entre CIMs: {pd.Series(jac_dist).std():.2f}")

            # Retorna o resultado ao usuário
            # Atualmente só printa as disciplinas e seus pesos. Temporário
            #pesosOrdenados = sorted(turmasFiltradas, key=lambda d: d.peso, reverse=True)

            #for p in pesosOrdenados:
            #    print(p.sigla, "---", p.disciplina.nome, "---", p.disciplina.categoria, "---", p.horario, "---", p.semestre)
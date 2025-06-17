from Metodos import leHistorico, montaListaAdjDirigida, calculaPesos, filtraTurmas, montaListaAdjSimples, calculaCIM, geraGrafoPreRequisitos, geraGrafoConflitosHorario
from Objetos import Disciplina, Optativa
from Metodos.mwis.branchAndBound import BranchAndBound

import pandas as pd

if __name__ == "__main__":
    # Trocar para True caso deseje testar o funcionamento do sistema pela main
    mainTeste = False

    # Roda o servidor web
    if not mainTeste: 
        from Webserver.server import app
        app.run(debug=True)

        exit(0)        

    while mainTeste:
        classeOptativa = Optativa()

        print()
        print("------------------------------------------------------------------------------")
        print()

        realizarTeste = input("Deseja realizar um teste (S/N)? ")

        if realizarTeste != "S" and realizarTeste != "s" and realizarTeste != "N" and realizarTeste != "n":
            print("Entrada inválida")
            continue

        elif realizarTeste == "N" or realizarTeste == "n":
            break

        else:
            # Caminho do arquivo pdf
            
            caminhoArquivo = "./Testes/Historicos/Historico_CCO_1.pdf"
            
            # Obtém o curso e as disciplinas cumpridas pelo PDF e declara o número de períodos do curso
            
            (curso, disciplinasCumpridas) = leHistorico(caminhoArquivo)
            print(f"Disciplinas cumpridas: {disciplinasCumpridas}")

            disciplinasCumpridas = set(["XDES01", "CRSC03", "XMAC01", "CAHC04", "MAT00A"])

            nPeriodos = (
                8 if curso == "CCO"
                else 9 if curso == "SIN"
                else 10
            )

            # Escolhe a trilha de optativa preferida

            print()
            print("------------------------------------------------------------------------------")
            print()
            print("Trilhas Possíveis:")

            if curso == "CCO":
                print("Resolução de Problemas", "---", "1")
                print("Desenvolvimento de Sistemas", "---", "2")
                print("Ciência, Tecnologia e Inovação", "---", "3")
                print("Nenhumna", "---", "0")

            elif curso == "SIN":    
                print("Persistência e Análise de Dados", "---", "1")
                print("Redes e Sistemas Computacionais", "---", "2")
                print("Desenvolvimento e Engenharia de Software", "---", "3")
                print("Nenhumna", "---", "0")

            print()
            print("------------------------------------------------------------------------------")
            print()
            numeroTrilha = int(input("Digite o número da trilha preferida: "))
            
            optativasPreferidas = classeOptativa.getTrilha(numeroTrilha, curso)

            if optativasPreferidas == None:
                print("Trilha inválida")
                continue

            print(optativasPreferidas)

            print()
            print("------------------------------------------------------------------------------")
            print()
            
            # Obtém o semestre de previsão

            semestrePrevisao = int(input("Digite o semestre do ano para previsão (1/2): "))
            if semestrePrevisao != 1 and semestrePrevisao != 2:
                print("Semestre inválido")
                continue

            semestrePrevisao %= 2

            # Lê o dataset pertinente

            dataframe = pd.read_csv(
                "Datasets/Disciplinas" + curso + ".csv" ,
                na_values=[],
                keep_default_na=False
            )

            # Cria o array das disciplinas do curso e o popula a partir do dataset

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

                    peso            =   nPeriodos - row["PER"] + 1
                )

                disciplina.adicionaTurma(qtdTurmas, row['HOR'], row['SEM'])
                qtdTurmas += 1

                disciplinasProcessadas[(row['SIGLA'], row['CAT'])] = disciplina

                disciplinas.append(disciplina)

            # Constrói o grafo de pré-requisitos

            listaAdjDirigida = montaListaAdjDirigida(disciplinas)

            geraGrafoPreRequisitos(listaAdjDirigida, disciplinas, curso)

            # Calcula os pesos das disciplinas

            disciplinas = calculaPesos(listaAdjDirigida, disciplinas, numeroTrilha, curso)
            disciplinasSorted = sorted(disciplinas, key=lambda d: d.peso, reverse=True)

            for d in disciplinasSorted:
                print(d.sigla, "---", d.nome, "---", d.categoria, "---", d.peso)


            # Filtra as disciplinas e obtém as turmas disponíveis

            turmasFiltradas = filtraTurmas(disciplinas, disciplinasCumpridas, semestrePrevisao)

            #for t in turmasFiltradas:
            #    print(t.sigla, "---", t.disciplina.nome, "---", t.disciplina.categoria, "---", t.peso)

            # Constrói o grafo de conflitos de horários

            listaAdjSimples = montaListaAdjSimples(turmasFiltradas)

            geraGrafoConflitosHorario(listaAdjSimples, turmasFiltradas, curso)

            # Calcula os conjuntos independentes
            
            conjuntoIM = BranchAndBound(
                (turmasFiltradas, listaAdjSimples),
                416
            )

            print()
            print("------------------------------------------------------------------------------")
            print()


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
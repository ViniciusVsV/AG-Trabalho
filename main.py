from Metodos import LeHistorico, MontaListaAdjDirigida, CalculaPesos, FiltraTurmas, MontaListaAdjSimples, CalculaCIM, GeraGrafoPreRequisitos, GeraGrafoConflitosHorario
from Objetos import Disciplina

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
            caminhoArquivo = "./Testes/Historicos/historico_Vinicius.pdf"
            
            # disciplinasCumpridas = set(["XDES01", "MAT00A", "CRSC03", "CAHC04", "XMAC01", "CTCO01", "CRSC04", "CMAC04", "MAT00B"])
            # curso = 'CCO'
            
            (curso, disciplinasCumpridas) = LeHistorico(caminhoArquivo)

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
            disciplinas = []
            disciplinasProcessadas: dict[tuple[str, str], Disciplina] = dict()

            qtdTurmas = 0

            for index, row in dataframe.iterrows():
                if (row['SIGLA'], row['CAT']) in disciplinasProcessadas:
                    # Se a disciplina já foi processada, apenas adiciona o horário
                    disciplinasProcessadas[(row['SIGLA'], row['CAT'])].\
                        AdicionaTurma(qtdTurmas, row['HOR'], row['SEM'])
                    
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

                disciplina.AdicionaTurma(qtdTurmas, row['HOR'], row['SEM'])
                qtdTurmas += 1

                disciplinasProcessadas[(row['SIGLA'], row['CAT'])] = disciplina

                disciplinas.append(disciplina)

            # Constrói o grafo de pré-requisitos
            listaAdjDirigida = MontaListaAdjDirigida(disciplinas)

            GeraGrafoPreRequisitos(listaAdjDirigida, disciplinas, curso, id)

            # Calcula os pesos das disciplinas
            disciplinas = CalculaPesos(listaAdjDirigida, disciplinas)

            # Filtra as disciplinas e obtém as turmas disponíveis
            turmasFiltradas = FiltraTurmas(disciplinas, disciplinasCumpridas, semestrePrevisao)

            # Constrói o grafo de conflitos de horários, primeiro sem ser interconectado
            listaAdjSimples = MontaListaAdjSimples(turmasFiltradas, False)
            GeraGrafoConflitosHorario(listaAdjSimples, turmasFiltradas, curso, id, False)

            listaAdjSimples = MontaListaAdjSimples(turmasFiltradas, True)
            GeraGrafoConflitosHorario(listaAdjSimples, turmasFiltradas, curso, id, True)

            # Calcula os conjuntos independentes


            # Retorna o resultado ao usuário
            # Atualmente só printa as disciplinas e seus pesos. Temporário
            pesosOrdenados = sorted(turmasFiltradas, key=lambda d: d.peso, reverse=True)

            for p in pesosOrdenados:
                print(p.sigla, "---", p.disciplina.nome, "---", p.disciplina.categoria, "---", p.peso)
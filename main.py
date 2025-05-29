from Metodos import MontaListaAdjDirigida, MontaListaAdjSimples, GeraGrafo, FiltraDisciplinas, CalculaPesos
from Objetos import Vertice
import pandas as pd

# Isso é só pra teste, modifiquem como quiserem
if __name__ == "__main__":
    ds = pd.read_csv(
        'Datasets/DisciplinasCCO.csv',
        na_values=[],            
        keep_default_na=False
    )

    vertices = []
    qtdSemestres = 8

    for index, row in ds.iterrows():
        vertice = Vertice(
            sigla       =   row['SIGLA'],
            nome        =   row['NOME'],
            curso       =   row['CURSO'],
            categoria   =   row['CAT.'],
            semestre    =   row['PER.'],
            anualidade  =   row['AN.'],
            horarios    =   row['HOR.'],
            cargaHor    =   row['CH'],
            preReq      =   row['REQ.'],

            peso        =   qtdSemestres - row['PER.'] + 1
        )
        vertices.append(vertice)  

    listaAdj = MontaListaAdjDirigida(vertices)

    verticesComPesos = CalculaPesos(listaAdj, vertices)

    #for vertice in verticesComPesos:
    #    print(vertice.nome + " --- " + str(vertice.peso))

    #verticesOrdenados = sorted(verticesComPesos, key=lambda v: v.peso, reverse=True)
    #for vertice in verticesOrdenados:
    #    print(vertice.nome + " --- " + str(vertice.peso))

    GeraGrafo(listaAdj, verticesComPesos, True, 3)

    vazio = set()

    disciplinasFiltradas = FiltraDisciplinas(verticesComPesos, vazio, 1)

    ordenado = sorted(disciplinasFiltradas, key=lambda d: d.peso, reverse=True)

    for d in ordenado:
        print(d.sigla + " " + d.nome + " - " + d.categoria + " --- " + str(d.peso))

    listaAdj2 = MontaListaAdjSimples(disciplinasFiltradas)

    GeraGrafo(listaAdj2, disciplinasFiltradas, False, 3)
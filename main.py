from Metodos import MontaListaAdjDirigida, MontaListaAdjSimples, GeraGrafo, FiltraDisciplinas
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

    for index, row in ds.iterrows():
        vertice = Vertice(
            sigla=row['SIGLA'],
            nome=row['NOME'],
            curso=row['CURSO'],
            categoria=row['CAT.'],
            semestre=row['PER.'],
            anualidade=row['AN.'],
            horarios=row['HOR.'],
            cargaHor=row['CH'],
            preReq=row['REQ.']
        )
        vertices.append(vertice)

    listaAdj = MontaListaAdjDirigida(vertices)

    GeraGrafo(listaAdj, vertices, True, 1)

    vazio = set()

    disciplinasFiltradas = FiltraDisciplinas(vertices, vazio, 1)

    listaAdj2 = MontaListaAdjSimples(disciplinasFiltradas)

    GeraGrafo(listaAdj2, disciplinasFiltradas, False, 1)

    for i in range(len(disciplinasFiltradas)):
        print(disciplinasFiltradas[i].nome)
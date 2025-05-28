from Metodos import MontaMatrizAdjSimples, MontaMatrizAdjDirigida, GeraGrafo
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

    matriz = MontaMatrizAdjSimples(vertices)

    
    GeraGrafo(matriz, vertices, False, 1)
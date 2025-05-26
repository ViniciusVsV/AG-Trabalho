from Metodos import matrizAdjSimples
from Objetos import Vertice
import pandas as pd

# Isso é só pra teste, modifiquem como quiserem
if __name__ == "__main__":
    ds = pd.read_csv('Datasets/DisciplinasCCO.csv')

    vertices = []

    for index, row in ds.iterrows():
        vertice = Vertice(
            sigla=row['SIGLA'],
            nome=row['NOME'],
            categoria=row['CAT.'],
            semestre=row['PER.'],
            anualidade=row['AN.'],
            horarios=row['HOR.'],
            cargaHor=row['CH'],
            preReq=row['REQ.']
        )
        vertices.append(vertice)
    
    matriz = matrizAdjSimples(vertices)

    for i, vertice in enumerate(vertices):
        print(f"{vertice.sigla} - {vertice.nome}: {vertice.horarios}")
    
    print("\nMatriz de Adjacência Simples:")
    for row in matriz:
        print(row)
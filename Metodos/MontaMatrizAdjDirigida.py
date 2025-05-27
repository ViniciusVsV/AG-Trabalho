from Objetos import Vertice
from Objetos import PreRequisito

def MontaMatrizAdjDirigida(disciplinas: list[Vertice]) -> list[list[int]]:
    """
    Gera uma matriz de adjacência dirigida a partir da lista de disciplinas recebida.
    Args:
        disciplinas (list[Vertice]): Lista de vértices, onde cada vértice representa uma disciplina do curso.
    
    Returns:
        list[list[int]]: Matriz de adjacência representando as relações de dependência (pré-requisito) entre as disciplinas.
    """

    # Inicializa a matriz de adjacência
    n = len(disciplinas)
    matrizAdj = [[0] * n for _ in range(n)]

    # Preenche a matriz de adjacência com as relações de dependência
    for i in range(n):
        for j in range(i + 1, n):
            preRequisitos = PreRequisito(disciplinas[j].preReq)

            if preRequisitos.contem(disciplinas[i].sigla):
                matrizAdj[i][j] = 1

    return matrizAdj
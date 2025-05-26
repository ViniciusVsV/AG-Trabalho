from Objetos import Vertice

def matrizAdjSimples(dataframeFiltrado: list[Vertice]) -> list[list[int]]:
    """
    Gera uma matriz de adjacência simples a partir de um dataframe filtrado.
    Args:
        dataframeFiltrado (list[Vertice]): Lista de vértices filtrados, onde cada vértice representa uma disciplina.
    
    Returns:
        list[list[int]]: Matriz de adjacência representando os conflitos de horários entre as disciplinas.
    """

    # Inicializa a matriz de adjacência
    n = len(dataframeFiltrado)
    matrizAdjacencia = [[0] * n for _ in range(n)]

    # Preenche a matriz de adjacência com os conflitos de horários
    for i in range(n):
        for j in range(i + 1, n):
            if dataframeFiltrado[i].verificaHorarioConflitante(dataframeFiltrado[j]):
                matrizAdjacencia[i][j] = 1
                matrizAdjacencia[j][i] = 1

    return matrizAdjacencia
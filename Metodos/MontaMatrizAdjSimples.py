from Objetos import Vertice

def MontaMatrizAdjSimples(disciplinasFiltradas: list[Vertice]) -> list[list[int]]:
    """
    Gera uma matriz de adjacência simples a partir de uma lista de disciplinas recebida.
    Args:
        disciplinasFiltradas (list[Vertice]): Lista de vértices filtrados, onde cada vértice representa uma disciplina.
    
    Returns:
        list[list[int]]: Matriz de adjacência representando os conflitos de horários entre as disciplinas.
    """

    # Inicializa a matriz de adjacência
    n = len(disciplinasFiltradas)
    matrizAdj = [[0] * n for _ in range(n)]

    # Preenche a matriz de adjacência com os conflitos de horários
    for i in range(n):
        for j in range(i + 1, n):
            if disciplinasFiltradas[i].verificaHorarioConflitante(disciplinasFiltradas[j]):
                matrizAdj[i][j] = 1
                matrizAdj[j][i] = 1

    return matrizAdj
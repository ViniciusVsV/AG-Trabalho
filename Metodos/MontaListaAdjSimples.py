from Objetos import Vertice

def MontaListaAdjSimples(disciplinasFiltradas: list[Vertice]) -> list[list[int]]:
    """
    Gera uma lista de adjacência simples a partir de uma lista de disciplinas recebida.
    Args:
        disciplinasFiltradas (list[Vertice]): Lista de vértices filtrados, onde cada vértice representa uma disciplina.
    
    Returns:
        list[list[int]]: Lista de adjacência representando os conflitos de horários entre as disciplinas.
    """

    # Inicializa a lista de adjacência
    n = len(disciplinasFiltradas)
    listaAdj = [[] for _ in range(n)]

    # Preenche a lista de adjacência com os conflitos de horários
    for i in range(n):
        for j in range(i + 1, n):
            if disciplinasFiltradas[i].verificaHorarioConflitante(disciplinasFiltradas[j]):
                listaAdj[i].append(j)
                listaAdj[j].append(i)

    return listaAdj
from Objetos import Turma

def MontaListaAdjSimples(turmasFiltradas: list[Turma]) -> list[list[int]]:
    """
    Gera uma lista de adjacência simples a partir de uma lista de turmas recebida.
    Args:
        turmasFiltradas (list[Turma]): Lista de vértices filtrados, onde cada vértice representa uma disciplina.
    
    Returns:
        list[list[int]]: Lista de adjacência representando os conflitos de horários entre as turmas.
    """

    # Inicializa a lista de adjacência
    n = len(turmasFiltradas)

    listaAdj = [[] for _ in range(n)]

    # Preenche a lista de adjacência com os conflitos de horários
    for i in range(n):
        for j in range(i + 1, n):
            if turmasFiltradas[i].VerificaHorarioConflitante(turmasFiltradas[j]):
                listaAdj[i].append(j)
                listaAdj[j].append(i)

    return listaAdj
from Objetos import Disciplina

def montaListaAdjDirigida(disciplinas: list[Disciplina]) -> list[list[int]]:
    """
    Gera uma lista de adjacência dirigida a partir da lista de disciplinas recebida.
    Args:
        disciplinas (list[Disciplina]): Lista de vértices, onde cada vértice representa uma disciplina do curso.
    
    Returns:
        list[list[int]]: Lista de adjacência representando as relações de dependência (pré-requisito) entre as disciplinas.
    """

    # Inicializa a lista de adjacência
    n = len(disciplinas)
    listaAdj = [[] for _ in range(n)]

    # Preenche a lista de adjacência com as relações de dependência de forma invertida
    for i in range(n):
        for j in range(i + 1, n):
            if disciplinas[j].isPreRequisito(disciplinas[i]):
                listaAdj[j].append(i)

    return listaAdj
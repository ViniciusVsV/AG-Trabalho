from Objetos import Turma
from Metodos.mwis.branchAndBound import BranchAndBound

def calculaCIM(grafo: tuple[list[Turma], list[list[int]]], carga_horaria: float) -> list[tuple[list[Turma], float]]:
    """
    Obtém os conjuntos independentes máximos do grafo recebido.

    Args:
        grafo (tuple[list[Turma], list[list[int]]]): Tupla contendo a lista de turmas e a lista de adjacências do grafo.
        carga_horaria (float): Carga horária máxima permitida para as turmas selecionadas.
    Retorna:
        list[tuple[list[Turma], float]]: Lista de conjuntos independentes máximos.
    """
    conjuntoIM = BranchAndBound(grafo, carga_horaria)

    return conjuntoIM.calculate_others_cmis(4)
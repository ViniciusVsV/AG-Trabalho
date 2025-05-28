from Objetos import Vertice
from Objetos import PreRequisito

def FiltraDisciplinas(disciplinas: list[Vertice], disciplinasCumpridas: set[str], periodoAtual: int) -> list[Vertice]:
    """
    Filtra a lista de todas as disciplinas recebida, removendo todas as matérias obsoletas para o caso de uso.

    Retorna:
        Lista de vértices representando as matérias pertinentes ao caso de uso.
    """

    disciplinasFiltradas = disciplinas
    
    for disciplina in disciplinas:
        # Filtra da lista as matérias que não estão sendo ofertadas
        if disciplina.semestre % 2 != periodoAtual % 2:
            disciplinasFiltradas.remove(disciplina)

        # Fitlra da lista as matérias que já foram concluidas
        elif disciplina in disciplinasCumpridas:
            disciplinasFiltradas.remove(disciplina)

        # Filtra da lista as matérias cujos pré requisitos não foram atendidos
        elif not preRequisitos.verifica(disciplinasCumpridas):
            disciplinasFiltradas.remove(disciplina)

    return disciplinasFiltradas
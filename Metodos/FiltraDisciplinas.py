from Objetos import Disciplina

def FiltraDisciplinas(disciplinas: list[Disciplina], disciplinasCumpridas: set[str], periodoAtual: int) -> list[Disciplina]:
    """
    Filtra a lista de todas as disciplinas recebida, removendo todas as matérias obsoletas para o caso de uso.
    Args:
        disciplinas (list[Disciplina]): Lista de todas as disciplinas do curso.
        disciplinasCumpridas (set[str]): Set com as disciplinas já cursadas pelo discente.
        periodoAtual (int): Período do ano para o qual a previsão será feita (1 ou 2).
    
    Retorna:
        Lista de vértices representando as matérias pertinentes ao caso de uso.
    """

    disciplinasFiltradas = disciplinas.copy()

    # Adiciona às disciplinas cumpridas todas as equivalentes que também devem ser ditas como cumpridas
    for disciplina in disciplinas:
        if disciplina.codigo in disciplinasCumpridas:
            for equivalente in disciplina.equivalentes.equivalentes:
                disciplinasCumpridas.add(equivalente)

    for disciplina in disciplinas:
        # Filtra da lista as matérias que não estão sendo ofertadas
        if disciplina.semestre % 2 != periodoAtual % 2:
            disciplinasFiltradas.remove(disciplina)

        # Fitlra da lista as matérias que já foram concluidas
        elif disciplina.codigo in disciplinasCumpridas:
            disciplinasFiltradas.remove(disciplina)

        # Filtra da lista as matérias cujos pré requisitos não foram atendidos
        elif not disciplina.atendePreRequisitos(disciplinasCumpridas):
            disciplinasFiltradas.remove(disciplina)

    return disciplinasFiltradas
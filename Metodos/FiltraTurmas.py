from Objetos import Disciplina
from Objetos import Turma

def FiltraTurmas(disciplinas: list[Disciplina], disciplinasCumpridas: set[str], semestreAtual: int) -> list[Turma]:
    """
    Filtra a lista de todas as disciplinas recebida, removendo todas as matérias obsoletas para o caso de uso.
    Args:
        disciplinas (list[Disciplina]): Lista de todas as disciplinas do curso.
        disciplinasCumpridas (set[str]): Set com as disciplinas já cursadas pelo discente.
        semestreAtual (int): Semestre do ano para o qual a previsão será feita (0 ou 1).
    
    Retorna:
        list[Turma]: Lista das turmas pertinentes ao caso de uso.
    """

    # Primeiro, filtra disciplinas
    disciplinasFiltradas = []

    for disciplina in disciplinas:
        # Filtra da lista as disciplinas que já foram concluidas
        if disciplina.sigla in disciplinasCumpridas or disciplina.VerificaEquivalencia(disciplinasCumpridas):
            disciplinasCumpridas.add(disciplina.sigla)
            disciplinasCumpridas.update(disciplina.equivalentes.setEquivalentes)

            continue

        # Filtra da lista as disciplinas cujos pré requisitos não foram atendidos
        if not disciplina.VerificaPreRequisitos(disciplinasCumpridas):
            continue

        # Filtra da lista as disciplinas que possuem co-requisitos que não estão sendo recomendados ou não foram cumpridos
        if disciplina.correquisitos:
            setAux = set(d.sigla for d in disciplinasFiltradas)

            if not disciplina.correquisitos.issubset(setAux.union(disciplinasCumpridas)):
                continue           

        disciplinasFiltradas.append(disciplina)     

    # Segundo, filtra turmas
    turmasFiltradas = []

    for disciplina in disciplinasFiltradas:
        for turma in disciplina.CriaTurmas():
            # Filtra da lista as turmas que não estão sendo ofertadas
            if turma.semestre != semestreAtual % 2:
                continue
            
            turmasFiltradas.append(turma)

    return turmasFiltradas
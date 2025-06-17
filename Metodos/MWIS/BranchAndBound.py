from Objetos import Turma
import copy
import random

class BranchAndBound:
    def __init__(self, G: tuple[list[Turma], list[list[int]]], cargaHorariaMaxima: float):
        """
        Inicializa a classe BranchAndBound com o grafo fornecido.
        Args:
            G (tuple[list[Turma], list[list[int]]]): Tupla contendo a lista de vértices (turmas) e a lista de adjacência do grafo.
        """
        self.__G = (copy.deepcopy(G[0]), G[1].copy()) # É preciso do deepcopy para evitar problemas de referência
        self.__max_indep_set: list[Turma] = []
        self.cargaHorariaMaxima = cargaHorariaMaxima
        self.__max_weight = 0.0
        self.__map = {turma: i for i, turma in enumerate(self.__G[0])}
        self.__branchAndBound(self.__G[0], [], 0.0)
    
    @property
    def cmi(self) -> list[Turma]:
        """
        Retorna o conjunto máximo independente encontrado pelo algoritmo.
        Returns:
            list[Turma]: Lista de turmas que formam o conjunto máximo independente.
        """
        return self.__max_indep_set
    
    
    def calculate_others_cmis(self, count: int) -> list[tuple[list[Turma], float]]:
        """
        Retorna outros conjuntos máximos independentes encontrados pelo algoritmo.
        Args:
            count (int): Número de conjuntos máximos independentes a serem retornados.
        Returns:
            list[list[Turma]]: Lista de listas de turmas que formam os conjuntos máximos independentes.
        """
        cmis = [(self.__max_indep_set, self.__max_weight)]

        for _ in range(count):

            # 1. Usando a turma de maior peso para remoção
            # turma_remove = max(self.__G[0], key=lambda t: t.peso)


            # 2. Procura pela disciplina dentro do conjunto anterior que possui mais conflitos de horário (mais elementos na lista de adjacência) e a remova.
            # turma_remove = max(self.__max_indep_set, key=lambda t: len(self.__G[1][self.__map[t]]))
            
            # 3. Remove usando a disciplian com mais conflito de horário dentro dos 3 maiores pesos
            turma_remove = max(
                sorted(self.__max_indep_set, key=lambda t: t.peso, reverse=True)[:3],
                key=lambda t: len(self.__G[1][self.__map[t]])
            )

            print(f"Removendo turma: {turma_remove.disciplina.sigla} - {turma_remove.horario} ({turma_remove.peso:.3f})")
            
            # Exclusão lógica: Para não remover a turma do grafo original e ter que reconstruir a matriz de adjacência,
            # apenas zeramos o peso dela, o que a torna inelegível para o conjunto independente.
            turma_remove.peso = 0

            self.__max_indep_set = []
            self.__max_weight = 0.0

            self.__branchAndBound(self.__G[0], [], 0.0)
            cmis.append((self.__max_indep_set, self.__max_weight))
        
        return cmis


    @property
    def max_weight(self) -> float:
        """
        Retorna o peso máximo do conjunto independente encontrado pelo algoritmo.
        Returns:
            float: Peso máximo do conjunto independente.
        """
        return self.__max_weight
    
    def __branchAndBound(self, non_processed: list[Turma], current_set: list[Turma], current_weight: float = 0.0):
        """
        Implementa o algoritmo Branch and Bound para encontrar o conjunto máximo independente em um grafo.
        Args:
            non_processed (list[Turma]): Lista de turmas que ainda não foram processadas.
            current_set (list[Turma]): Lista de turmas que formam o conjunto atual.
            current_weight (float): Peso atual do conjunto.
        """

        # === FASE DE DELIMITAÇÃO (BOUNDING) ===
        # Calcula um limite superior para o que pode ser adicionado.
        max_weight_possible = sum(t.peso for t in non_processed)
        if current_weight + max_weight_possible <= self.__max_weight:
            return # Poda
        
        # === VERIFICAÇÃO DE CORREQUISITOS ===
        # Verifica se o conjunto atual atende aos requisitos de correquisito
        # Explicação: Caso o conjunto atual tenha uma disciplina que possui correquisitos, porém o
        # correquisito não é atendido (as disciplinas não estão no conjunto atual), então o ramo é podado.
        if not self.__verifica_correquisitos_atendidos(current_set):
            return

        # === CASO BASE ===
        # Se não há mais turmas a processar no ramo atual, verifica se o conjunto atual é o melhor encontrado.
        if not non_processed:
            if current_weight > self.__max_weight:
                self.__max_weight = current_weight
                self.__max_indep_set = current_set.copy()
            return

        # == FASE DE RAMIFICAÇÃO (BRANCHING) ==
        # Nessa fase, o algoritmo se divide em dois ramos:
        # 1. Incluindo a próxima turma no conjunto atual (eliminando todos os adjacentes).
        # 2. Não incluindo a próxima turma no conjunto atual.

        # Seleciona a próxima turma para considerar.
        (next_turma, rest) = self.__next_turma(non_processed)

        # 1. A turma é incluída no conjunto atual.

        # Verifica se a turma conflita com o conjunto atual e se não ultrapassa o limite de carga horária.
        if not any(self.__map[t] in self.__G[1][self.__map[next_turma]] or t.disciplina.nome == next_turma.disciplina.nome for t in current_set) and\
            sum(t.disciplina.cargaHoraria for t in current_set) + next_turma.disciplina.cargaHoraria <= self.cargaHorariaMaxima:
            new_set = current_set + [next_turma]

            # Remove turma atual e suas adjacências do restante
            new_non_processed = [t for t in rest if self.__map[t] not in self.__G[1][self.__map[next_turma]]]

            # Chama recursivamente com a turma incluída
            self.__branchAndBound(new_non_processed, new_set, current_weight + next_turma.peso)

        # 2. A turma não é incluída no conjunto atual
        self.__branchAndBound(rest, current_set, current_weight)

    def __verifica_correquisitos_atendidos(self, current_set: list[Turma]) -> bool:
        """
        Verifica se o conjunto atual de turmas atende aos requisitos de correquisito.
        Args:
            current_set (list[Turma]): Lista de turmas que formam o conjunto atual.
        Returns:
            bool: True se os requisitos de correquisito forem atendidos, False caso contrário.
        """
        current_sigas = {turma.sigla for turma in current_set}
        for turma in current_set:
            for corr in turma.disciplina.correquisitos:
                if corr not in current_sigas:
                    return False
        return True
    
    def __next_turma(self, lista: list[Turma]) -> tuple[Turma, list[Turma]]:
        """
        Obtém a próxima turma a ser processada.
        Args:
            lista (list[Turma]): Lista de turmas que ainda não foram processadas.
        Returns:
            Turma: A próxima turma a ser processada.
            list[Turma]: Lista de turmas restantes após a remoção da turma selecionada.
        """
        # Abordagem pegando a turma de maior peso
        next_turma = max(lista, key=lambda t: t.peso)
        rest = lista.copy()
        rest.remove(next_turma)
        return next_turma, rest
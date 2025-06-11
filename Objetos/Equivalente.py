from .Expression import tokenizar, ExpressaoFalsa

class Equivalente:
    def __init__(self, equivalentes: str):
        self.__equivalentes = equivalentes
        self.__setEquivalentes = set()

        if equivalentes.strip() == '-':
            self.__expressao = ExpressaoFalsa()
        else:
            (self.__expressao, self.__setEquivalentes) = tokenizar(equivalentes)

    @property
    def setEquivalentes(self) -> set[str]:
        """
        Retorna o conjunto de equivalentes.
        
        Returns:
            set: Conjunto de equivalentes.
        """

        return self.__setEquivalentes

    def __str__(self):
        """
        Retorna a representação em string das equivalentes.

        Returns:
            str: String de equivalentes
        """

        return str(self.__expressao)

    def verifica(self, disciplinasCumpridas: set[str]) -> bool:
        """
        Verifica se a equivalência foi atendida.
        
        Args:
            DisciplinasCumpridas (set): Set de siglas das disciplinas já concluídas.
        Returns:
            bool: True se a equivalência foi atendida, False caso contrário.
        """

        return self.__expressao.avaliar(disciplinasCumpridas)
    
    def contem(self, disciplina: str) -> bool:
        """
        Verifica se a disciplina está incluída no conjunto de equivalentes.

        Args:
            disciplina (str): Sigla da disciplina a ser verificada.
        
        Returns:
            bool: True se a disciplina for equivalente, False caso contrário.
        """

        return disciplina in self.__setEquivalentes


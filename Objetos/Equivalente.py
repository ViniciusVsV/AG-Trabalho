from .Expression import Tokenizar, ExpressaoFalsa

class Equivalente:
    def __init__(self, equivalentes: str):
        self.__equivalentes = equivalentes
        self.__setEquivalentes = set()

        if equivalentes.strip() == '-':
            self.__expressao = ExpressaoFalsa()
        else:
            (self.__expressao, self.__setEquivalentes) = Tokenizar(equivalentes)

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

    def Verifica(self, disciplinasCumpridas: set[str]) -> bool:
        """
        Verifica se a equivalência foi atendida.
        
        Args:
            DisciplinasCumpridas (set): Set de siglas das disciplinas já concluídas.
        Returns:
            bool: True se a equivalência foi atendida, False caso contrário.
        """

        return self.__expressao.Avaliar(disciplinasCumpridas)


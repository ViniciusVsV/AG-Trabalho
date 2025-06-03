class Equivalente:
    def __init__(self, equivalentes: str):
        self.__equivalentes = equivalentes

        self.__set = self.__parseEquivalente()

    def __parseEquivalente(self) -> set[str]:
        """
        Converte a string de equivalências em uma lista siglas.

        Returns:
            set[str]: Conjunto de siglas individuais.
        """

        if self.__equivalentes == "-" or not self.__equivalentes:
            return {}
        
        equivalencias = set([eq.strip() for eq in self.__equivalentes.split(",")])

        return equivalencias

    @property
    def equivalentes(self) -> set[str]:
        """
        Lista de equivalências.

        Returns:
            set[str]: Conjunto de siglas das disciplinas equivalentes.
        """
        return self.__set
    
    def __str__(self):
        """
        Representação em string do objeto Equivalente.

        Returns:
            str: String formatada com as equivalências.
        """
        return self.__equivalentes


class Equivalente:
    def __init__(self, equivalentes: str):
        self.__equivalentes = equivalentes

        self.__list = self.__parseEquivalente()

    def __parseEquivalente(self) -> list[str]:
        """
        Converte a string de equivalências em uma lista siglas.

        Returns:
            list[str]: Conjunto de siglas individuais.
        """

        if self.__equivalentes == "-" or not self.__equivalentes:
            return []
        
        equivalencias = [eq.strip() for eq in self.__equivalentes.split(",")]

        return equivalencias
    
    def getEquivalencias(self) -> list[str]:
        """
        Getter da lista de equivalências.

        Returns:
            list[str]: Conjunto de siglas das disciplinas equivalentes.
        """
        return self.__list
        


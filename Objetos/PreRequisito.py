from .Expression import tokenizar, ExpressaoVerdadeira

class PreRequisito:
    """
    Classe que representa um pré-requisito.
    """

    def __init__(self, preRequisitos: str):
        self.__preRequisitos = preRequisitos
        self.__setPreRequisitos = set()

        if preRequisitos.strip() == '-':
            self.expressao = ExpressaoVerdadeira()
        else:
            (self.expressao, self.__setPreRequisitos) = tokenizar(preRequisitos)

    @property
    def setPreRequisitos(self) -> set[str]:
        """
        Retorna o conjunto de pré-requisitos.
        
        Returns:
            set: Conjunto de pré-requisitos.
        """

        return self.__setPreRequisitos

    def __str__(self):
        """
        Retorna a representação em string do pré-requisito.
        """

        return str(self.expressao)
    
    def verifica(self, disciplinasCumpridas: set[str]) -> bool:
        """
        Verifica se o pré-requisito foi atendido.

        Args:
            disciplinasCumpridas (set[str]): Set de siglas das disciplinas já concluídas.
        
        Returns:
            bool: True se o pré-requisito foi atendido, False caso contrário.
        """

        return self.expressao.avaliar(disciplinasCumpridas)
    
    def contem(self, sigla: str) -> bool:
        """
        Verifica se uma matéria é um pré-requisito.
        
        Args:
            sigla (str): Sigla da matéria a ser analisada.
        
        Returns:
            bool: True se a matéria é um pré-requisito, False caso contrário.
        """
    
        return sigla in self.setPreRequisitos
from .Expression import TrueExpression, tokenize
class PreRequisito:
    """
    Classe que representa um pré-requisito.
    """
    def __init__(self, pre_requisito: str):
        self.__pre_requisito = pre_requisito
        self.__pre_reqset = set()

        if pre_requisito.strip() == '-':
            self.__expression = TrueExpression()
        else:
            (self.__expression, self.__pre_reqset) = tokenize(pre_requisito)

    @property
    def pre_reqset(self) -> set[str]:
        """
        Retorna o conjunto de pré-requisitos.
        Returns:
            set: Conjunto de pré-requisitos.
        """
        return self.__pre_reqset

    def __str__(self):
        """
        Retorna a representação em string do pré-requisito.
        """
        return str(self.__expression)
    
    def verifica(self, taken_courses: set[str]) -> bool:
        """
        Verifica se o pré-requisito foi atendido.
        Args:
            taken_courses (set): Lista de cursos já concluídos.
        Returns:
            bool: True se o pré-requisito foi atendido, False caso contrário.
        """
        return self.__expression.evaluate(taken_courses)
    
    def contem(self, sigla: str) -> bool:
        """
        Verifica se uma matéria é um pré-requisito.
        Args:
            sigla (str): Sigla da matéria a ser analisada.
        Returns:
            bool: True se a matéria é um pré-requisito, False caso contrário.
        """
    
        return sigla in self.pre_reqset
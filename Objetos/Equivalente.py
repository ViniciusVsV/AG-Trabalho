from .Expression import tokenize, FalseExpression

class Equivalente:
    def __init__(self, equivalentes: str):
        self.__equivalentes = equivalentes
        self.__eq_set = set()

        if equivalentes.strip() == '-':
            self.__expression = FalseExpression()
        else:
            (self.__expression, self.__eq_set) = tokenize(equivalentes)

    @property
    def eq_set(self) -> set[str]:
        """
        Retorna o conjunto de equivalentes.
        Returns:
            set: Conjunto de equivalentes.
        """
        return self.__eq_set

    def __str__(self):
        """
        Retorna a representação em string das equivalentes.
        """
        return str(self.__expression)

    def verifica(self, taken_courses: set[str]) -> bool:
        """
        Verifica se a equivalência foi atendido.
        Args:
            taken_courses (set): Lista de cursos já concluídos.
        Returns:
            bool: True se a equivalência foi atendida, False caso contrário.
        """
        return self.__expression.evaluate(taken_courses)


class Expression:
    """
    Classe que representa uma expressão.
    """
    def evaluate(self, taken_courses: set[str]):
        raise NotImplementedError("Subclasses devem implementar o método evaluate.")

class Leaf(Expression):
    """
    Classe que representa uma folha na árvore de expressão.
    """
    def __init__(self, course_code: str):
        self.course_code = course_code

    def evaluate(self, taken_courses: set[str]):
        """
        Avalia se o curso foi concluído.
        Args:
            taken_courses (set): Lista de cursos já concluídos.
        Returns:
            bool: True se o curso foi concluído, False caso contrário.
        """
        return self.course_code in taken_courses
    
    def __str__(self):
        """
        Retorna a representação em string do curso.
        """
        return self.course_code
    
class And(Expression):
    """
    Classe que representa uma operação AND na árvore de expressão.
    """
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def evaluate(self, taken_courses: set[str]):
        """
        Avalia a expressão AND.
        Args:
            taken_courses (set): Lista de cursos já concluídos.
        Returns:
            bool: True se ambas as expressões forem verdadeiras, False caso contrário.
        """
        return self.left.evaluate(taken_courses) and self.right.evaluate(taken_courses)
    
    def __str__(self):
        """
        Retorna a representação em string da expressão AND.
        """
        return f"{self.left} E {self.right}"

class Or(Expression):
    """
    Classe que representa uma operação OR na árvore de expressão.
    """
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def evaluate(self, taken_courses: set[str]):
        """
        Avalia a expressão OR.
        Args:
            taken_courses (set): Lista de cursos já concluídos.
        Returns:
            bool: True se pelo menos uma das expressões for verdadeira, False caso contrário.
        """
        return self.left.evaluate(taken_courses) or self.right.evaluate(taken_courses)
    
    def __str__(self):
        """
        Retorna a representação em string da expressão OR.
        """
        return f"({self.left} OU {self.right})"

class FalseExpression(Expression):
    """
    Classe que representa uma expressão falsa.
    """
    def evaluate(self, _):
        """
        Avalia a expressão falsa.
        Args:
            taken_courses (set): Lista de cursos já concluídos.
        Returns:
            bool: Sempre retorna False.
        """
        return False
    
    def __str__(self):
        """
        Retorna a representação em string da expressão falsa.
        """
        return "False"

class Equivalente:
    def __init__(self, equivalentes: str):
        self.__equivalentes = equivalentes
        self.__eq_set = set()

        if equivalentes.strip() == '-':
            self.__expression = FalseExpression()
        else:
            self.__tokenize()

    @property
    def eq_set(self) -> set[str]:
        """
        Retorna o conjunto de equivalentes.
        Returns:
            set: Conjunto de equivalentes.
        """
        return self.__eq_set

    def __tokenize(self):
        """
        Tokeniza a string de equivalentes.
        """
        tokens = self.__equivalentes.replace('(', ' ( ').replace(')', ' ) ').strip().split()
        stack = []
        current = None
        parentheses = 0

        for token in tokens:
            if token == '(':
                parentheses += 1
                if current is not None:
                    stack.append(current)
                current = None
            elif token == ')':
                if parentheses == 0:
                    raise ValueError("Parênteses não balanceados")
                parentheses -= 1
                if len(stack) > 0:
                    temp = stack.pop()
                    if isinstance(temp, And) or isinstance(temp, Or):
                        temp.right = current
                        current = temp
                    else:
                        raise ValueError("Token inesperado dentro de parênteses")
            elif token == 'E':
                if current is None:
                    raise ValueError("Operador 'E' não pode ser o primeiro token")
                current = And(current, None)
            elif token == 'OU':
                if current is None:
                    raise ValueError("Operador 'OU' não pode ser o primeiro token")
                current = Or(current, None)
            else:
                self.eq_set.add(token)
                if current is None:
                    current = Leaf(token)
                elif not isinstance(current, Leaf):
                    current.right = Leaf(token)
                else:
                    raise ValueError(f"Token inesperado: {token}")
                
        if parentheses > 0:
            raise ValueError("Parênteses não balanceados")
        
        if current is None:
            raise ValueError("Expressão vazia")
        
        if not isinstance(current, Leaf) and current.right is None:
            raise ValueError("Expressão incompleta, falta um operando")
        
        self.__expression = current

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


class Expression:
    """
    Classe que representa uma expressão.
    """
    def evaluate(self, elements: set[str]):
        raise NotImplementedError("Subclasses devem implementar o método evaluate.")

class Leaf(Expression):
    """
    Classe que representa uma folha na árvore de expressão.
    """
    def __init__(self, elements: str):
        self.elements = elements

    def evaluate(self, elements: set[str]):
        """
        Avalia se o curso foi concluído.
        Args:
            elements (set): Lista de elementos.
        Returns:
            bool: True se o elemento estiver na lista, False caso contrário.
        """
        return self.elements in elements
    
    def __str__(self):
        """
        Retorna a representação em string.
        """
        return self.elements
    
class And(Expression):
    """
    Classe que representa uma operação AND na árvore de expressão.
    """
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def evaluate(self, elements: set[str]):
        """
        Avalia a expressão AND.
        Args:
            taken_courses (set): Lista elementos.
        Returns:
            bool: True se ambas as expressões forem verdadeiras, False caso contrário.
        """
        return self.left.evaluate(elements) and self.right.evaluate(elements)
    
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

    def evaluate(self, elements: set[str]):
        """
        Avalia a expressão OR.
        Args:
            elements (set): Lista de cursos já concluídos.
        Returns:
            bool: True se pelo menos uma das expressões for verdadeira, False caso contrário.
        """
        return self.left.evaluate(elements) or self.right.evaluate(elements)
    
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
            elements (set): Lista de cursos já concluídos.
        Returns:
            bool: Sempre retorna False.
        """
        return False
    
    def __str__(self):
        """
        Retorna a representação em string da expressão falsa.
        """
        return "False"


class TrueExpression(Expression):
    """
    Classe que representa uma expressão verdadeira.
    """
    def evaluate(self, _):
        """
        Avalia a expressão verdadeira.
        Args:
            elements (set): Lista de cursos já concluídos.
        Returns:
            bool: Sempre retorna True.
        """
        return True
    
    def __str__(self):
        """
        Retorna a representação em string da expressão verdadeira.
        """
        return "True"

def tokenize(expression: str):
        """
        Tokeniza uma expressão lógica em uma árvore de expressão.

        Args:
            expression (str): A expressão lógica a ser tokenizada.

        Returns:
            Expression: A raiz da árvore de expressão resultante.
            Operands: Um conjunto de operandos encontrados na expressão.
        """
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').strip().split()
        stack = []
        current = None
        parentheses = 0
        operands = set()

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
                operands.add(token)
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
        
        return current, operands
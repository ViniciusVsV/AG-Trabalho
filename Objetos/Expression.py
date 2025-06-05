class Expressao:
    """
    Classe que representa uma expressão.
    """

    def Avaliar(self, elementos: set[str]):
        raise NotImplementedError("Subclasses devem implementar o método Avaliar.")

class Folha(Expressao):
    """
    Classe que representa uma folha na árvore de expressão.
    """

    def __init__(self, elementos: str):
        self.elementos = elementos

    def Avaliar(self, elementos: set[str]):
        """
        Avalia se o curso foi concluído.
        Args:
            elementos (set): Lista de elementos.
        Returns:
            bool: True se o elemento estiver na lista, False caso contrário.
        """
        return self.elementos in elementos
    
    def __str__(self):
        """
        Retorna a representação em string.
        """

        return self.elementos
    
class And(Expressao):
    """
    Classe que representa uma operação AND na árvore de expressão.
    """

    def __init__(self, esqueda: Expressao, direita: Expressao):
        self.esqueda = esqueda
        self.direita = direita

    def Avaliar(self, elementos: set[str]):
        """
        Avalia a expressão AND.

        Args:
            taken_courses (set): Lista elementos.
        
        Returns:
            bool: True se ambas as expressões forem verdadeiras, False caso contrário.
        """

        return self.esqueda.Avaliar(elementos) and self.direita.Avaliar(elementos)
    
    def __str__(self):
        """
        Retorna a representação em string da expressão AND.
        """

        return f"{self.esqueda} E {self.direita}"

class Or(Expressao):
    """
    Classe que representa uma operação OR na árvore de expressão.
    """

    def __init__(self, esquerda: Expressao, direita: Expressao):
        self.esquerda = esquerda
        self.direita = direita

    def Avaliar(self, elements: set[str]):
        """
        Avalia a expressão OR.
        
        Args:
            elements (set): Lista de cursos já concluídos.
        
        Returns:
            bool: True se pelo menos uma das expressões for verdadeira, False caso contrário.
        """

        return self.esquerda.Avaliar(elements) or self.direita.Avaliar(elements)
    
    def __str__(self):
        """
        Retorna a representação em string da expressão OR.
        """

        return f"({self.esquerda} OU {self.direita})"

class ExpressaoFalsa(Expressao):
    """
    Classe que representa uma expressão falsa.
    """

    def Avaliar(self, _):
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


class ExpressaoVerdadeira(Expressao):
    """
    Classe que representa uma expressão verdadeira.
    """

    def Avaliar(self, _):
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

def Tokenizar(expressao: str):
        """
        Tokeniza uma expressão lógica em uma árvore de expressão.

        Args:
            expressao (str): A expressão lógica a ser tokenizada.

        Returns:
            Expressao: A raiz da árvore de expressão resultante.
            Operandos: Um conjunto de operandos encontrados na expressão.
        """
       
        tokens = expressao.replace('(', ' ( ').replace(')', ' ) ').strip().split()
        stack = []
        
        atual = None
        parenteses = 0

        operandos = set()

        for token in tokens:
            if token == '(':
                parenteses += 1
                if atual is not None:
                    stack.append(atual)
                atual = None
            elif token == ')':
                if parenteses == 0:
                    raise ValueError("Parênteses não balanceados")
                parenteses -= 1
                if len(stack) > 0:
                    temp = stack.pop()
                    if isinstance(temp, And) or isinstance(temp, Or):
                        temp.direita = atual
                        atual = temp
                    else:
                        raise ValueError("Token inesperado dentro de parênteses")
            elif token == 'E':
                if atual is None:
                    raise ValueError("Operador 'E' não pode ser o primeiro token")
                atual = And(atual, None)
            elif token == 'OU':
                if atual is None:
                    raise ValueError("Operador 'OU' não pode ser o primeiro token")
                atual = Or(atual, None)
            else:
                operandos.add(token)
                if atual is None:
                    atual = Folha(token)
                elif not isinstance(atual, Folha):
                    atual.direita = Folha(token)
                else:
                    raise ValueError(f"Token inesperado: {token}")
                
        if parenteses > 0:
            raise ValueError("Parênteses não balanceados")
        
        if atual is None:
            raise ValueError("Expressão vazia")
        
        if not isinstance(atual, Folha) and atual.direita is None:
            raise ValueError("Expressão incompleta, falta um operando")
        
        return atual, operandos
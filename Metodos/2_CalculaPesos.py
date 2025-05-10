def CalculaPesos(vertices):
    """
    Instancia um novo grafo direcionado com as matérias do dataset pertinente ao caso de uso e calcula os pesos destes.
    Os pesos serão calculados percorrendo o grafo de trás para frente, somando ao vértice atual os pesos de todos os vértices predecessores.
    
    Retorna:
        Novo grafo instanciado com pesos dos vértices calculados.
    """
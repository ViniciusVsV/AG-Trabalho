def AdicionaArestas(grafo):
    """
    Adiciona arestas ao grafo recebido seguindo a ordem dos pesos (maior => menor). Leva em consideração as cores do grafo.
    Inicialmente calcula o caminho mais otimizado, com o melhor peso. Depois, analisa os conflitos dos vértices desse caminho e remove os que possuem mais conflitos e calcula um novo caminho.
        
    Retorna:
        Grafo com um trajeto configurado.
    """
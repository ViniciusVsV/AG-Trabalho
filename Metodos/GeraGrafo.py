from Objetos import Vertice

from igraph import Graph

def GeraGrafo(matrizAdj: list[list[int]], disciplinas: list[Vertice], dirigido: bool) -> None:
    """
    Gera e salva uma grafo, simples ou dirigido, a partir da matriz de adjacencia recebida
    Args:
        matrizAdj (list[list[int]]): Matriz de adjacência do grafo a ser construído.
        disciplinas (list[Vertice]): Lista das disciplinas que serão incluidas no grafo.
        dirigido (bool):  Booleana que dita se o grafo é dirigido ou não

    Retorna:
        
    """

    grafo = Graph(directed = dirigido)

    # Adiciona os vértices
    siglasPrefixos = []
    siglasNormais = []
    cores = []
    
    for disciplina in disciplinas:
        siglasPrefixos.append(disciplina.curso + "_" + disciplina.sigla)
        siglasNormais.append(disciplina.sigla)

        cores.append(
            "lightblue" if disciplina.categoria == "OBRIGATORIA" else
            "yellow" if disciplina.categoria == "EQUIVALENTE" else
            "orange"
        )


    grafo.add_vertices(siglasPrefixos)  

    grafo.vs["label"] = siglasNormais
    grafo.vs["color"] = cores

    # Adiciona as arestas
    quantidadeVertices = len(matrizAdj)

    if dirigido == True:
        for i in range(quantidadeVertices):
            for j in range(quantidadeVertices):
                if matrizAdj[i][j] == 1:
                    grafo.add_edge(siglasPrefixos[j], siglasPrefixos[i])

    else:
        for i in range(quantidadeVertices):
            for j in range(i):
                if matrizAdj[i][j] == 1:
                    grafo.add_edge(siglasPrefixos[i], siglasPrefixos[j])

    # Desenha o grafo


    # Salva a imagem produzida
    
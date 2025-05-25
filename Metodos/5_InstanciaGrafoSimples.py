import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def InstanciaGrafoSimples(dataframeFiltrado):
    """
    Instancia um novo grafo simples com o dataframe recebido.
    As arestas deverão representar os conflitos de horários entre matérias.
            
    Retorna:
        Matriz de adjacência do novo grafo simples instanciado.
    """

    #criar um array de vértices (classe).
    vertices = [1, 2, 3, 4]

    qtdVertices = len(vertices)

    #Instanciar uma matriz de adjacência VxV com valores zerados
    matrizAdj = np.zeros((qtdVertices, qtdVertices))

    #Percorrer a matriz e checar se haverão conexões (caso haja conflito de horário)
    for v in matrizAdj:
        for u in matrizAdj[v]:
            if v == u: continue #como não haverão loops, ignora esse caso

            #Checar se há conflito de horário
            

            if sim: #Se houver conflito 
                matrizAdj[v][u] = 1
                matrizAdj[u][v] = 1

    #Instanciar o grafo simples com networkX
    grafoSimples = nx.Graph()

    #adicionar os vértices
    #o label deverá ser a sigla
    #a coloração deverá ser baseada na categoria (lightblue = obrigatória, yellow = equivalente, green = optativa)
    grafoSimples.add_nodes_from()

    #adicionar as arestas a partir da matriz de adjacência
    grafoSimples.add_edges_from(matrizAdj)

    #desenhar o grafo para identificação visual
    nx.draw(grafoSimples)
    plt.show()

    #retornar matriz de adjacência
    return matrizAdj

InstanciaGrafoSimples(1)
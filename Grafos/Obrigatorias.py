import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

#Função que instancia um grafo com todas as matérias obrigatórias e suas conexões
#Deverá criar o grafo e já calcular os respectivos pesos dos nós
def InstanciaObrigatorias():
    #Lê o dataset do arquivo .csv
    df = pd.read_csv("Obrigatorias.csv")

    vertices = {}
    arestas = {}

    #Cria e preenche os dicionários de vértices e arestas
    k = 0 
    ultimoX = 1
    for _, j in df.iterrows():
        x = int(j["PER."]) - 1

        if x != ultimoX: k = 0; 
        ultimoX = x
        
        y = 5 - k
        k += 1

        vertices[j["SIGLA"]] = ((x, y), j["PER."], j["DISCIPLINA"], j["CH"])
        arestas[j["SIGLA"]] = (j["PRE REQ."])

    #Cria e preenche o grafo
    grafo = nx.DiGraph()

    #Adiciona nós
    for sigla, ((x, y), periodo, disciplina, ch) in vertices.items():
        grafo.add_node(sigla, pos=(x, y), label=disciplina)

    #Adiciona arestas
    for sigla, (pre_reqs) in arestas.items():
        if pre_reqs != "-":
            for pre_req in pre_reqs.split(","):
                pre_req = pre_req.strip()
                if pre_req in grafo.nodes:
                    grafo.add_edge(pre_req, sigla)

    pos = nx.get_node_attributes(grafo, 'pos')
    labels = nx.get_node_attributes(grafo, 'label')

    #Desenha o grafo
    plt.figure(figsize=(12, 6))
    nx.draw(grafo, pos, with_labels=False, node_size=1000, node_color='lightblue', arrows=True)
    nx.draw_networkx_labels(grafo, pos, labels=labels, font_size=6, font_color="red")

    plt.show()

InstanciaObrigatorias()
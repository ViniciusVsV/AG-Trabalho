from Objetos import Disciplina

from igraph import Graph, plot
import os

def GeraGrafoDisciplina(listaAdj: list[list[int]], disciplinas: list[Disciplina], dirigido: bool, id: int, curso: str) -> tuple[Graph, str]:
    """
    Gera e salva uma grafo, simples ou dirigido, a partir da lista de adjacencia de disciplinas recebida
    Args:
        listaAdj (list[list[int]]): Lista de adjacência do grafo a ser construído.
        disciplinas (list[Disciplina]): Lista das disciplinas que serão incluidas no grafo.
        dirigido (bool):  Booleana que dita se o grafo é dirigido ou não.

    Retorna:
        Grafo produzido com igraph.
    """

    grafo = Graph(directed = dirigido)

    # Adiciona os vértices
    siglasPrefixos = []
    codigosNormais = []
    cores = []
    i = 0
    
    for disciplina in disciplinas:
        siglasPrefixos.append(str(i) + "_" + disciplina.codigo)
        codigosNormais.append(disciplina.codigo)

        cores.append(
            "lightblue" if disciplina.categoria == "OBRIGATORIA" else
            "yellow" if disciplina.categoria == "EQUIVALENTE" else
            "orange"
        )

        i += 1

    grafo.add_vertices(siglasPrefixos)  

    grafo.vs["label"] = codigosNormais
    grafo.vs["color"] = cores

    # Adiciona as arestas
    if dirigido == True:
        for i in range(len(listaAdj)):
            for j in listaAdj[i]:
                grafo.add_edge(siglasPrefixos[i], siglasPrefixos[j])

    else:
        for i in range(len(listaAdj)):
            for j in listaAdj[i]:
                if i < j:
                    grafo.add_edge(siglasPrefixos[i], siglasPrefixos[j])

    # Desenha o grafo e salva a imagem dele em um arquivo
    if dirigido:    layout = grafo.layout("tree")
    else:           layout = grafo.layout("fr")

    caminhoDiretorio = os.path.join(".", "Imagens", f"Teste_{curso}_{id}")
    os.makedirs(caminhoDiretorio, exist_ok = True)

    nomeImagem = "Grafo_Pre_Requisitos.png" if dirigido else "Grafo_Conflitos_Horarios.png"

    diretorio = os.path.abspath(os.path.join(caminhoDiretorio, nomeImagem))

    plot(
        grafo,
        layout = layout,
        vertex_label = codigosNormais,
        vertex_color = grafo.vs["color"],
        vertex_size = 60,
        edge_color = "gray",
        bbox = (2000, 2000),
        margin = 50,
        target = diretorio
    )

    mensagem = "Grafo salvo em Imagens/Teste_" + str(id) + "/" + nomeImagem

    return grafo, mensagem
    
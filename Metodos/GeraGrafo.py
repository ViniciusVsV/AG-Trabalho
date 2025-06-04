from Objetos import Disciplina

from igraph import Graph, plot
import os

def GeraGrafo(listaAdj: list[list[int]], disciplinas: list[Disciplina], id: int, curso: str, dirigido: bool) -> None:
    """
    Gera e salva uma grafo, simples ou dirigido, a partir da lista de adjacencia de disciplinas recebida
    Args:
        listaAdj (list[list[int]]): Lista de adjacência do grafo a ser construído.
        disciplinas (list[Disciplina]): Lista das disciplinas a serem incluidas no grafo.
        dirigido (bool):  Booleana que dita se o grafo é dirigido ou não.

    Retorna:
        None
    """ 

    # Chama a função pertinente para obter os dados necessários
    (grafo, layout, nomeImagem) = (
        GeraGrafoPreRequisitos(listaAdj, disciplinas) if dirigido == True
        else GeraGrafoConflitosHorario(listaAdj, disciplinas)
    )

    # Obtém, ou cria, o diretório para salvar as imagens
    caminhoDiretorio = os.path.join(".", "Imagens", f"Teste_{curso}_{id}")
    os.makedirs(caminhoDiretorio, exist_ok = True)

    diretorio = os.path.abspath(os.path.join(caminhoDiretorio, nomeImagem))

    # Desenha o grafo e gera a imagem
    plot(
        grafo,
        layout = layout,
        vertex_label = grafo.vs["label"],
        vertex_color = grafo.vs["color"],
        vertex_size = 60,
        edge_color = "gray",
        bbox = (2000, 2000),
        margin = 50,
        target = diretorio
    )

def GeraGrafoPreRequisitos(listaAdj: list[list[int]], disciplinas: list[Disciplina]) -> tuple[Graph, str, str]:
    grafo = Graph(directed = True)

    # Cria e adiciona os vértices
    siglasPrefixos = []
    siglasNormais = []
    cores = []
    i = 0
    
    for disciplina in disciplinas:
        siglasPrefixos.append(str(i) + "_" + disciplina.sigla)
        siglasNormais.append(disciplina.sigla)

        cores.append(
            "lightblue" if disciplina.categoria == "OBRIGATORIA" else
            "yellow" if disciplina.categoria == "EQUIVALENTE" else
            "orange"
        )

        i += 1

    grafo.add_vertices(siglasPrefixos)  

    grafo.vs["label"] = siglasNormais
    grafo.vs["color"] = cores

    # Adiciona as arestas
    for i in range(len(listaAdj)):
        for j in listaAdj[i]:
            grafo.add_edge(siglasPrefixos[i], siglasPrefixos[j])

    # Define o layout do grafo e retorna os dados
    layout = grafo.layout("tree")

    return grafo, layout, "Grafo_Pre_Requisitos.png"

def GeraGrafoConflitosHorario(listaAdj: list[list[int]], disciplinas: list[Disciplina]) -> tuple[Graph, str, str]:
    grafo = Graph(directed = False)

    # Adiciona os vértices
    siglasPrefixos = []
    siglasNormais = []
    cores = []
    i = 0

    for disciplina in disciplinas:
        turmas = disciplina.criaTurmas()

        for turma in turmas:
            siglasPrefixos.append(str(i) + "_" + disciplina.sigla)
            siglasNormais.append(disciplina.sigla)

            cores.append(
                "lightblue" if disciplina.categoria == "OBRIGATORIA" else
                "yellow" if disciplina.categoria == "EQUIVALENTE" else
                "orange"
            )

            i += 1

    grafo.add_vertices(siglasPrefixos)  

    grafo.vs["label"] = siglasNormais
    grafo.vs["color"] = cores

    # Adiciona as arestas
    for i in range(len(listaAdj)):
            for j in listaAdj[i]:
                if i < j:
                    grafo.add_edge(siglasPrefixos[i], siglasPrefixos[j])

    # Define o layout para o grafo e retorna os dados
    layout = grafo.layout("fr")

    return grafo, layout, "Grafo_Conflitos_Horario.png"
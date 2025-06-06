from Objetos import Disciplina, Turma

from igraph import Graph, plot
import os

def GeraGrafoPreRequisitos(listaAdj: list[list[int]], disciplinas: list[Disciplina], curso: str) -> None:
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

    DesenhaGrafo(grafo, layout, curso, "GrafoPreRequisitos.png", True)

def GeraGrafoConflitosHorario(listaAdj: list[list[int]], turmas: list[Turma], curso: str, interconectado: bool = False) -> None:
    grafo = Graph(directed = False)

    # Adiciona os vértices
    siglasPrefixos = []
    siglasNormais = []
    cores = []
    i = 0

    for turma in turmas:
        siglasPrefixos.append(str(i) + "_" + turma.sigla)
        siglasNormais.append(turma.sigla)

        cores.append(
            "lightblue" if turma.disciplina.categoria == "OBRIGATORIA" else
            "yellow" if turma.disciplina.categoria == "EQUIVALENTE" else
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

    nomeImagem = "GrafoConflitosHorariosInterconectado.png" if interconectado else "GrafoConflitosHorarios.png"

    DesenhaGrafo(grafo, layout, curso, nomeImagem, False)

def DesenhaGrafo(grafo: Graph, layout: str, curso: str, nomeImagem: str, preRequisito: bool) -> None:
    """
    Desenha e salva um grafo, simples ou dirigido, no diretorio referente ao caso de uso
    
    Args:
        grafo (Graph): Grafo montado a ser desenhado e salvo.
        curso (str): Curso do discente.
        nomeImagem (str): Nome do arquivo da imagem que será salva.
        preRequisito (bool): Caso o grafo produzido é de pré-requisistos (dirigido).
    
    Retorna:
        None
    """ 

    # Obtém, ou cria, o diretório para salvar as imagens
    caminhoDiretorio = os.path.join(".", "Resultados", curso) if preRequisito else\
        os.path.join(".", "Resultados", curso)

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
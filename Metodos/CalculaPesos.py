from Objetos import Disciplina, Optativa

classeOptativa = Optativa()
optativasPreferidas = set[str]

def calculaPesos(listaAdj: list[list[int]], disciplinas: list[Disciplina], numeroTrilha: int, curso: str) -> list[Disciplina]:
    """
    Calcula os pesos dos vértices do grafo dirigido recebido com uma BFS.
    Os pesos serão calculados percorrendo o grafo de trás para frente (matéria mais ao fim do curso para a mais ao inícnio), somando ao vértice atual os pesos de todos os vértices predecessores.
    Args:
        listaAdj (list[list[int]]): Lista de adjacência do grafo a ser analisado
        disciplinas (list[Disciplina]): Lista das disciplinas inclusas no grafo.

    Retorna:
        Lista de disciplinas (vértices) com pesos calculados.
    """

    global optativasPreferidas
    optativasPreferidas = classeOptativa.getTrilha(numeroTrilha, curso)

    # Obtém os índices dos vértices com grau de entrada zero
    n = len(listaAdj)
    grausEntrada = [0] * n

    for i in listaAdj:
        for j in i:
            grausEntrada[j] += 1

    indicesVerticesIniciais = [i for i, grau in enumerate(grausEntrada) if grau == 0]

    # Inicia a DFS multínicio a partir dos vértices iniciais
    for indiceV in indicesVerticesIniciais:
        DFS(indiceV, listaAdj, disciplinas, 1.0)

    return disciplinas

def DFS(indiceV: int, listaAdj: list[list[int]], disciplinas: list[Disciplina], pesoPropagado: float):
    # Obtém os multiplicadores de pesos
    [multiplicadorAnualidade, multiplicadorCategoria] = obtemMultiplicadores(disciplinas[indiceV])

    # Soma o peso base ao peso propagado vezes os multiplicadores
    disciplinas[indiceV].peso += pesoPropagado * multiplicadorAnualidade * multiplicadorCategoria

    # Chama a DFS para os adjacentes, com o peso propagado sendo o peso calculado para o vértice atual
    for adjacente in listaAdj[indiceV]:
        DFS(adjacente, listaAdj, disciplinas, disciplinas[indiceV].peso)

def obtemMultiplicadores(disciplina: Disciplina) -> tuple[float, float]:
    """
    Obtém os valores para os multiplicadores do peso de acordo com a anualidade e categoria da disciplina.
    Args:
        disciplina (Disciplina): Disciplina sendo analisada.

    Retorna:
        Tupla com os multiplicadores de anualidade e categoria, respectivamente.
    """

    global optativasPreferidas

    multiplicadorAnualidade = 1.2 if disciplina.anualidade == "SIM" else 1.0

    multiplicadorOptativa = (
        0.8 if disciplina.sigla in optativasPreferidas
        else 0.6 if disciplina.sigla in classeOptativa.optativasComputacao
        else 0.4
    )  

    multiplicadorCategoria = (
        1.4 if disciplina.categoria == "OBRIGATORIA"
        else 1.0 if disciplina.categoria == "EQUIVALENTE"
        else multiplicadorOptativa
    )   

    return (multiplicadorAnualidade, multiplicadorCategoria)
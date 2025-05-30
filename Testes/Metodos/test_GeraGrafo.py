import pytest
from Metodos.GeraGrafo import GeraGrafo
from Objetos.Vertice import Vertice

@pytest.mark.parametrize("listaAdj, disciplinas, dirigido, id, expected", [
    # Teste da geração de um grafo dirigido
    (
        [
            [],
            [0],
            [0],
            [1, 2]
        ],
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 2, "NÃO", "2M23 3T2", 60, "MAT101", 0),
            Vertice("MAT102", "CCO", "Química I", "Obrigatória", 2, "NÃO", "4M1 5T2", 60, "MAT101", 0),
            Vertice("FIS102", "CCO", "Química I", "Obrigatória", 3, "NÃO", "4M1 5T2", 60, "FIS101 E MAT102", 0)
        ],
        True,
        0,
        "Grafo salvo em Imagens/Teste_0/Grafo_Pre_Requisitos.png"
    ),

    # Teste da geração de um grafo simples
    (
        [
            [1, 2],
            [0],
            [0]
        ],
        [
            Vertice("MAT101", "CCO", "Matemática I", "Obrigatória", 1, "NÃO", "2M12 3T3", 60, "-", 0),
            Vertice("FIS101", "CCO", "Física I", "Obrigatória", 1, "NÃO", "2M23 3T2", 60, "-", 0),
            Vertice("BIO101", "CCO", "Biologia I", "Obrigatória", 1, "NÃO", "2M1 3T3", 60, "-", 0)
        ],
        False,
        0,
        "Grafo salvo em Imagens/Teste_0/Grafo_Conflitos_Horarios.png"
    )
])
def test_GeraGrafo(listaAdj, disciplinas, dirigido, id, expected):
    [_, mensagem] = GeraGrafo(listaAdj, disciplinas, dirigido, id)
    assert mensagem == expected, f"Esperado {expected}, mas obteve {mensagem} para {mensagem}"

from Objetos.Historico import Historico
import pytest

@pytest.mark.parametrize("caminho_pdf, expected_curso, expected_disciplinas", [
    ("Testes/Historicos/historico_CCO-1.pdf", "CCO", {
        "CAHC04",
        "XDES01",
        "XMAC01",
        "CDES05",
        "IEPG21",
        "ADM51H",
        "XDES04",
        "XMCO01",
        "XAHC01",
        "XDES11"
    }),
])
def test_le_historico(caminho_pdf, expected_curso, expected_disciplinas):
    historico = Historico(caminho_pdf)
    assert historico.curso == expected_curso, f"Curso esperado: {expected_curso}, obtido: {historico.curso}"
    assert historico.disciplinas_aprovadas == expected_disciplinas, \
        f"Disciplinas esperadas: {expected_disciplinas}, obtidas: {list(historico.disciplinas_aprovadas)}. Diferença {expected_disciplinas ^ historico.disciplinas_aprovadas}"
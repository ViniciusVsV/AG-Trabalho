from Objetos.Historico import Historico
import pytest

@pytest.mark.parametrize("caminho_pdf, expected_curso, expected_disciplinas", [
    ("Testes/Historicos/Historico_CCO_1.pdf", "CCO", {
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
def test_leHistorico(caminho_pdf, expected_curso, expected_disciplinas):
    historico = Historico(caminho_pdf)
    assert historico.curso == expected_curso, f"Curso esperado: {expected_curso}, obtido: {historico.curso}"
    assert historico.disciplinasAprovadas == expected_disciplinas, \
        f"Disciplinas esperadas: {expected_disciplinas}, obtidas: {list(historico.disciplinasAprovadas)}. Diferença {expected_disciplinas ^ historico.disciplinasAprovadas}"
import pytest
from Objetos.Equivalente import Equivalente

# Testes de inicialização e parsing válidos
@pytest.mark.parametrize("input_str, taken_courses, expected", [
    ("-", {}, False),
    ("-", {"XDES01"}, False),
    ("XDES01", {}, False),
    ("XDES01", {"XDES01"}, True),
    ("XDES01", {"OTHER"}, False),
    ("CTCO01 OU STCO01", {}, False),
    ("CTCO01 OU STCO01", {"CTCO01"}, True),
    ("CTCO01 OU STCO01", {"STCO01"}, True),
    ("CTCO01 OU STCO01", {"OTHER"}, False),
    ("(CTCO01 OU STCO01) E CRSC04", {"CTCO01", "CRSC04"}, True),
    ("(CTCO01 OU STCO01) E CRSC04", {"STCO01", "CRSC04"}, True),
    ("(CTCO01 OU STCO01) E CRSC04", {"CTCO01"}, False),
    ("(CTCO01 OU STCO01) E CRSC04", {"CRSC04"}, False),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", {"MAT00A", "XMAC01", "CTCO01"}, True),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", {"MAT00A", "XMAC01", "STCO01"}, True),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", {"MAT00A", "XMAC01"}, False),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO02)", {"MAT00A", "XMAC02"}, False)
])
def test_parse_equivalentes_validos(input_str, taken_courses, expected):
    eq = Equivalente(input_str)
    assert eq.verifica(taken_courses) == expected, f"Falha para {input_str} com {taken_courses}"
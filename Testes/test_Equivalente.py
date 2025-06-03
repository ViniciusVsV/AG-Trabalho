import pytest
from Objetos.Equivalente import Equivalente

# Testes de inicialização e parsing válidos
@pytest.mark.parametrize("input_str, expected_list", [
    ("-", {}),                                                  # Nenhuma equivalência
    ("MAT00A", {"MAT00A"}),                                     # Uma equivalência
    ("MAT00A, XDES01", {"MAT00A", "XDES01"}),                   # Duas equivalências
    (" MAT00A , XDES01 ", {"MAT00A", "XDES01"}),                # Espaços extras
    ("MAT00A, XDES01, ABCD02", {"MAT00A", "XDES01", "ABCD02"}), # Três equivalentes
])
def test_parse_equivalentes_validos(input_str, expected_list):
    eq = Equivalente(input_str)
    assert eq.equivalentes == expected_list, f"O parsing de '{input_str}' deveria resultar em {expected_list} porém resultou em {eq.equivalentes}"
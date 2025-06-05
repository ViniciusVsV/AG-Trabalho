import pytest
from Objetos.PreRequisito import PreRequisito

# Casos de teste para o método verifica
test_cases = [
    # Sem pré-requisito
    ("-", {}, True),
    ("-", {"XDES01"}, True),
    # Curso único
    ("XDES01", {}, False),
    ("XDES01", {"XDES01"}, True),
    ("XDES01", {"OTHER"}, False),
    # Combinação OR
    ("CTCO01 OU STCO01", {}, False),
    ("CTCO01 OU STCO01", {"CTCO01"}, True),
    ("CTCO01 OU STCO01", {"STCO01"}, True),
    ("CTCO01 OU STCO01", {"OTHER"}, False),
    # Combinação com parênteses
    ("(CTCO01 OU STCO01) E CRSC04", {"CTCO01", "CRSC04"}, True),
    ("(CTCO01 OU STCO01) E CRSC04", {"STCO01", "CRSC04"}, True),
    ("(CTCO01 OU STCO01) E CRSC04", {"CTCO01"}, False),
    ("(CTCO01 OU STCO01) E CRSC04", {"CRSC04"}, False),
    # Expressão complexa
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", {"MAT00A", "XMAC01", "CTCO01"}, True),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", {"MAT00A", "XMAC01", "STCO01"}, True),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", {"MAT00A", "XMAC01"}, False),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", {"MAT00A", "CTCO01"}, False),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", {"XMAC01", "CTCO01"}, False),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", {}, False),
    # Múltiplos ANDs
    ("MAT00A E XMAC01 E CRSC04", {"MAT00A", "XMAC01", "CRSC04"}, True),
    ("MAT00A E XMAC01 E CRSC04", {"MAT00A", "XMAC01"}, False),
    # Múltiplos ORs
    ("CTCO01 OU STCO01 OU CRSC04", {"CTCO01"}, True),
    ("CTCO01 OU STCO01 OU CRSC04", {"STCO01"}, True),
    ("CTCO01 OU STCO01 OU CRSC04", {"CRSC04"}, True),
    ("CTCO01 OU STCO01 OU CRSC04", {}, False),
]

@pytest.mark.parametrize("prereq_str,taken_courses,expected", test_cases)
def test_prerequisito_verifica(prereq_str, taken_courses, expected):
    """
    Testa o método verifica para diferentes pré-requisitos e listas de disciplinas cursadas.
    """
    prereq = PreRequisito(prereq_str)
    assert prereq.Verifica(taken_courses) == expected, f"Falha para {prereq_str} com {taken_courses}"


@pytest.mark.parametrize("prereq_str", [
    "E",  # Operador 'E' sem operandos
    "OU",  # Operador 'OU' sem operandos
    "CTCO01 E",  # Operador 'E' no final
    "CTCO01 OU",  # Operador 'OU' no final
    "(CTCO01 OU STCO01 E CRSC04",  # Parênteses não balanceados
    "CTCO01 E (STCO01 OU CRSC04))",  # Parênteses não balanceados
    "CTCO01 E (STCO01 OU CRSC04) E",  # Operador 'E' no final
    "CTCO01 OU (STCO01 E CRSC04) OU",  # Operador 'OU' no final
])
def test_prerequisito_invalid_expression(prereq_str):
    """
    Testa a criação de pré-requisitos com expressões inválidas.
    """
    with pytest.raises(ValueError):
        PreRequisito(prereq_str)

@pytest.mark.parametrize("prereq_str,course,expected", [
    # Sem pré-requisito
    ("-", "", False),
    ("-", "XDES01", False),
    # Curso único
    ("XDES01", "", False),
    ("XDES01", "XDES01", True),
    ("XDES01", "OTHER", False),
    # Combinação OR
    ("CTCO01 OU STCO01", "", False),
    ("CTCO01 OU STCO01", "CTCO01", True),
    ("CTCO01 OU STCO01", "STCO01", True),
    ("CTCO01 OU STCO01", "OTHER", False),
    # Combinação com parênteses
    ("(CTCO01 OU STCO01) E CRSC04", "", False),
    ("(CTCO01 OU STCO01) E CRSC04", "CTCO01", True),
    ("(CTCO01 OU STCO01) E CRSC04", "STCO01", True),
    ("(CTCO01 OU STCO01) E CRSC04", "CRSC04", True),
    ("(CTCO01 OU STCO01) E CRSC04", "OTHER", False),
    # Expressão complexa
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", "MAT00A", True),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", "XMAC01", True),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", "CTCO01", True),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", "STCO01", True),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", "OTHER", False),
    ("MAT00A E XMAC01 E (CTCO01 OU STCO01)", "", False),
    # Múltiplos ANDs
    ("MAT00A E XMAC01 E CRSC04", "MAT00A", True),
    ("MAT00A E XMAC01 E CRSC04", "XMAC01", True),
    ("MAT00A E XMAC01 E CRSC04", "CRSC04", True),
    ("MAT00A E XMAC01 E CRSC04", "", False),
    ("MAT00A E XMAC01 E CRSC04", "OTHER", False),
    # Múltiplos ORs
    ("CTCO01 OU STCO01 OU CRSC04", "CTCO01", True),
    ("CTCO01 OU STCO01 OU CRSC04", "STCO01", True),
    ("CTCO01 OU STCO01 OU CRSC04", "CRSC04", True),
    ("CTCO01 OU STCO01 OU CRSC04", "", False),
    ("CTCO01 OU STCO01 OU CRSC04", "OTHER", False)
])
def test_prerequisito_contem(prereq_str, course, expected):
    """
    Testa o método contem para verificar se um curso específico está nos pré-requisitos.
    """
    prereq = PreRequisito(prereq_str)
    assert prereq.Contem(course) == expected, f"Falha para {prereq_str} com {course}. {prereq.pre_reqset}"
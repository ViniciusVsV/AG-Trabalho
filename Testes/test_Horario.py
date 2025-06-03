import pytest
from Objetos.Horario import Horario

def test_inicializacao_valida():
    h = Horario("2M3")
    assert str(h) == "2M3", "A representação em string deve ser '2M3'"

    h = Horario("2M34")
    assert str(h) == "2M34", "A representação em string deve ser '2M34'"

    h = Horario("23M1")
    assert str(h) == "23M1", "A representação em string deve ser '23M1'"

    h = Horario("2M1 3T2")
    assert str(h) == "2M1 3T2", "A representação em string deve ser '2M1 3T2'"

# Testes de inicialização com horários inválidos
@pytest.mark.parametrize("invalid_schedule", [
    "1M34",  # Dia inválido (1)
    "8M34",  # Dia inválido (8)
    "2X34",  # Turno inválido (X)
    "2M9",   # Período inválido (9)
    "2M",    # Período ausente
    "ABC",   # Formato inválido
    "",      # String vazia
    "   ",   # Apenas espaços
])
def test_inicializacao_invalida(invalid_schedule):
    with pytest.raises(ValueError, match="Horário inválido"):
        Horario(invalid_schedule)

# Testes de verificação de conflitos
@pytest.mark.parametrize("sched1, sched2, expected_conflict", [
    ("2M3", "2M3", True),           # Mesmo horário exato
    ("2M3", "2M4", False),          # Mesmo dia e turno, períodos diferentes
    ("2M3", "2T3", False),          # Mesmo dia e período, turno diferente
    ("2M3", "3M3", False),          # Mesmo turno e período, dia diferente
    ("2M34", "2M3", True),          # "2M34" inclui "2M3"
    ("2M12", "2M23", True),         # Sobreposição em "2M2"
    ("2M13", "2M4", False),         # Nenhum período em comum
    ("23M1", "2M1", True),          # "23M1" inclui "2M1"
    ("23M1", "3M1", True),          # "23M1" inclui "3M1"
    ("23M1", "4M1", False),         # Nenhum dia em comum
    ("2M1 3T2", "2M1 4N3", True),   # Conflito em "2M1"
    ("2M1 3T2", "5T4 6N1", False),  # Nenhum conflito
])
def test_conflito(sched1, sched2, expected_conflict):
    h1 = Horario(sched1)
    h2 = Horario(sched2)
    assert h1.isConflitante(h2) == expected_conflict, f"Conflito esperado: {expected_conflict} para {sched1} e {sched2}"

# Teste de tipo inválido no método isConflitante
def test_tipo_invalido():
    h1 = Horario("2M1")
    with pytest.raises(TypeError, match="O parâmetro deve ser do tipo Horario"):
        h1.isConflitante("invalido")
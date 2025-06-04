from ..Horario import Horario

class Turma:
    def __init__(self, nro_turma: int, horarios: str, peso: float = 0.0):
        self.nro_turma = nro_turma
        self.horarios = Horario(horarios)

        self.peso = peso

    def verificaHorarioConflitante(self, outro: 'Turma') -> bool:
        """
        Verifica se há conflito de horários entre duas turmas.

        Args:
            outro (Turma): Outra turma para comparar os horários.
        Returns:
            bool: True se houver conflito de horários, False caso contrário.
        """
        
        return self.horarios.isConflitante(outro.horarios)
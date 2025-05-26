from .Horario import Horario
from .PreRequisito import PreRequisito

class Vertice:
    def __init__(self, sigla: str, nome: str, categoria: str, semestre: int, anualidade: str, horarios: str, cargaHor: int, preReq: str):
        self.sigla = sigla
        self.nome = nome
        self.categoria = categoria
        self.semestre = semestre
        self.anualidade = anualidade == 'SIM'
        self.horarios = Horario(horarios)
        self.cargaHor = cargaHor
        self.preReq = PreRequisito(preReq)
        
        self.Peso: int = None

    
    def verificaHorarioConflitante(self, outro: 'Vertice') -> bool:
        """
        Verifica se há conflito de horários entre dois vértices.

        Args:
            outro (Vertice): Outro vértice para comparar os horários.
        Returns:
            bool: True se houver conflito de horários, False caso contrário.
        """
        
        return self.horarios.isConflitante(outro.horarios)

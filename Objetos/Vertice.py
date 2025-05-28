from .Horario import Horario
from .PreRequisito import PreRequisito

class Vertice:
    def __init__(self, sigla: str, nome: str, curso: str, categoria: str, semestre: int, anualidade: str, horarios: str, cargaHor: int, preReq: str):
        self.sigla = sigla
        self.nome = nome
        self.curso = curso
        self.categoria = categoria
        self.semestre = semestre
        self.anualidade = anualidade == 'SIM'
        self.horarios = Horario(horarios)
        self.cargaHor = cargaHor
        self.preReq = PreRequisito(preReq)
        
        self.Peso: int = 0


    def verificaHorarioConflitante(self, outro: 'Vertice') -> bool:
        """
        Verifica se há conflito de horários entre dois vértices.

        Args:
            outro (Vertice): Outro vértice para comparar os horários.
        Returns:
            bool: True se houver conflito de horários, False caso contrário.
        """
        
        return self.horarios.isConflitante(outro.horarios)

    def isPreRequisito(self, outro: 'Vertice') -> bool:
        """
        Verifica se o vértice atual é pré-requisito do outro vértice.

        Args:
            outro (Vertice): Outro vértice para verificar os pré-requisitos.
        Returns:
            bool: True se o pré-requisito for atendido, False caso contrário.
        """

        return self.preReq.contem(outro.sigla)
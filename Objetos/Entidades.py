from .PreRequisito import PreRequisito
from .Equivalente import Equivalente
from .Horario import Horario

class Disciplina:
    """
    Classe que representa uma disciplina em um curso.
    Atributos:
        sigla (str): Sigla da disciplina.
        nome (str): Nome da disciplina.
        curso (str): Curso ao qual a disciplina pertence.
        categoria (str): Categoria da disciplina (obrigatória, optativa, equivalente).
        periodo (int): Periodo do curso pretendido para a conclusão da disciplina.
        anualidade (bool): Indica se a disciplina é anual.
        cargaHoraria (int): Carga horária da disciplina.
        preRequisitos (PreRequisito): Pré-requisitos da disciplina.
        equivalentes (Equivalente): Disciplinas equivalentes. 
        correquisitos (set): Correquisitos da disciplina.
        peso (float): Peso da disciplina.
        turmas (list): Lista de turmas da disciplina.
    """
    def __init__(self, sigla: str, nome: str, curso: str, categoria: str, periodo: int, anualidade: str, cargaHoraria: int, preRequisitos: str = '-', equivalentes: str = '-', correquisitos: str = '-', peso: float = 0.0):
        self.sigla = sigla
        self.nome = nome
        self.curso = curso
        self.categoria = categoria
        self.periodo = periodo
        self.anualidade = anualidade == 'SIM'
        self.cargaHorario = cargaHoraria

        self.preRequisitos = PreRequisito(preRequisitos)
        self.equivalentes = Equivalente(equivalentes)
        self.correquisitos = set(corr.strip() for corr in correquisitos.split(',')) if correquisitos and correquisitos != '-' else set()
        
        self.peso = 0.0 if categoria == "OPTATIVA" else peso

        self.turmas: list[(int, str, int)] = []

    def AdicionaTurma(self, numeroTurma: int, horario: str, semestre: int, ):
        """
        Adiciona uma turma à disciplina.

        Args:
            numeroTurma (int): Número da turma a ser adicionada.
            horario (str): Horário da turma a ser adicionada.
            semestre (int): Semestre do ano em que a turma a ser adicionada é ofertada (1, 2).
        """
        self.turmas.append((numeroTurma, horario, semestre))

    def CriaTurmas(self) -> list['Turma']:
        """
        Cria uma lista de objetos Turma a partir das turmas da disciplina.

        Returns:
            list[Turma]: Lista de objetos Turma criados.
        """
        turmas = []

        for (numeroTurma, horario, semestre) in self.turmas:
            turmas.append(Turma(self, numeroTurma, horario, semestre, self.peso))
        
        return turmas

    def isPreRequisito(self, outro: 'Disciplina') -> bool:
        """
        Verifica se a outra disciplina é pré-requisito da disciplina atual.

        Args:
            outro (Disciplina): Outra disciplina para verificar os pré-requisitos.
        Returns:
            bool: True se o pré-requisito for atendido, False caso contrário.
        """

        return self.preRequisitos.Contem(outro.sigla)
    
    def VerificaPreRequisitos(self, disciplinasCumpridas: set[str]) -> bool:
        """
        Verifica se os pré-requisitos da disciplina foram atendidos.

        Args:
            disciplinasCumpridas (set[str]): Conjunto de disciplinas já cursadas.
        
        Returns:
            bool: True se os pré-requisitos foram atendidos, False caso contrário.
        """
        
        return self.preRequisitos.Verifica(disciplinasCumpridas)
    
    def VerificaEquivalencia(self, disciplinasEquivalentes: set[str]) -> bool:
        """
        Verifica se alguma equivalência da disciplina foi atendida.

        Args:
            disciplinasEquivalentes (set[str]): Conjunto de disciplinas equivalentes.
        
        Returns:
            bool: True se alguma equivalência foi atendida, False caso contrário.
        """
        
        return self.equivalentes.Verifica(disciplinasEquivalentes)

    def __eq__(self, value):
        if not isinstance(value, Disciplina):
            return False

        if self.sigla != value.sigla:
            return False

        if self.peso != value.peso:
            return False
        
    def __str__(self):
        return f"Disciplina(sigla={self.sigla}, nome={self.nome})"

class Turma:
    def __init__(self, disciplina: 'Disciplina', numeroTurma: int, horario: str, semestre: int, peso: float = 0.0):
        self.disciplina = disciplina

        self.numeroTurma = numeroTurma
        self.horario = Horario(horario)
        self.semestre = semestre

        self.peso = peso

    def VerificaHorarioConflitante(self, outro: 'Turma') -> bool:
        """
        Verifica se há conflito de horários entre duas turmas.

        Args:
            outro (Turma): Outra turma para comparar os horários.
        Returns:
            bool: True se houver conflito de horários, False caso contrário.
        """
        
        return self.horario.isConflitante(outro.horario)
    
    @property
    def sigla(self) -> str:
        """
        Retorna a sigla da disciplina associada à turma.

        Returns:
            str: Sigla da disciplina.
        """
        return self.disciplina.sigla

    # Só para garantir que a verificação de igualdade funcione corretamente
    # Estava dando problema por causa que comparada as referências de objetos
    # ao invés de seus valores
    def __eq__(self, value):
        if not isinstance(value, Turma):
            return False

        if self.codigo != value.codigo:
            return False

        if self.peso != value.peso:
            return False

    def __str__(self):
        return f"Turma(disciplina={self.disciplina.codigo}, nro_turma={self.nro_turma}, horarios={self.horarios})"
from ..PreRequisito import PreRequisito
from ..Equivalente import Equivalente
from ..Horario import Horario

class Disciplina:
    """
    Classe que representa uma disciplina em um curso.
    Atributos:
        sigla (str): Sigla da disciplina.
        nome (str): Nome da disciplina.
        curso (str): Curso ao qual a disciplina pertence.
        categoria (str): Categoria da disciplina (obrigatória, optativa, etc.).
        semestre (int): Semestre em que a disciplina é oferecida.
        anualidade (bool): Indica se a disciplina é anual.
        carga_horaria (int): Carga horária da disciplina.
        pre_requisitos (PreRequisito): Pré-requisitos da disciplina.
        equivalentes (Equivalente): Disciplinas equivalentes. 
        correquisitos (set): Conjunto de disciplinas que devem ser cursadas simultaneamente.
        peso (float): Peso da disciplina, usado para cálculo de média ponderada.
        turmas (list): Lista de horários das turmas disponíveis para a disciplina.
    """
    def __init__(self, sigla: str, nome: str, curso: str, categoria: str, semestre: int, anualidade: str, carga_horaria: int, pre_requisitos: str = '-', equivalentes: str = '-', correquisito: str = '-', peso: float = 0.0):
        self.sigla = sigla
        self.nome = nome
        self.curso = curso
        self.categoria = categoria
        self.semestre = semestre
        self.anualidade = anualidade == 'SIM'
        self.carga_horaria = carga_horaria
        self.pre_requisitos = PreRequisito(pre_requisitos)
        self.equivalentes = Equivalente(equivalentes)
        self.correquisitos = set(corr.strip() for corr in correquisito.split(',')) if correquisito and correquisito != '-' else set()
        self.peso = 0.0 if categoria == "OPTATIVA" else peso
        self.turmas: list[(int, str)] = []

    def adicionar_turma(self, horario: str, nro_turma: int):
        """
        Adiciona um horário de turma à disciplina.

        Args:
            horario (str): Horário da turma a ser adicionada.
            nro_turma (int): Número da turma a ser adicionada.
        """
        self.turmas.append((nro_turma, horario))

    def isPreRequisito(self, outro: 'Disciplina') -> bool:
        """
        Verifica se a outra disciplina é pré-requisito da disciplina atual.

        Args:
            outro (Disciplina): Outra disciplina para verificar os pré-requisitos.
        Returns:
            bool: True se o pré-requisito for atendido, False caso contrário.
        """

        return self.pre_requisitos.contem(outro.sigla)
    
    def atendePreRequisitos(self, disciplinasCumpridas: set[str]) -> bool:
        """
        Verifica se os pré-requisitos da disciplina foram atendidos.

        Args:
            disciplinasCumpridas (set[str]): Conjunto de disciplinas já cursadas.
        Returns:
            bool: True se os pré-requisitos foram atendidos, False caso contrário.
        """
        return self.pre_requisitos.verifica(disciplinasCumpridas)
    
    def criaTurmas(self) -> list['Turma']:
        """
        Cria uma lista de objetos Turma a partir dos horários da disciplina.

        Returns:
            list[Turma]: Lista de objetos Turma criados.
        """
        turmas = []
        for (nro_turma, horario) in self.turmas:
            turmas.append(Turma(self, nro_turma=nro_turma, horarios=horario, peso=self.peso))
        return turmas

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
    def __init__(self, disciplina: 'Disciplina', nro_turma: int, horarios: str, peso: float = 0.0):
        self.disciplina = disciplina
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
    
    @property
    def codigo(self) -> str:
        """
        Retorna o código da disciplina associada à turma.

        Returns:
            str: Código da disciplina.
        """
        return self.disciplina.codigo

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
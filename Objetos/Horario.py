import re

HORARIOS_REGEX = re.compile(r"(([2-7]+)([M|T|N])([1-5]+)\s?)+")

class Horario:
    def __init__(self, horario: str):
        self.__horario = horario

        if not self.__VerificaHorario():
            raise ValueError(f"Horário inválido. Deve estar no formato: /[2-7]+[M|T|N][1-5]+/. Recebido: {horario}")
        
        self.__setHorario = self.__ParseHorario()

    def __VerificaHorario(self) -> bool:
        """
        Verifica se o horário está no formato correto.

        O formato esperado é uma string contendo múltiplos horários separados por espaço,
        onde cada horário é composto por:
        - Um número de 2 a 7 representando o dia da semana (2 = segunda, 3 = terça, ..., 7 = sábado)
        - Uma letra representando o turno (M = manhã, T = tarde, N = noite)
        - Um número de 1 a 4 representando o período (1 = 1º período, 2 = 2º período, ..., 4 = 4º período)

        Returns:
            bool: True se o horário estiver no formato correto, False caso contrário.
        """

        return bool(HORARIOS_REGEX.fullmatch(self.__horario))
    
    def __ParseHorario(self) -> set[str]:
        """
        Converte o horário em um conjunto de strings representando cada horário individual.

        Returns:
            set[str]: Conjunto de horários individuais.
        """

        setHorarios = set()

        for horario in self.__horario.split():
            valor = HORARIOS_REGEX.split(horario)[2:-1]

            for dia in valor[0]:
                for turno in valor[2]:
                    setHorarios.add(f"{dia}{valor[1]}{turno}")

        return setHorarios
    
    def isConflitante(self, outro: 'Horario') -> bool:
        """
        Verifica se há conflito de horários entre dois objetos Horario.

        Args:
            outro (Horario): Outro objeto Horario para comparar os horários.

        Returns:
            bool: True se houver conflito de horários, False caso contrário.
        """

        if not isinstance(outro, Horario):
            raise TypeError("O parâmetro deve ser do tipo Horario.")

        return not self.__setHorario.isdisjoint(outro.__setHorario)

    def __str__(self) -> str:
        """
        Retorna uma representação em string do horário.

        Returns:
            str: String representando o horário.
        """
        return self.__horario
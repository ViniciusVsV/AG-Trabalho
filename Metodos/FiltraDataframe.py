import pandas as pd

def FiltraDataframe(dataframe, materiasRealizadas, periodoAtual, cursoDiscente):
    """
    Filtra o dataframe recebido, removendo todas as matérias obsoletas para o caso de uso.

    Retorna:
        Dataframe com as matérias pertinentes ao caso de uso.
    """

    dataframeFiltrado = dataframe[dataframe["CURSO"] == cursoDiscente]
    dataframeFiltrado = dataframeFiltrado[~dataframeFiltrado["SIGLA"].isin(materiasRealizadas)]
    dataframeFiltrado = dataframeFiltrado[dataframeFiltrado["PER."] % 2 == periodoAtual]

    print(dataframeFiltrado)

    return dataframeFiltrado


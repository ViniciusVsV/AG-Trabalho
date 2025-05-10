import pandas as pd

def ProcessaDataframe(dataframe, materiasRealizadas, periodoAtual):
    """
    Filtra o dataset recebido, removendo todas as matérias obsoletas para o caso de uso.
    
    Retorna:
        Array com as matérias pertinentes ao caso de uso.
    """
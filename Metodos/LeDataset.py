from Objetos import Disciplina
import pandas as pd

def leDataset(curso: str):
    '''
    Lê o dataset de disciplinas do curso especificado e retorna uma lista de objetos Disciplina.
    Args:
        curso (str): O curso para o qual as disciplinas serão lidas. Deve ser "CCO", "SIN" ou "ECO".
    Returns:
        list[Disciplina]: Lista de objetos Disciplina contendo as informações das disciplinas do curso.
    '''
    if curso not in ["CCO", "SIN", "ECO"]:
        raise ValueError("Curso inválido. Deve ser 'CCO', 'SIN' ou 'ECO'.")
    
    nPeriodos = (
        8 if curso == "CCO"
        else 9 if curso == "SIN"
        else 10
    )
    
    # Lê o dataset pertinente
    dataframe = pd.read_csv(
        "Datasets/Disciplinas" + curso + ".csv" ,
        na_values=[],
        keep_default_na=False
    )

    # Cria o array das disciplinas do curso e o popula a partir do dataset

    disciplinas: list[Disciplina] = []
    disciplinasProcessadas: dict[tuple[str, str], Disciplina] = dict()

    qtdTurmas = 0
    for index, row in dataframe.iterrows():
        if (row['SIGLA'], row['CAT']) in disciplinasProcessadas:
            # Se a disciplina já foi processada, apenas adiciona o horário
            disciplinasProcessadas[(row['SIGLA'], row['CAT'])].\
                adicionaTurma(qtdTurmas, row['HOR'], row['SEM'])
            
            qtdTurmas += 1
            continue

        disciplina = Disciplina(
            sigla           =   row['SIGLA'],
            nome            =   row['NOME'],
            curso           =   row['CURSO'],
            categoria       =   row['CAT'],
            periodo         =   row['PER'],
            anualidade      =   row['AN'],
            cargaHoraria    =   row['CH'],
            preRequisitos   =   row['REQ'],
            equivalentes    =   row['EQV'],
            correquisitos   =   row['COREQ'],

            peso            =   nPeriodos - row["PER"] + 1
        )

        disciplina.adicionaTurma(qtdTurmas, row['HOR'], row['SEM'])
        qtdTurmas += 1

        disciplinasProcessadas[(row['SIGLA'], row['CAT'])] = disciplina

        disciplinas.append(disciplina)

    return disciplinas
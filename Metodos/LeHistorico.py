from Objetos import Historico

def leHistorico(caminhoArquivo: str) -> tuple[str, set[str]]:
    """
    Lê o histório do discente em arquivo pdf para obter dados importantes
    Args:
        caminhoArquivo (str): Caminho para o diretório onde o arquivo está armazenado.
    
    Returns:
        str: Curso do discente
        set[str]: Siglas das disciplinas já cumpridas pelo aluno
    """

    historico = Historico(caminhoArquivo)

    return historico.curso, historico.disciplinasAprovadas
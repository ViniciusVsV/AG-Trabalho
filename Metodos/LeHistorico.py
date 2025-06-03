from Objetos.Historico import Historico

def LeHistorico(caminho_pdf):
    historico = Historico(caminho_pdf)

    return historico.curso, sorted(historico.disciplinas_aprovadas)

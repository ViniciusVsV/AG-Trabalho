class Vertice:
    def __init__(self, sigla, nome, categoria, semestre, anualidade, horarios, cargaHor, preReq):
        self.sigla = sigla
        self.nome = nome
        self.categoria = categoria
        self.semestre = semestre
        self.anualidade = anualidade
        self.horarios = horarios
        self.cargaHor = cargaHor
        self.preReq = preReq
        
        self.Peso = None
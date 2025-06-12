class Optativa:
    def __init__(self):
        self.optativasComputacao = set(["SDES05", "SDES06", "SDES07", "XDES08", "XDES10", "XDES11", "XDES12",
                                        "XDES14", "XDES16", "XDES17", "ECOX21", "ECOX22", "SPAD02", "SPAD03",
                                        "XPAD04", "XPAD08", "XPAD09", "XMCO02", "XMCO03", "XMCO04", "CMCO06",
                                        "CMCO07", "XMCO08", "XMCO09", "XRSC06", "XRSC07", "XRSC08", "XRSC09",
                                        "XRSC10", "ECOS04"])

        self.trilhasCCO = {
            0: set(),
            1: set(["XMCO04", "XMCO03", "CMCO06", "XDES08", "XMCO08", "CMCO07", "CRSC08", "XPAD04", "XRSC09", "XRSC07"]),
            2: set(["SDES05", "XDES08", "CDES13", "CMCO06", "SDES07", "XPADO09", "SPAD02", "SDES06", "XRSC09", "XRSC07"]),
            3: set(["SPAD03", "XPAD04", "CMCO06", "XMCO03", "XPAD09", "CRSC08", "XRSC06", "XAHC08", "XRSC09", "XRSC07"])
        }

        self.trilhasSIN = {
            0: set(),
            1: set(["XPAD04", "XRSC09", "SPAD05", "XMCO04", "SPAD06", "XMCO03", "SPAD07", "XRSC06", "SADG02"]),
            2: set(["XRSC09", "XRSC07", "XRSC06", "XRSC08", "CRSC05", "XPAD04", "XDES08", "SPAD07", "XMCO04"]),
            3: set(["XDES10", "XDES09", "XDES08", "XRSC06", "XPAD04", "XRSC09", "SPAD07", "XRSC08", "SADG02"])
        }

    def getTrilha(self, numeroTrilha : int, curso: str) -> set[str] | None:
        if curso == "CCO":      trilhas = self.trilhasCCO
        elif curso == "SIN":    trilhas = self.trilhasSIN
        else:
            print("Curso inválido")
            return None

        if numeroTrilha not in trilhas:     return None

        return trilhas[numeroTrilha]

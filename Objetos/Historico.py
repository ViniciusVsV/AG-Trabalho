import pymupdf as mu
import re

class Historico:
    def __init__(self, historico):
        self.historico = historico
        
        self.nome = None
        self.curso = None

        self.disciplinasAprovadas = set()

        self.leHistorico()

    def leHistorico(self):
        doc = mu.open(self.historico)
        lendo_disciplinas = False
        linha_atual = []

        for page in doc:
            texto_dict = page.get_text("dict")
            for bloco in texto_dict["blocks"]:
                if "lines" not in bloco:
                    continue
                for linha in bloco["lines"]:
                    texto_linha = " ".join(
                        span["text"].strip() for span in linha["spans"] if span["text"].strip()
                    )

                    if self.nome is None:
                        if texto_linha.startswith("Nome:"):
                            self.nome = texto_linha.split(":", 1)[1].strip()
                            continue

                    if self.curso is None:
                        linha = texto_linha
                    if "CIÊNCIA DA COMPUTAÇÃO" in linha:
                        self.curso = "CCO"
                    elif "SISTEMAS DE INFORMAÇÃO" in linha:
                        self.curso = "SIN"

                    if "Componentes Curriculares Cursados" in texto_linha:
                        lendo_disciplinas = True
                        continue
                    if "Componentes Curriculares Obrigatórios Pendentes" in texto_linha:
                        lendo_disciplinas = False
                        continue

                    if not lendo_disciplinas:
                        continue

                    if re.match(r"\d{4}\.\d|--", texto_linha):
                        if linha_atual:
                            registro = " ".join(linha_atual)
                            match = re.search(r'\b(APRN?|CUMP)\b', registro) or re.search(r'CUMP[A-Z]{3,4}[0-9]{2,3}[A-Z]?', registro)
                            if match:
                                sigla_match = re.search(r'\b([A-Z]{3,4}[0-9]{2,3}[A-Z]?)\b', registro)
                                if sigla_match:
                                    self.disciplinasAprovadas.add(sigla_match.group(1))
                        linha_atual = [texto_linha]
                    elif linha_atual:
                        linha_atual.append(texto_linha)

            # Processa a última linha se necessário. Revisar depois. Se tá funcionando, não mexe.
            if linha_atual:
                registro = " ".join(linha_atual)
                match = re.search(r'\b(APRN?|CUMP)\b', registro) or re.search(r'CUMP[A-Z]{3,4}[0-9]{2,3}[A-Z]?', registro)
                if match:
                    sigla_match = re.search(r'\b([A-Z]{3,4}[0-9]{2,3}[A-Z]?)\b', registro)
                    if sigla_match:
                        self.disciplinasAprovadas.add(sigla_match.group(1))
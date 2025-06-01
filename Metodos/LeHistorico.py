import pymupdf as mu
import re

def LeHistorico(historico):
    doc = mu.open(historico)
    disciplinas_aprovadas = set()
    linha_atual = []
    lendo_disciplinas = False
    curso = "NADA"

    for page in doc:
        texto_dict = page.get_text("dict")
        for bloco in texto_dict["blocks"]:
            if "lines" not in bloco:
                continue
            for linha in bloco["lines"]:
                texto_linha = " ".join(
                    span["text"].strip() for span in linha["spans"] if span["text"].strip()
                )

                if curso == "NADA":
                    linha = texto_linha
                    if "CIÊNCIA DA COMPUTAÇÃO" in linha:
                        curso = "CCO"
                    elif "SISTEMAS DE INFORMAÇÃO" in linha:
                        curso = "SIN"

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
                                disciplinas_aprovadas.add(sigla_match.group(1))
                    linha_atual = [texto_linha]
                elif linha_atual:
                    linha_atual.append(texto_linha)

    if linha_atual:
        registro = " ".join(linha_atual)
        match = re.search(r'\b(APRN?|CUMP)\b', registro) or re.search(r'CUMP[A-Z]{3,4}[0-9]{2,3}[A-Z]?', registro)
        if match:
            sigla_match = re.search(r'\b([A-Z]{3,4}[0-9]{2,3}[A-Z]?)\b', registro)
            if sigla_match:
                disciplinas_aprovadas.add(sigla_match.group(1))

    return curso, sorted(disciplinas_aprovadas)

if __name__ == '__main__':
    nameArq = input("Digite o nome do PDF: ")
    curso, aprovadas = LeHistorico(nameArq)
    
    print(curso)
    for sigla in aprovadas:
        print(sigla)

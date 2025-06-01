import pymupdf
import re

def LeHistorico(historico):
    doc = pymupdf.open(historico)
    disciplinas_aprovadas = []
    linha_atual = []

    for page in doc:
        texto_dict = page.get_text("dict")
        for bloco in texto_dict["blocks"]:
            if "lines" not in bloco:
                continue
            for linha in bloco["lines"]:
                texto_linha = " ".join(span["text"].strip() for span in linha["spans"] if span["text"].strip())
                if re.match(r"\d{4}\.\d", texto_linha):
                    if linha_atual:
                        registro = " ".join(linha_atual)
                        if re.search(r"\bAPR(N)?\b", registro):
                            partes = registro.split()
                            nome_index = partes.index('APR') if 'APR' in partes else partes.index('APRN')
                            nome_disciplina = " ".join(partes[1:nome_index])
                            disciplinas_aprovadas.append(nome_disciplina)      
                    linha_atual = [texto_linha]
                elif linha_atual:
                    linha_atual.append(texto_linha)
    if linha_atual:
        registro = " ".join(linha_atual)
        if re.search(r"\bAPR(N)?\b", registro):
            partes = registro.split()
            nome_index = partes.index('APR') if 'APR' in partes else partes.index('APRN')
            nome_disciplina = " ".join(partes[1:nome_index])
            disciplinas_aprovadas.append(nome_disciplina)

    disciplinas_aprovadas.pop()
    return disciplinas_aprovadas

if __name__ == '__main__':
    nomeArq = input("Digite o nome do PDF: ")
    aprovadas = LeHistorico(nomeArq)
    print("\nDisciplinas aprovadas:")
    for d in aprovadas:
        print(d)

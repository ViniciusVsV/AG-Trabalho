import pymupdf
def LeHistorico(historico):
    doc = pymupdf.open(historico) # open a document
    


if __name__ == '__main__':
    nameArq = input("Digite o nome do pdf:")
    LeHistorico(nameArq)
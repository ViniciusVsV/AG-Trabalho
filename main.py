import tabula

tables = tabula.read_pdf("historico1.pdf", pages="all")

print(tables)
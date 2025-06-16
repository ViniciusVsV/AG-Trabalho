from flask import Flask, request, render_template, jsonify
import os
import uuid
from Metodos import montaListaAdjDirigida, montaListaAdjSimples, calculaPesos, leHistorico, leDataset, filtraTurmas, calculaCIM
from Objetos import Historico

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# Criar a pasta de uploads se ela não existir
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado"})
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Nenhum arquivo selecionado"})
        if file and file.filename.endswith('.pdf'):
            # Gerar um nome de arquivo único
            filename = str(uuid.uuid4()) + '.pdf'
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # Salvar o arquivo na pasta de uploads
            file.save(file_path)
            try:
                historico = Historico(file_path)

                curso = request.form.get('curso')
                numeroTrilha = int(request.form.get('trilha'))
                semestre = int(request.form.get('semestre'))
                cargaHoraria = int(request.form.get('cargahoraria'))

                disciplinas = leDataset(curso)

                listaAdjDirigida = montaListaAdjDirigida(disciplinas)

                # Calcula os pesos das disciplinas

                disciplinas = calculaPesos(listaAdjDirigida, disciplinas, numeroTrilha, curso)

                # Filtra as disciplinas e obtém as turmas disponíveis

                turmasFiltradas = filtraTurmas(disciplinas, historico.disciplinasAprovadas, semestre)

                # Constrói o grafo de conflitos de horários

                listaAdjSimples = montaListaAdjSimples(turmasFiltradas)

                matriculas = calculaCIM((turmasFiltradas, listaAdjSimples), cargaHoraria)

                sugestoes = []

                for turma_set, peso in matriculas:
                    sugestao = {
                        "peso": peso,
                        "turmas": []
                    }

                    cargaHoraria = 0
                    for turma in turma_set:
                        cargaHoraria += turma.disciplina.cargaHoraria
                        sugestao["turmas"].append({
                            "sigla": turma.sigla,
                            "nome": turma.disciplina.nome,
                            "tipo": turma.disciplina.categoria,
                            "turma": turma.numeroTurma,
                            "horario": str(turma.horario)
                        })
                        
                    sugestao["cargaHoraria"] = cargaHoraria
                    sugestoes.append(sugestao)

                data = {
                    "nome": historico.nome,
                    "matricula": historico.matricula,
                    "horario_semestre": 40,
                    "sugestoes": sugestoes
                }
            finally:
                # Deletar o arquivo após o processamento
                if os.path.exists(file_path):
                    os.remove(file_path)
            return jsonify(data)
        else:
            return jsonify({"error": "Arquivo inválido"})
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
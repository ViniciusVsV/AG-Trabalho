from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'pdfs')
ALLOWED_EXTENSIONS = {'pdf'} 

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def processamentoPDF(nomeArquivo):
    return 

def processamento_grafos(pdf_caminho):
    return

@app.route('/api/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'Nenhum arquivo PDF encontrado na requisição poha.'}), 400

    pdf_file = request.files['pdf']

    if pdf_file.filename == '':
        return jsonify({'erro': 'Nome do arquivo PDF ta sem nada.'}), 400

    if pdf_file and allowed_file(pdf_file.filename):
        filename = secure_filename(pdf_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        pdf_file.save(filepath)

        area_selected = request.form.get('area', 'Não especificada')
        max_hours_str = request.form.get('max_hours')
        resposta_recomendacao = processamento_grafos()
        #coloque as funcoes de processamento de grafos

        '''POR FAVOR VALIDE QUE AS HORAS SAO INTEIRAS'''

        print(f"PDF recebido: {filename}")
        print(f"Área selecionada: {area_selected}")
        print(f"Caminho completo do arquivo salvo: {filepath}")

        """
            algoritmos de grafos aqui
        """

        resposta_data = {
            'message': 'Upload e processamento de grafo concluídos!',
            'pdf_name': filename,
            'area_selected': area_selected,
            'maximas_horas': max_hours_str,
            'file_url': f"/media/pdfs/{filename}",
            'resposta_recomendacao': resposta_recomendacao # <-- Aqui estão os resultados da recomendação
        }
        return jsonify(resposta_data), 200
    else:
        return jsonify({'error': 'Tipo de arquivo não permitido. Apenas PDFs são aceitos.'}), 400

@app.route('/media/pdfs/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
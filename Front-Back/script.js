document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const checkboxes = document.querySelectorAll('input[name="area"]');
    const resultDiv = document.getElementById('result');
    const pdfUploadInput = document.getElementById('pdfUpload');
    const recomendacaoResultados = document.getElementById('recomendacaoResultados');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            checkboxes.forEach(otherCheckbox => {
                if (otherCheckbox !== this) {
                    otherCheckbox.checked = false;
                }
            });
        });
    });

    uploadForm.addEventListener('submit', async function(event) {
        event.preventDefault();

        const selectedPdf = pdfUploadInput.files[0];
        const selectedAreas = Array.from(checkboxes)
                               .filter(checkbox => checkbox.checked)
                               .map(checkbox => checkbox.value);

        const maxHoursSelect = document.getElementById('maxHours');
        const maxHours = maxHoursSelect.value;

        if (!maxHours) {
            resultDiv.textContent = 'Por favor, selecione a quantidade de horas máximas.';
            resultDiv.style.color = 'red';
            return;
        }

        if (!selectedPdf) {
            resultDiv.textContent = 'Por favor, selecione um arquivo PDF.';
            resultDiv.style.color = 'red';
            return;
        }

        if (selectedAreas.length === 0) {
            resultDiv.textContent = 'Por favor, selecione uma área de interesse.';
            resultDiv.style.color = 'red';
            return;
        }

        const areaName = selectedAreas[0];

        const formData = new FormData();
        formData.append('pdf', selectedPdf);
        formData.append('area', areaName);
        formData.append('max_hours', maxHours);

        const uploadUrl = 'http://127.0.0.1:5000/api/upload-pdf';

        try {
            resultDiv.textContent = 'Enviando PDF e processando...';
            resultDiv.style.color = 'orange';
            recomendacaoResultados.innerHTML = '<h2>Resultados da Recomendação:</h2><p>Calma ai...</p>';

            const response = await fetch(uploadUrl, {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();

                resultDiv.textContent = `Upload e processamento realizados com sucesso! PDF: "${data.pdf_name}", Área: "${data.area_selected}".`;
                resultDiv.style.color = 'green';
                console.log('Resposta completa do Flask:', data);

                recomendacaoResultados.innerHTML = '<h2>Resultados da Recomendação:</h2>'; 

                if (data.resposta_recomendacao) {
                    const recomendacao = data.resposta_recomendacao;

                    const cursosTitle = document.createElement('h3');
                    cursosTitle.textContent = 'Cursos Sugeridos:';
                    recomendacaoResultados.appendChild(cursosTitle);

                    if (recomendacao.cursos_recomendados && recomendacao.cursos_recomendados.length > 0) {
                        const cursosList = document.createElement('ul');
                        recomendacao.cursos_recomendados.forEach(curso => {
                            const li = document.createElement('li');
                            li.textContent = `${curso.curso} (${curso.horas} horas)`;
                            cursosList.appendChild(li);
                        });
                        recomendacaoResultados.appendChild(cursosList);
                    } else {
                        const noCourses = document.createElement('p');
                        noCourses.textContent = 'Nenhum curso recomendado com base nos critérios fornecidos.';
                        recomendacaoResultados.appendChild(noCourses);
                    }



                } else {
                    const noRecData = document.createElement('p');
                    noRecData.textContent = 'Nenhum dado de recomendação retornado pelo servidor.';
                    recomendacaoResultados.appendChild(noRecData);
                }

                uploadForm.reset();
            } else {
                const errorData = await response.json();
                resultDiv.textContent = `Erro no upload: ${errorData.error || 'Erro desconhecido'}.`;
                resultDiv.style.color = 'red';
                console.error('Erro na resposta do Flask:', errorData);
            }
        } catch (error) {
            resultDiv.textContent = 'Ocorreu um erro de rede. Verifique sua conexão com o servidor.';
            resultDiv.style.color = 'red';
            console.error('Erro ao conectar com o backend:', error);
        }
    });
});
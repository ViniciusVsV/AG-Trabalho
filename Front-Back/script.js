document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const checkboxes = document.querySelectorAll('input[name="area"]');
    const resultDiv = document.getElementById('result');
    const pdfUploadInput = document.getElementById('pdfUpload');

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

      
        const uploadUrl = '/api/upload-pdf/'; 

        try {
            resultDiv.textContent = 'Enviando PDF... Aguarde.';
            resultDiv.style.color = 'orange';

            const response = await fetch(uploadUrl, {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                resultDiv.textContent = `Upload realizado com sucesso! PDF: "${data.pdf_name}", Área: "${data.area_selected}".`;
                resultDiv.style.color = 'green';
                console.log('Resposta do Django:', data);
                uploadForm.reset();
            } else {
                const errorData = await response.json();
                resultDiv.textContent = `Erro no upload: ${errorData.error || 'Erro desconhecido'}.`;
                resultDiv.style.color = 'red';
                console.error('Erro na resposta do Django:', errorData);
            }
        } catch (error) {
            resultDiv.textContent = 'Ocorreu um erro de rede. Verifique sua conexão ou o servidor.';
            resultDiv.style.color = 'red';
            console.error('Erro ao conectar com o backend:', error);
        }
    });
});
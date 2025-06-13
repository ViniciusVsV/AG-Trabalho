
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import os

@csrf_exempt
def upload_pdf_view(request):
    if request.method == 'POST':
        if 'pdf' in request.FILES and 'area' in request.POST:
            pdf_file = request.FILES['pdf']
            area_selected = request.POST['area']

            fs = FileSystemStorage()
            filename = fs.save(os.path.join('pdfs', pdf_file.name), pdf_file)
            uploaded_file_url = fs.url(filename)

            print(f"PDF recebido: {pdf_file.name}")
            print(f"Área selecionada: {area_selected}")
            print(f"URL do arquivo salvo: {uploaded_file_url}")

            return JsonResponse({
                'message': 'Upload realizado com sucesso!',
                'pdf_name': pdf_file.name,
                'area_selected': area_selected,
                'file_url': uploaded_file_url
            }, status=200)
        else:
            return JsonResponse({'error': 'Arquivo PDF ou área de interesse não fornecidos.'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido. Use POST.'}, status=405)
from django.shortcuts import render


# Create your views here.


def extract_pdf_view(request):
    return render(request, 'extract_pdf.html')

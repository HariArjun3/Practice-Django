from django.urls import path
from . import views

urlpatterns = [
    path('', views.extract_pdf_view, name='pdfextractor'),
    # path('extracted-text/', views.extracted_text_view, name='extracted_text'),
]
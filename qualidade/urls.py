# qualidade/urls.py
from django.urls import path
from . import views # Importa 'views' do app 'qualidade'

urlpatterns = [
    path('analise/', views.analisar_compressor, name='analise_compressor'),
]
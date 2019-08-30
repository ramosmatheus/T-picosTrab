# módulo do Django para criar urls
from django.urls import path

# Importe todas suas classes do views.py
from .views import *

urlpatterns = [
    # path('caminho/da/url', ClasseLáDoView.as_view(), name="nomeDessaURL" )
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('curriculum/', CurriculumView.as_view(), name="curriculum"),

    ############################### CADASTRAR ####################################

    path('cadastrar/pessoa/', PessoaCreate.as_view(), name="cadastrar-pessoa"),
    path('cadastrar/setor/', SetorCreate.as_view(), name="cadastrar-setor"),
    path('cadastrar/viajem/', ViajemCreate.as_view(), name="cadastrar-viajem"),
    path('cadastrar/veiculo/', VeiculoCreate.as_view(), name="cadastrar-veiculo"),
    path('cadastrar/passagem/', PassagemCreate.as_view(), name="cadastrar-passagem"),
    path('cadastrar/servidor/', ServidorCreate.as_view(), name="cadastrar-servidor"),
    path('cadastrar/motorista/', MotoristaCreate.as_view(), name="cadastrar-motorista"),

    ############################### ALTERAR ####################################

    path('alterar/pessoa/<int:pk>/', PessoaCreateUpdate.as_view(), name="alterar-pessoa"),
    path('alterar/setor/<int:pk>/', SetorCreateUpdate.as_view(), name="alterar-setor"),
    path('alterar/viajem/<int:pk>/', ViajemCreateUpdate.as_view(), name="alterar-viajem"),
    path('alterar/veiculo/<int:pk>/', VeiculoCreateUpdate.as_view(), name="alterar-veiculo"),
    path('alterar/passagem/<int:pk>/', PassagemCreateUpdate.as_view(), name="alterar-passagem"),
    path('alterar/servidor/<int:pk>/', ServidorCreateUpdate.as_view(), name="alterar-servidor"),
    path('alterar/motorista/<int:pk>/', MotoristaCreateUpdate.as_view(), name="alterar-motorista"),

    ############################### DELETAR ####################################

    path('delete/pessoa/<int:pk>/', PessoaDelete.as_view(), name="delete-pessoa"),
    path('delete/setor/<int:pk>/', SetorDelete.as_view(), name="delete-setor"),
    path('delete/viajem/<int:pk>/', ViajemDelete.as_view(), name="delete-viajem"),
    path('delete/veiculo/<int:pk>/', VeiculoDelete.as_view(), name="delete-veiculo"),
    path('delete/passagem/<int:pk>/', PassagemDelete.as_view(), name="delete-passagem"),
    path('delete/servidor/<int:pk>/', ServidorDelete.as_view(), name="delete-servidor"),
    path('delete/motorista/<int:pk>/', MotoristaDelete.as_view(), name="delete-motorista"),

    ############################### LISTAR ####################################

    path('listar/pessoa/', PessoaList.as_view(), name="listar-pessoa"),
    path('listar/setor/', SetorList.as_view(), name="listar-setor"),
    path('listar/viajem/', ViagemList.as_view(), name="listar-viajem"),
    path('listar/veiculo/', VeiculoList.as_view(), name="listar-veiculo"),
    path('listar/passagem/', PassagemList.as_view(), name="listar-passagem"),
    path('listar/servidor/', ServidorList.as_view(), name="listar-servidor"),
    path('listar/motorista/', MotoristaList.as_view(), name="listar-motorista"),
]

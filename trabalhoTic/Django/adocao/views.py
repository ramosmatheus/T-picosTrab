from django.shortcuts import render
# Importa todas as classes do models.py
from .models import *
# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy
# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView
# Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView
# Importa o Mixin para obrigar login
from django.contrib.auth.mixins import LoginRequiredMixin
# Método que busca um objeto. Se não existir, da um erro 404
from django.shortcuts import get_object_or_404

from braces.views import GroupRequiredMixin


# Create your views here.

# Cria uma classe com herança de TemplateView para exibir
# um arquivo HTML normal (com o conteúdo dele)


class PaginaInicialView(TemplateView):
    template_name = "adocao/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PaginaInicialView, self).get_context_data(
            *args, **kwargs)
        context['ultimos_animais'] = "Aqui vai a lista de animais"

        return context

# Página "Sobre"


class SobreView(TemplateView):
    template_name = "adocao/sobre.html"

# Página de contato


class CurriculumView(TemplateView):
    template_name = "adocao/curriculum.html"


class ContatoView(TemplateView):
    template_name = "adocao/contato.html"


##################### INSERIR ######################

class PessoaCreate(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    model = Pessoa
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-pessoa")
    fields = ['nome', 'cargo', 'email', 'telefone', 'tipoUsuario']
    group_required = [u"Administrador"] 

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de nova Pessoa"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context


class SetorCreate(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    model = Setor
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-setor")
    fields = ['nome', 'diretor']
    group_required = [u"Administrador"]

    def get_context_data(self, *args, **kwargs):
        context = super(SetorCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar novo Setor"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context


class ViajemCreate(LoginRequiredMixin, CreateView):
    model = Viajem
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-viajem")
    fields = ['solicitante', 'nomePassageiros', 'quantidadePassageiros',
              'finalidade', 'roteiro', 'dataPartida', 'dataRetorno']
    group_required = [u"Administrador"]

    def get_context_data(self, *args, **kwargs):
        context = super(ViajemCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de nova Viajem"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context


class VeiculoCreate(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    model = Veiculo
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-veiculo")
    fields = ['categoria', 'marca', 'modelo', 'ano', 'quilometragem', 'placa']
    group_required = [u"Administrador"]

    def get_context_data(self, *args, **kwargs):
        context = super(VeiculoCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novo Veiculo"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url


class PassagemCreate(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    model = PassagemAviao
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-passagem")
    fields = ['companhiaAereaPartida', 'numVooPartida',
              'companhiaAereaChegada', 'numVooChegada', 'horaPartida', 'horaChegada']
    group_required = [u"Administrador"]

    def get_context_data(self, *args, **kwargs):
        context = super(PassagemCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de nova Passagem"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context


class ServidorCreate(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    model = Servidor
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-servidor")
    fields = ['Siape']
    group_required = [u"Administrador"]

    def get_context_data(self, *args, **kwargs):
        context = super(ServidorCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novo Servidor"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context


class MotoristaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Motorista
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-motorista")
    fields = ['cnh', 'validade']
    group_required = [u"Administrador"]

    def get_context_data(self, *args, **kwargs):
        context = super(MotoristaCreate, self).get_context_data(
            *args, **kwargs)
        context['titulo'] = "Cadastro de novo Motorista"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        return context

############################ ALTERAR ####################################


class PessoaCreateUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-pessoa")
    fields = ['nome', 'cargo', 'email', 'telefone', 'tipoUsuario']

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaCreateUpdate, self).get_context_data(
            *args, **kwargs)
        context['titulo'] = "AlterarPessoa"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-primary"

        return context


class SetorCreateUpdate(LoginRequiredMixin, UpdateView):
    model = Setor
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-setor")
    fields = ['nome', 'diretor']

    def get_context_data(self, *args, **kwargs):
        context = super(SetorCreateUpdate, self).get_context_data(
            *args, **kwargs)
        context['titulo'] = "Alterar novo Setor"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-primary"

        return context


class ViajemCreateUpdate(LoginRequiredMixin, UpdateView):
    model = Viajem
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-viajem")
    fields = ['solicitante', 'nomePassageiros', 'quantidadePassageiros',
              'finalidade', 'roteiro', 'dataPartida', 'dataRetorno']

    def get_context_data(self, *args, **kwargs):
        context = super(ViajemCreateUpdate, self).get_context_data(
            *args, **kwargs)
        context['titulo'] = "Alterar Viajem"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-primary"

        return context


class VeiculoCreateUpdate(LoginRequiredMixin, UpdateView):
    model = Veiculo
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-veiculo")
    fields = ['categoria', 'marca', 'modelo', 'ano', 'quilometragem', 'placa']

    def get_context_data(self, *args, **kwargs):
        context = super(VeiculoCreateUpdate,
                        self).get_context_data(*args, **kwargs)
        context['titulo'] = "Alterar Veiculo"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-primary"

        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Veiculo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object



class PassagemCreateUpdate(LoginRequiredMixin, UpdateView):
    model = PassagemAviao
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-passagem")
    fields = ['companhiaAereaPartida', 'numVooPartida',
              'companhiaAereaChegada', 'numVooChegada', 'horaPartida', 'horaChegada']

    def get_context_data(self, *args, **kwargs):
        context = super(PassagemCreateUpdate,
                        self).get_context_data(*args, **kwargs)
        context['titulo'] = "Alterar Passagem"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-primary"

        return context


class ServidorCreateUpdate(LoginRequiredMixin, UpdateView):
    model = Servidor
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-servidor")
    fields = ['Siape']

    def get_context_data(self, *args, **kwargs):
        context = super(ServidorCreateUpdate,
                        self).get_context_data(*args, **kwargs)
        context['titulo'] = "Alterar Servidor"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-primary"

        return context


class MotoristaCreateUpdate(LoginRequiredMixin, UpdateView):
    model = Motorista
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-motorista")
    fields = ['cnh', 'validade']

    def get_context_data(self, *args, **kwargs):
        context = super(MotoristaCreateUpdate,
                        self).get_context_data(*args, **kwargs)
        context['titulo'] = "Alterar Motorista"
        context['botao'] = "Alterar"
        context['classeBotao'] = "btn-primary"

        return context

############################# LISTARS ##################################


class PessoaList(LoginRequiredMixin, ListView):
    model = Pessoa
    template_name = "adocao/listas/list_pessoa.html"


class SetorList(LoginRequiredMixin, ListView):
    model = Setor
    template_name = "adocao/listas/list_setor.html"


class ViagemList(LoginRequiredMixin, ListView):
    model = Viajem
    template_name = "adocao/listas/list_viajem.html"


class VeiculoList(LoginRequiredMixin, ListView):
    model = Veiculo
    template_name = "adocao/listas/list_veiculo.html"
    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView
        self.object_list = Veiculo.objects.filter(usuario=self.request.user)
        return self.object_list



class PassagemList(LoginRequiredMixin, ListView):
    model = PassagemAviao
    template_name = "adocao/listas/list_passagem.html"


class ServidorList(LoginRequiredMixin, ListView):
    model = Servidor
    template_name = "adocao/listas/list_servidor.html"


class MotoristaList(LoginRequiredMixin, ListView):
    model = Motorista
    template_name = "adocao/listas/list_motorista.html"


############################# EXCLUIR ##################################

class PessoaDelete(LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-pessoa")

    def get_context_data(self, *args, **kwargs):
        context = super(PessoaDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class SetorDelete(LoginRequiredMixin, DeleteView):
    model = Setor
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-setor")

    def get_context_data(self, *args, **kwargs):
        context = super(SetorDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class ViajemDelete(LoginRequiredMixin, DeleteView):
    model = Viajem
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-viajem")

    def get_context_data(self, *args, **kwargs):
        context = super(ViajemDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class VeiculoDelete(LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-veiculo")

    def get_context_data(self, *args, **kwargs):
        context = super(VeiculoDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Veiculo, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object



class PassagemDelete(LoginRequiredMixin, DeleteView):
    model = PassagemAviao
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-passagem")

    def get_context_data(self, *args, **kwargs):
        context = super(PassagemDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class ServidorDelete(LoginRequiredMixin, DeleteView):
    model = Servidor
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-servidor")

    def get_context_data(self, *args, **kwargs):
        context = super(ServidorDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class MotoristaDelete(LoginRequiredMixin, DeleteView):
    model = Motorista
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-motorista")

    def get_context_data(self, *args, **kwargs):
        context = super(MotoristaDelete, self).get_context_data(
            *args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

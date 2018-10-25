from django.shortcuts import render
from .models import Membro
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import MembroForm


class MembroList(LoginRequiredMixin, ListView):
    model = Membro

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class MembroDetail(LoginRequiredMixin, DetailView):
    model = Membro


class MembroCreate(LoginRequiredMixin, CreateView):
    model = Membro
    fields = ['codigo', 'nome', 'apelido', 'data_nascimento', 'cpf', 'rg', 'cnpj', 'ie', 'telefone', 'celular',
              'email', 'site', 'endereco', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado']
    success_url = '/membros/membro_list'



class MembroUpdate(LoginRequiredMixin, UpdateView):
    model = Membro
    fields = ['codigo', 'nome', 'apelido', 'data_nascimento', 'cpf', 'rg', 'cnpj', 'ie', 'telefone', 'celular',
              'email', 'site', 'endereco', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado']
    success_url = reverse_lazy('membro_list_cbv')


class MembroDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('membro.deletar_clientes',)

    model = Membro
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('membro_list_cbv')
# Create your views here.

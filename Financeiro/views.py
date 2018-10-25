from django.shortcuts import render
from .models import Entrada, Saida, Categoria
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class EntradaList(LoginRequiredMixin, ListView):
    model = Entrada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EntradaDetail(LoginRequiredMixin, DetailView):
    model = Entrada

class EntradaCreate(LoginRequiredMixin, CreateView):
    model = Entrada
    fields = ['entrada_cliente', 'data_da_compra', 'valor_total', 'categoria']
    success_url = '/entrada/entrada_list'

class EntradaUpdate(LoginRequiredMixin, UpdateView):
    model = Entrada
    fields = ['entrada_cliente', 'data_da_compra', 'valor_total', 'categoria']
    success_url = reverse_lazy('entrada_list_cbv')

class EntradaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('entrada.deletar_entrada',)
    model = Entrada
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('entrada_list_cbv')

# Saída
class SaidaList(LoginRequiredMixin, ListView):
    model = Saida

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SaidaDetail(LoginRequiredMixin, DetailView):
    model = Saida

class SaidaCreate(LoginRequiredMixin, CreateView):
    model = Saida
    fields = ['saida_cliente', 'data_da_compra', 'valor_total', 'categoria']
    success_url = '/saida/saida_list'

class SaidaUpdate(LoginRequiredMixin, UpdateView):
    model = Saida
    fields = ['saida_cliente', 'data_da_compra', 'valor_total', 'categoria']
    success_url = reverse_lazy('saida_list_cbv')

class SaidaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('saida.deletar_saida',)
    model = Saida
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('saida_list_cbv')

# Categoria
class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoriaDetail(LoginRequiredMixin, DetailView):
    model = Categoria

class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['descricao_categoria']
    success_url = '/entrada/categoria_list'

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ['descricaocategoria']
    success_url = reverse_lazy('categoria_list_cbv')

class CategoriaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('categoria.deletar_categoria',)
    model = Categoria
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('categoria_list_cbv')

# Create your views here.


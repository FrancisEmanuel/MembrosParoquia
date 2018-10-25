from django.db import models
from Membros.models import Membro
from django.db.models import Sum

#=====CONTA============
'''class TipoConta(models.Model):
    tipo = models.CharField(max_length=50, verbose_name="Tipo da Conta")# Crédio ou Débito
    descricao_tipo_conta = models.TextField(null=False, blank=False, verbose_name="Descrição")

    def __str__(self):
        return self.tipo'''

class Conta(models.Model):
    nome_conta = models.CharField(max_length=150, verbose_name="Nome da Conta")
    descricao_tipo_conta = models.TextField(null=False, blank=False, verbose_name="Descrição")
    conta_ativa = models.NullBooleanField(null=False, blank=False, default=True, verbose_name="Ativa")
    saldo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Saldo Caixa")

    def __str__(self):
        return self.nome_conta

#=====ENTRADA=============
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100, verbose_name="Categoria")
    entrada_ou_saida = models.CharField(max_length=100, verbose_name="Entrada ou Saída")
    descricao_categoria = models.TextField(null=False, blank=False, verbose_name="Descrição")

    def __str__(self):
        return self.descricao_categoria

class Entrada(models.Model):
    entrada_cliente = models.ForeignKey(Membro, on_delete=models.CASCADE, verbose_name="Cliente")
    conta_usada = models.ForeignKey(Conta, on_delete=models.CASCADE, verbose_name="Conta")
    data_da_entrada = models.DateField(verbose_name="Data de Entrada")
    valor_total = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Valor Total")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria da Entrada")

    def credito_caixa(self):
        self.conta_usada.saldo = self.conta_usada.saldo + self.valor_total
        return self.conta_usada.save()

#=======SAÍDA============

class Saida(models.Model):
    cliente_sainda = models.ForeignKey(Membro, on_delete=models.CASCADE, verbose_name="Cliente")
    conta_usada = models.ForeignKey(Conta, on_delete=models.CASCADE, verbose_name="Conta")
    data_da_saida = models.DateField(verbose_name="Data de Saída")
    valor_total = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Valor Total")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria de Saída")

    def debito_caixa(self):
        self.conta_usada.saldo = self.conta_usada.saldo - self.valor_total
        return self.conta_usada.save()


def saldo_data(data_inicio, data_fim):
    total_entrada = Entrada.objects.filter(data_da_entrada__gte=data_inicio, data_da_saida__lte=data_fim).aggregate(Sum('valor_total'))
    total_saida = Saida.objects.filter(data_da_entrada__gte=data_inicio, data_da_saida__lte=data_fim).aggregate(Sum('valor_total'))
    total = total_entrada - total_saida

'''
#=======SALDO============
class Saldo(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, verbose_name="Conta")
    entradas = models.ForeignKey(Entrada, on_delete=models.CASCADE, verbose_name="Entrada")
    saidas = models.ForeignKey(Saida, on_delete=models.CASCADE, verbose_name="Saida")
    data_minima = models.DateField(verbose_name="Data Minima")
    data_maxima = models.DateField(verbose_name="Data Maxima")
    soma = 0

    def saldo(self)
        soma += Saida.get_saida_cliente()
        return self.entradas - self.saidas
'''
# Create your models here.

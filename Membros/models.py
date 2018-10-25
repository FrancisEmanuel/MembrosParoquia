from django.db import models


class Membro(models.Model):
    codigo = models.IntegerField(unique=True, null=False, blank=False, verbose_name="Código de Acesso")
    nome = models.CharField(max_length=150, verbose_name="Nome")                               #Obrigatório
    apelido = models.CharField(max_length=150, null=False, blank=False, verbose_name="Apelido")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name="CPF")
    rg = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name="RG")
    cnpj = models.CharField(max_length=40,unique=True, null=False, blank=False, verbose_name="CNPJ")
    ie = models.CharField(max_length=20, null=False, blank=False, verbose_name="IE")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")                        #Obrigatório
    celular = models.CharField(max_length=20, null=False, blank=False, verbose_name="Celular")
    email = models.EmailField(max_length=40, null=False, blank=False, verbose_name="Email")
    site = models.CharField(max_length=50, null=False, blank=False, verbose_name="Site")
    endereco = models.CharField(max_length=100, null=False, blank=False, verbose_name="Endereço")
    numero = models.CharField(max_length=6, null=False, blank=False, verbose_name="Nº")
    complemento = models.CharField(max_length=40, null=False, blank=False, verbose_name="Complemento")
    bairro = models.CharField(max_length=40, null=False, blank=False, verbose_name="Bairro")
    cep = models.CharField(max_length=40, null=False, blank=False, verbose_name="CEP")
    cidade = models.CharField(max_length=40, null=False, blank=False, verbose_name="Cidade")
    estado = models.CharField(max_length=40, null=False, blank=False, verbose_name="Estado")

    def __str__(self):
        return self.nome


# Create your models here.

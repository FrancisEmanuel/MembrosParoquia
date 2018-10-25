from django.forms import ModelForm
from .models import Membro


class MembroForm(ModelForm):
    class Meta:
        model = Membro
        fields = ['codigo', 'nome', 'data_nascimento', 'telefone', 'celular',
                  'email', 'endereco', 'numero', 'bairro', 'cidade', 'estado']
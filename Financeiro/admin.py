from django.contrib import admin
from .models import Conta, Categoria, Entrada

admin.site.register(Conta)
admin.site.register(Categoria)
admin.site.register(Entrada)
# Register your models here.

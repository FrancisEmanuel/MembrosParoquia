# Generated by Django 2.0.7 on 2018-08-02 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Membros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaEntrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=100, verbose_name='Categoria da Entrada')),
                ('descricao_categoria', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaSaida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=100, verbose_name='Categoria de Saída')),
                ('descricao_categoria', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_conta', models.CharField(max_length=150, verbose_name='Nome da Conta')),
                ('descricao_tipo_conta', models.TextField(verbose_name='Descrição')),
                ('conta_ativa', models.NullBooleanField(default=True, verbose_name='Ativa')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Saldo Caixa')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_compra', models.DateField(verbose_name='Data de Entrada')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor Total')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financeiro.CategoriaEntrada', verbose_name='Categoria da Entrada')),
                ('conta_usada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financeiro.Conta', verbose_name='Conta')),
                ('entrada_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Membros.Membro', verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_saida', models.DateField(verbose_name='Data de Saída')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor Total')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financeiro.CategoriaSaida', verbose_name='Categoria de Saída')),
                ('cliente_sainda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Membros.Membro', verbose_name='Cliente')),
                ('conta_usada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financeiro.Conta', verbose_name='Conta')),
            ],
        ),
    ]
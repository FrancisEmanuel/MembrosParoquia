# Generated by Django 2.0.7 on 2018-08-07 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Financeiro', '0002_auto_20180802_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=100, verbose_name='Categoria')),
                ('entrada_ou_saida', models.CharField(max_length=100, verbose_name='Entrada ou Saída')),
                ('descricao_categoria', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.AlterField(
            model_name='entrada',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financeiro.Categoria', verbose_name='Categoria da Entrada'),
        ),
        migrations.AlterField(
            model_name='saida',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financeiro.Categoria', verbose_name='Categoria de Saída'),
        ),
        migrations.DeleteModel(
            name='CategoriaEntrada',
        ),
        migrations.DeleteModel(
            name='CategoriaSaida',
        ),
    ]

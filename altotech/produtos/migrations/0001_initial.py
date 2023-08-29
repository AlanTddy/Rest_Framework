# Generated by Django 4.2.4 on 2023-08-24 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=155)),
                ('cidade', models.CharField(max_length=155)),
                ('rua', models.CharField(max_length=155)),
                ('numero', models.CharField(max_length=15)),
                ('complemento', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nome', models.CharField()),
                ('descricao', models.TextField()),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='estoque', to='produtos.item')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nasc', models.DateField()),
                ('endereco', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='produtos.endereco')),
            ],
        ),
    ]

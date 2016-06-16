# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-16 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=45)),
                ('email', models.EmailField(default='', max_length=45)),
                ('endereco', models.CharField(default='', max_length=45)),
                ('telefone', models.CharField(default='', max_length=20)),
                ('CNPJ', models.CharField(default='', max_length=45)),
                ('isNew', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=256)),
                ('logradouro', models.CharField(default='', max_length=45)),
                ('numero', models.CharField(default='', max_length=4)),
                ('complemento', models.CharField(blank=True, max_length=45, null=True)),
                ('municipio', models.CharField(default='', max_length=45)),
                ('estado', models.CharField(default='', max_length=2)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataPedido', models.DateField()),
                ('prioridade', models.CharField(max_length=10)),
                ('status', models.CharField(default='pendente', max_length=45)),
                ('dataEntrega', models.DateField(blank=True, null=True)),
                ('qtd_tentativas', models.IntegerField()),
                ('codigoRastreamento', models.CharField(default='', max_length=8)),
                ('preco', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Cliente')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Destinatario')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('nome', models.CharField(max_length=45)),
                ('dataNascimento', models.DateField()),
                ('CPF', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('salario', models.FloatField()),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assinatura', models.CharField(max_length=45)),
                ('dataRecebimento', models.DateField()),
            ],
            options={
                'ordering': ['dataRecebimento'],
            },
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('precoBase', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Regioes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('tipoUsuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(default='', max_length=45)),
                ('modelo', models.CharField(default='', max_length=45)),
                ('ano', models.CharField(default='0000', max_length=4)),
                ('placa', models.CharField(default='AAA-0000', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Entregador',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.Funcionario')),
                ('status', models.IntegerField(default=0)),
                ('veiculos', models.ManyToManyField(related_name='entregadores', to='home.Veiculo', verbose_name='Veiculos que esta autorizado a usar')),
            ],
            options={
                'verbose_name_plural': 'Entregadores',
            },
            bases=('home.funcionario',),
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.Funcionario')),
            ],
            bases=('home.funcionario',),
        ),
        migrations.AddField(
            model_name='entrega',
            name='recibo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Recibo'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='regiao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Regiao'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='entregador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Entregador'),
        ),
    ]

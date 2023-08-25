# Generated by Django 4.2.4 on 2023-08-24 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUnidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
            options={
                'db_table': 'tb_tipos_unidade',
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('disponivel', models.BooleanField()),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('tipo_unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.tipounidade')),
            ],
            options={
                'db_table': 'tb_unidades',
            },
        ),
    ]
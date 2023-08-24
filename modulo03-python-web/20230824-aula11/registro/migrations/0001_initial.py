# Generated by Django 4.2.4 on 2023-08-18 23:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300, verbose_name='E-mail')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('valido', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tb_pre_registro',
            },
        ),
    ]

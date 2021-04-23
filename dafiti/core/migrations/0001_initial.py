# Generated by Django 3.2 on 2021-04-23 17:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='última atualização')),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('sku', models.CharField(blank=True, max_length=15, verbose_name='SKU')),
                ('descricao', models.TextField(null=True, verbose_name='Descrição')),
                ('quantidade', models.PositiveIntegerField(default=0, verbose_name='Quantidade estoque')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('tipo', models.CharField(choices=[('normal', 'Normal'), ('grade', 'Grade')], default='normal', max_length=50, verbose_name='Tipo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
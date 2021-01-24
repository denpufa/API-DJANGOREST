# Generated by Django 3.1.5 on 2021-01-22 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('comentarios', '0001_initial'),
        ('endereco', '0001_initial'),
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontosTuristicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('aprovado', models.BooleanField(default=False)),
                ('Avaliacoes', models.ManyToManyField(to='avaliacoes.Avaliacao')),
                ('atracoes', models.ManyToManyField(to='atracoes.Atracoes')),
                ('comentarios', models.ManyToManyField(to='comentarios.Comentario')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco')),
            ],
        ),
    ]
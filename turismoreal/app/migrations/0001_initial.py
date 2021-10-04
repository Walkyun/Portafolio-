# Generated by Django 3.2.7 on 2021-09-26 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUbicacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Depto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descipcion', models.TextField()),
                ('disponible', models.BooleanField()),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.ubicacion')),
            ],
        ),
    ]
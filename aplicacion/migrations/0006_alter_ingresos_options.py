# Generated by Django 3.2.15 on 2022-10-26 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_alter_gastos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingresos',
            options={'ordering': ['fecha_cobro']},
        ),
    ]

# Generated by Django 3.2.15 on 2022-10-26 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_ingresos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gastos',
            options={'ordering': ['fecha_cobro']},
        ),
    ]
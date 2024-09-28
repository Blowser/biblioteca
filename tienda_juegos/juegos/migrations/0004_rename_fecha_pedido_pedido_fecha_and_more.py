# Generated by Django 5.1.1 on 2024-09-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0003_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='fecha_pedido',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
    ]

# Generated by Django 3.2.8 on 2022-05-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_auto_20220509_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fechaNac',
            field=models.DateField(blank=True, null=True, verbose_name='FechaNac'),
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataComprension', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivos',
            name='rendimiento_t_ha',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]

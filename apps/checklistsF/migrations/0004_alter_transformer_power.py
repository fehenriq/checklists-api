# Generated by Django 4.2.4 on 2024-06-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklistsF', '0003_transformer_demand_transformer_impedance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transformer',
            name='power',
            field=models.FloatField(verbose_name='Transformer Power'),
        ),
    ]

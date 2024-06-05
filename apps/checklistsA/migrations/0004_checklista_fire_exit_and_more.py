# Generated by Django 4.2.4 on 2024-06-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklistsA', '0003_alter_checklista_cable_side'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklista',
            name='fire_exit',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Transformer Fire Exit'),
        ),
        migrations.AddField(
            model_name='checklista',
            name='fire_transformer_demand',
            field=models.FloatField(blank=True, null=True, verbose_name='Fire Transformer Demand'),
        ),
        migrations.AddField(
            model_name='checklista',
            name='fire_transformer_impedance',
            field=models.FloatField(blank=True, null=True, verbose_name='Fire Transformer Impedance'),
        ),
        migrations.AddField(
            model_name='checklista',
            name='fire_transformer_power',
            field=models.FloatField(blank=True, null=True, verbose_name='Fire Transformer Power'),
        ),
        migrations.AddField(
            model_name='checklista',
            name='fire_transformer_type',
            field=models.CharField(blank=True, choices=[('Air', 'Air'), ('Oil', 'Oil')], max_length=3, null=True, verbose_name='Fire Transformer Type'),
        ),
        migrations.AlterField(
            model_name='transformer',
            name='power',
            field=models.FloatField(verbose_name='Transformer Power'),
        ),
    ]

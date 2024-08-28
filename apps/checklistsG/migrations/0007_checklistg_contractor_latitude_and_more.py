# Generated by Django 4.2.4 on 2024-08-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklistsG', '0006_alter_checklistg_contractor_zip_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistg',
            name='contractor_latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Contractor Latitude'),
        ),
        migrations.AddField(
            model_name='checklistg',
            name='contractor_longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Contractor Longitude'),
        ),
        migrations.AddField(
            model_name='checklistg',
            name='work_latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Work Latitude'),
        ),
        migrations.AddField(
            model_name='checklistg',
            name='work_longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Work Longitude'),
        ),
        migrations.AlterField(
            model_name='checklistg',
            name='contractor_zip_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Contractor Zip Code'),
        ),
        migrations.AlterField(
            model_name='checklistg',
            name='work_zip_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Work Zip Code'),
        ),
    ]

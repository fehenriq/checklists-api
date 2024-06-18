# Generated by Django 4.2.4 on 2024-06-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklistsE', '0004_checkliste_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkliste',
            name='contractor_phone',
            field=models.CharField(max_length=15, verbose_name='Contractor Phone'),
        ),
        migrations.AlterField(
            model_name='checkliste',
            name='owner_phone',
            field=models.CharField(max_length=15, verbose_name='Owner Phone'),
        ),
    ]

# Generated by Django 4.2.4 on 2024-06-10 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklistsE', '0003_alter_checkliste_transformer_power'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkliste',
            name='item',
            field=models.CharField(default='1', max_length=3, verbose_name='Item'),
        ),
    ]

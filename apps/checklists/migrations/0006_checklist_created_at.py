# Generated by Django 4.2.4 on 2024-04-19 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checklists', '0005_alter_checklist_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At'),
        ),
    ]

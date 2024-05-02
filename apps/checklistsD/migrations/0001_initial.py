# Generated by Django 4.2.4 on 2024-05-02 14:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checklists', '0006_checklist_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistD',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('process_number', models.CharField(max_length=10, verbose_name='Process Number')),
                ('company', models.CharField(choices=[('Gimi', 'Gimi'), ('GBL', 'GBL'), ('GPB', 'GPB'), ('GS', 'GS'), ('GIR', 'GIR')], default='Gimi', max_length=4, verbose_name='Company')),
                ('concessionaire', models.CharField(blank=True, choices=[('ENEL-SP', 'ENEL-SP')], default='ENEL-SP', max_length=20, null=True)),
                ('other_concessionaire', models.CharField(blank=True, max_length=20, null=True)),
                ('rated_voltage', models.CharField(max_length=20, verbose_name='Rated Voltage')),
                ('transformers_quantity', models.PositiveIntegerField(verbose_name='Transformers Quantity')),
                ('contractor_name', models.CharField(max_length=50, verbose_name='Contractor Name')),
                ('contractor_document', models.CharField(max_length=18, verbose_name='Contractor Document')),
                ('contractor_contact', models.CharField(max_length=50, verbose_name='Contractor Contact')),
                ('contractor_phone', models.CharField(max_length=13, verbose_name='Contractor Phone')),
                ('contractor_street', models.CharField(max_length=255, verbose_name='Contractor Street')),
                ('contractor_number', models.CharField(max_length=20, verbose_name='Contractor Number')),
                ('contractor_complement', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contractor Complement')),
                ('contractor_neighborhood', models.CharField(max_length=100, verbose_name='Contractor Neighborhood')),
                ('contractor_city', models.CharField(max_length=100, verbose_name='Contractor City')),
                ('contractor_state', models.CharField(max_length=50, verbose_name='Contractor State')),
                ('contractor_zip_code', models.CharField(max_length=20, verbose_name='Contractor Zip Code')),
                ('owner_name', models.CharField(max_length=50, verbose_name='Owner Name')),
                ('owner_document', models.CharField(max_length=18, verbose_name='Owner Document')),
                ('owner_contact', models.CharField(max_length=50, verbose_name='Owner Contact')),
                ('owner_phone', models.CharField(max_length=13, verbose_name='Owner Phone')),
                ('work_street', models.CharField(max_length=255, verbose_name='Work Street')),
                ('work_number', models.CharField(max_length=20, verbose_name='Work Number')),
                ('work_complement', models.CharField(blank=True, max_length=255, null=True, verbose_name='Work Complement')),
                ('work_neighborhood', models.CharField(max_length=100, verbose_name='Work Neighborhood')),
                ('work_city', models.CharField(max_length=100, verbose_name='Work City')),
                ('work_state', models.CharField(max_length=50, verbose_name='Work State')),
                ('work_zip_code', models.CharField(max_length=20, verbose_name='Work Zip Code')),
                ('parent_checklist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checklists.checklist', verbose_name='Parent Checklist')),
            ],
        ),
        migrations.CreateModel(
            name='Transformer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.PositiveIntegerField(verbose_name='Transformer Power')),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transformers', to='checklistsD.checklistd')),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-22 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_rename_patientclinicrecord_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.patient'),
        ),
    ]

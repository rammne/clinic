# Generated by Django 4.1.5 on 2023-01-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_patient_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='grade_year_level',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
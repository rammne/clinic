# Generated by Django 4.1.5 on 2023-01-19 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_illness_delete_patientillness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illness',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='illness', to='base.patient', verbose_name='Patient'),
        ),
    ]
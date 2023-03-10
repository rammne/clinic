# Generated by Django 4.1.5 on 2023-01-22 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_visitorslogs_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientClinicRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chief_complains', models.CharField(max_length=50)),
                ('treatments_medication', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='base.patient')),
            ],
        ),
    ]

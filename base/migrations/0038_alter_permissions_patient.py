# Generated by Django 4.1.3 on 2023-02-07 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_alter_permissions_allergy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='base.patient'),
        ),
    ]

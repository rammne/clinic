# Generated by Django 4.1.5 on 2023-01-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='student_number',
            field=models.CharField(default='00x-0000', max_length=10),
        ),
    ]

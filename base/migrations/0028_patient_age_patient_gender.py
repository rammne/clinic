# Generated by Django 4.1.5 on 2023-01-29 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_alter_record_remarks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
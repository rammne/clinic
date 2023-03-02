# Generated by Django 4.1.3 on 2023-02-07 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_patient_grade_year_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vax', models.CharField(max_length=50)),
                ('date_given', models.CharField(max_length=20)),
                ('c1', models.BooleanField(default=False)),
                ('c2', models.BooleanField(default=False)),
                ('c3', models.BooleanField(default=False)),
                ('c4', models.BooleanField(default=False)),
                ('hospital', models.CharField(max_length=50)),
                ('allergy', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=50)),
                ('parents_name', models.TextField()),
                ('date_printed', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='illness',
            options={'verbose_name_plural': 'Illnesses'},
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.CharField(max_length=20, null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='grade_year_level',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Grade/Year Level'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='section',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, verbose_name='Sex'),
        ),
    ]
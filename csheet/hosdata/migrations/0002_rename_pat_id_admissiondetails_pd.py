# Generated by Django 4.1.3 on 2022-11-15 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admissiondetails',
            old_name='pat_id',
            new_name='pd',
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-10 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0005_remove_casesheet_pid_casesheet_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='finalcasesheet',
        ),
    ]
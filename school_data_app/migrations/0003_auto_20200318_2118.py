# Generated by Django 3.0.4 on 2020-03-18 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_data_app', '0002_school_ico_cz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='ico_cz',
            new_name='company_id',
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_data_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='ico_cz',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
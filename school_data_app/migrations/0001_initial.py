# Generated by Django 3.0.4 on 2020-03-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=512, null=True)),
                ('ruian_code', models.CharField(blank=True, max_length=512, null=True)),
                ('address_1', models.CharField(blank=True, max_length=256, null=True)),
                ('address_2', models.CharField(blank=True, max_length=256, null=True)),
                ('address_3', models.CharField(blank=True, max_length=256, null=True)),
                ('principal_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]

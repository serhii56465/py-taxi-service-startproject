# Generated by Django 4.0.3 on 2022-04-02 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='license_number',
            field=models.CharField(max_length=60, null=True, unique=True),
        ),
    ]
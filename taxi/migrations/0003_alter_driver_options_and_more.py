# Generated by Django 4.0.3 on 2022-04-02 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_driver_license_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['username'], 'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='county',
            new_name='country',
        ),
    ]
